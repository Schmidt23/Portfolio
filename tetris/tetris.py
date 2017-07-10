from collections import Counter
import os
import copy
import random

#turn based tetris clone
#every line is wholly my own for better or worse
#Controls: w = switch , a = left, s = down, d = right, q = quit

max_x = 8
max_y = 12



class GameObject():

    def __init__(self, sign, alive, coordinates):
        self.sign = sign
        self.alive = alive
        self.coordinates = coordinates

    def update(self):
        #check position, go 1 row down or stop and "kill" instance
        if self.check_ahead():
            for i in self.coordinates:
                i[0] += 1
        else:
            for i in self.coordinates:
                dead_Objects[(i[0],i[1])]=self.sign
            self.alive = False

    def move_left(self):
        #title
        if self.check_left() and self.check_ahead():
            for i in self.coordinates:
                i[1] -= 1

    def move_right(self):
        #title
        if self.check_right()and self.check_ahead():
            for i in self.coordinates:
                i[1] += 1

    def check_ahead(self):
        #check every element, return true if all can go down
        can_move = 0
        for i in self.coordinates:
            if i[0] < max_y-1 and (i[0]+1,i[1]) not in dead_Objects.keys():
                can_move += 1
        return can_move == 4


    def check_left(self):
        #title
        can_move = 0
        for i in self.coordinates:
            if i[1] > 0 and (i[0], i[1]-1) not in dead_Objects.keys():
                can_move += 1
        return can_move == 4

    def check_right(self):
        #title
        can_move = 0
        for i in self.coordinates:
            if i[1] < max_x-1 and (i[0], i[1]+1) not in dead_Objects.keys():
                can_move += 1
        return can_move == 4


class Bar(GameObject):

    def __init__(self):
        self.sign = "*"
        self.alive = True
        self.bar = [[0,4], [0,5], [0,6],[0,7]]
        self.pipe = [[], [], [], []]
        self.form = self.bar
        self.coordinates = self.form
        #GameObject.__init__(self, "#", True, self.bar)



    def switch(self):
        #list needs deep copy here every other method gets ignored/overwritten
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.bar and self.check_ahead():
            #lowest/max in terms of number on the grid not position
            lowest_x_point = self.coordinates[1][1]
            lowest_y_point = min((i[0] for i in self.coordinates))-1
            max_y_point = lowest_y_point + 4
            max_x_point = lowest_x_point + 2
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #"update" position i.e. lower elements
                for i in self.coordinates:
                    i[0] = lowest_y_point
                    lowest_y_point += 1
                    i[1] = lowest_x_point
                #check if update is possible
                if self.check_ahead():
                    self.form = self.pipe
                #else revert back to previous state
                else:
                    self.coordinates = coord_mem
                    self.form = self.bar
        elif self.form == self.pipe and self.check_ahead():
            #same as above
            lowest_x_point = min((i[1] for i in self.coordinates))-1
            lowest_y_point = self.coordinates[1][0]
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 4
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                for i in self.coordinates:
                    i[1] = lowest_x_point
                    lowest_x_point += 1
                    i[0] = lowest_y_point
                if self.check_ahead():
                    self.form = self.bar
                else:
                    self.coordinates = coord_mem
                    self.form = self.pipe



class Square(GameObject):

    def __init__(self):
        self.sign = "#"
        self.alive = True
        self.coordinates = [[1,6], [1,7], [0,6],[0,7]]

    def switch(self):
        #square doesn't need to switch; I love square
        pass



class Zed(GameObject):

    def __init__(self):
        self.sign = "+"
        self.alive = True
        self.normal = [[0,5], [0,6], [1,6],[1,7]]
        self.up = [[], [], [], []]
        self.form = self.normal
        self.coordinates = self.form



    def switch(self):
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.normal and self.check_ahead():
            lowest_x_point = self.coordinates[0][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 2

            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #all later forms are "hardcoded" postiion changes
                #rest like with Bar() object
                self.coordinates[0][1] += 1
                self.coordinates[1][0] += 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][0] += 1
                self.coordinates[3][1] -= 2
                if self.check_ahead():
                    self.form = self.up
                else:
                    self.coordinates = coord_mem
                    self.form = self.normal


        elif self.form == self.up and self.check_ahead():
            lowest_x_point = self.coordinates[1][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                self.coordinates[0][1] -= 1
                self.coordinates[1][0] -= 1
                self.coordinates[2][1] += 1
                self.coordinates[3][0] -= 1
                self.coordinates[3][1] += 2
                if self.check_ahead():
                    self.form = self.normal
                else:
                    self.coordinates = coord_mem
                    self.form = self.up


class Ess(GameObject):

    def __init__(self):
        self.sign = "%"
        self.alive = True
        self.normal = [[0,6], [0,7], [1,5],[1,6]]
        self.up = [[], [], [], []]
        self.form = self.normal
        self.coordinates = self.form



    def switch(self):
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.normal and self.check_ahead():
            lowest_x_point = self.coordinates[2][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 2


            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:

                self.coordinates[0][0] += 1
                self.coordinates[1][0] += 2
                self.coordinates[1][1] -= 1
                self.coordinates[2][0] -= 1
                self.coordinates[3][1] -= 1
                if self.check_ahead():
                    self.form = self.up
                else:
                    self.coordinates = coord_mem
                    self.form = self.normal


        elif self.form == self.up and self.check_ahead():
            lowest_x_point = self.coordinates[1][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                self.coordinates[0][0] -= 1
                self.coordinates[1][0] -= 2
                self.coordinates[1][1] += 1
                self.coordinates[2][0] += 1
                self.coordinates[3][1] += 1
                if self.check_ahead():
                    self.form = self.normal
                else:
                    self.coordinates = coord_mem
                    self.form = self.up


class Tee(GameObject):

    def __init__(self):
        self.sign = "@"
        self.alive = True
        #forms need "unique" lists or else python would point the var names incorrectly
        self.down = [[0,5], [0,6], [1,6],[0,7]]
        self.upper = [[int, int], [], [], []]
        self.left = [[], [int, int], [], []]
        self.right = [[], [], [int, int], []]
        self.form = self.down
        self.coordinates = self.form



    def switch(self):
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.down and self.check_ahead():
            lowest_x_point = self.coordinates[0][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1


            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[0,5], [0,6], [1,6],[0,7]] --> [[0,6], [1,6], [1,5],[2,6]]
                self.coordinates[0][1] += 1
                self.coordinates[1][0] += 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][0] += 2
                self.coordinates[3][1] -= 1
                if self.check_ahead():
                    self.form = self.left
                else:
                    self.coordinates = coord_mem
                    self.form = self.down


        elif self.form == self.left and self.check_ahead():
            lowest_x_point = self.coordinates[2][1]-1
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 3
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[0,6], [1,6], [1,5],[2,6]] --> [[2,7], [2,6], [1,6],[2,5]]
                self.coordinates[0][0] += 2
                self.coordinates[0][1] += 1
                self.coordinates[1][0] += 1
                self.coordinates[2][1] += 1
                self.coordinates[3][1] -= 1
                if self.check_ahead():
                    self.form = self.upper
                else:
                    self.coordinates = coord_mem
                    self.form = self.left

        elif self.form == self.upper and self.check_ahead():

            lowest_x_point = self.coordinates[3][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[2,7], [2,6], [1,6],[2,5]] --> [[3,5], [2,5], [2,6],[1,5]]
                self.coordinates[0][0] += 1
                self.coordinates[0][1] -= 2
                self.coordinates[1][1] -= 1
                self.coordinates[2][0] += 1
                self.coordinates[3][0] -= 1
                if self.check_ahead():
                    self.form = self.right
                else:
                    self.coordinates = coord_mem
                    self.form = self.upper

        elif self.form == self.right and self.check_ahead():
            lowest_x_point = self.coordinates[3][1]-1
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 2
            #[[[3,5], [2,5], [2,6],[1,5]] -->[[1,4], [1,5], [2,5],[1,6]]
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                self.coordinates[0][0] -= 2
                self.coordinates[0][1] -= 1
                self.coordinates[1][0] -= 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][1] += 1
                if self.check_ahead():
                    self.form = self.down
                else:
                    self.coordinates = coord_mem
                    self.form = self.right

class El(GameObject):

    def __init__(self):
        self.sign = "o"
        self.alive = True
        self.right = [[0,5], [1,5], [2,5],[2,6]]
        self.down = [[int, int], [], [], []]
        self.left = [[], [int, int], [], []]
        self.up = [[], [], [int, int], []]
        self.form = self.right
        self.coordinates = self.form



    def switch(self):
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.right and self.check_ahead():
            lowest_x_point = self.coordinates[0][1]-1
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 2


            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[0,5], [1,5], [2,5],[2,6]] --> [[1,6], [1,5], [1,4],[2,4]]
                self.coordinates[0][0] += 1
                self.coordinates[0][1] += 1
                self.coordinates[2][0] -= 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][1] -= 2
                if self.check_ahead():
                    self.form = self.down
                else:
                    self.coordinates = coord_mem
                    self.form = self.right


        elif self.form == self.down and self.check_ahead():
            lowest_x_point = self.coordinates[2][1]
            lowest_y_point = min((i[0] for i in self.coordinates))-1
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[1,6], [1,5], [1,4],[2,4]] --> [[2,5], [1,5], [0,5],[0,4]]
                self.coordinates[0][0] += 1
                self.coordinates[0][1] -= 1
                self.coordinates[2][0] -= 1
                self.coordinates[2][1] += 1
                self.coordinates[3][0] -= 2
                if self.check_ahead():
                    self.form = self.left
                else:
                    self.coordinates = coord_mem
                    self.form = self.down

        elif self.form == self.left and self.check_ahead():

            lowest_x_point = self.coordinates[3][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 2
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[2,5], [1,5], [0,5],[0,4]] --> [[1,4], [1,5], [1,6],[0,6]]
                self.coordinates[0][0] -= 1
                self.coordinates[0][1] -= 1
                self.coordinates[2][0] += 1
                self.coordinates[2][1] += 1
                self.coordinates[3][1] += 2
                if self.check_ahead():
                    self.form = self.up
                else:
                    self.coordinates = coord_mem
                    self.form = self.left

        elif self.form == self.up and self.check_ahead():
            lowest_x_point = self.coordinates[1][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[1,4], [1,5], [1,6],[0,6]] -->[[0,5], [1,5], [2,5],[2,6]]
                self.coordinates[0][0] -= 1
                self.coordinates[0][1] += 1
                self.coordinates[2][0] += 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][0] += 2
                if self.check_ahead():
                    self.form = self.right
                else:
                    self.coordinates = coord_mem
                    self.form = self.up

class Jay(GameObject):

    def __init__(self):
        self.sign = "o"
        self.alive = True
        self.left = [[0,6], [1,6], [2,6],[2,5]]
        self.up = [[int, int], [], [], []]
        self.right = [[], [int, int], [], []]
        self.down = [[], [], [int, int], []]
        self.form = self.left
        self.coordinates = self.form



    def switch(self):
        coord_mem = copy.deepcopy(self.coordinates[:])
        if self.form == self.left and self.check_ahead():
            lowest_x_point = self.coordinates[3][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 2


            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[0,6], [1,6], [2,6],[2,5]] --> [[1,7], [1,6], [1,5],[0,5]]
                self.coordinates[0][0] += 1
                self.coordinates[0][1] += 1
                self.coordinates[2][0] -= 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][0] -= 2
                if self.check_ahead():
                    self.form = self.up
                else:
                    self.coordinates = coord_mem
                    self.form = self.left


        elif self.form == self.up and self.check_ahead():
            lowest_x_point = self.coordinates[2][1]
            lowest_y_point = min((i[0] for i in self.coordinates))
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 2
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[1,7], [1,6], [1,5],[0,5]] --> [[[2,6], [1,6], [0,6],[0,7]]
                self.coordinates[0][0] += 1
                self.coordinates[0][1] -= 1
                self.coordinates[2][0] -= 1
                self.coordinates[2][1] += 1
                self.coordinates[3][1] += 2
                if self.check_ahead():
                    self.form = self.right
                else:
                    self.coordinates = coord_mem
                    self.form = self.up

        elif self.form == self.right and self.check_ahead():

            lowest_x_point = self.coordinates[2][1]-1
            lowest_y_point = min((i[0] for i in self.coordinates))+1
            max_y_point = lowest_y_point + 1
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[[2,6], [1,6], [0,6],[0,7]] --> [[[1,5], [1,6], [1,7],[2,7]]
                self.coordinates[0][0] -= 1
                self.coordinates[0][1] -= 1
                self.coordinates[2][0] += 1
                self.coordinates[2][1] += 1
                self.coordinates[3][0] += 2
                if self.check_ahead():
                    self.form = self.down
                else:
                    self.coordinates = coord_mem
                    self.form = self.right

        elif self.form == self.down and self.check_ahead():
            lowest_x_point = self.coordinates[0][1]
            lowest_y_point = min((i[0] for i in self.coordinates))-1
            max_y_point = lowest_y_point + 2
            max_x_point = lowest_x_point + 1
            if lowest_x_point >= 0 and lowest_y_point >= 0 and max_x_point <= max_x and max_y_point <= max_y:
                #[[[1,5], [1,6], [1,7],[2,7]] -->[[[1,5], [1,6], [1,7],[2,7]]
                self.coordinates[0][0] -= 1
                self.coordinates[0][1] += 1
                self.coordinates[2][0] += 1
                self.coordinates[2][1] -= 1
                self.coordinates[3][1] -= 2
                if self.check_ahead():
                    self.form = self.left
                else:
                    self.coordinates = coord_mem
                    self.form = self.down

def draw(current_object):
    #draw grid, plus objects if any
    for i in xrange(max_y):
        for j in xrange(max_x):
            if [i,j] in current_object.coordinates and current_object.alive:
                filler = current_object.sign
            elif (i,j) in dead_Objects.keys():
                filler = dead_Objects[(i,j)]
            else:
                filler = " "
            print "|"+filler,
        print "|",i


def check_row(dead_Obs,points):
    #check if row is full
    row_counter = Counter(key[0] for key in dead_Obs.keys())
    for i in row_counter:
        if row_counter[i] == max_x:
            #increase points
            pointsInc(points)
            new_dead_Obs = {}
            #leave every non full row in dead_Obs
            for k,v in dead_Obs.items():
                if k[0] != i:
                    new_dead_Obs[k]=v
            dead_Obs = new_dead_Obs
            #collapse forms
            crumble(dead_Obs)
    return dead_Obs

def crumble(d_O):
    #drops all elements seperately instead of as a whole object
    #makes the game essentially easier to play but was harder to code imho
    #not in origianl tetris but I decided to let it in as it was a pain to get the game to do it
    again = False
    for y,x in sorted(d_O.keys(),reverse=True):
        if y+1 < max_y and (y+1,x) not in d_O.keys():
            #remove old dead element and replace it with updated one
            d_O[(y+1,x)] = d_O.pop((y,x))
            again = True
    if again == True:
        #repeat if one at least one row got updated
        return(crumble(d_O))
    else:
        return d_O

def chooseObject():
    #as title says
    objects = [Jay(),El(),Tee(),Bar(), Square(),Ess(), Zed()]
    objct = random.choice(objects)
    return objct

def pointsInc(p):
    p[0] += 100

curObj = chooseObject()
game = True
dead_Objects = {}
coord_mem = [[]]
points = [0]

while game:
    while curObj.alive:
        inputTimes = 0
        os.system("cls")
        dead_Objects = check_row(dead_Objects,points)
        draw(curObj)
        #inputTimes allows 2 moves to left/right before form gets updated/lowered
        while inputTimes < 2 and curObj.alive:
            print points[0]
            print curObj.coordinates
            print dead_Objects
            inp = raw_input("inp ")
            #w=switch, a=left, s=down, d=right, q=quit
            if inp == "a":
                curObj.move_left()
                inputTimes += 1
                os.system("cls")
                draw(curObj)
            elif inp == "d":
                curObj.move_right()
                inputTimes += 1
                os.system("cls")
                draw(curObj)
            elif inp == "s":
                inputTimes += 2
                curObj.update()
                os.system("cls")
                draw(curObj)
            elif inp == "w":
                inputTimes += 1
                curObj.switch()
                os.system("cls")
                draw(curObj)
            elif inp == "q":
                curObj.alive=False
                game = False
        curObj.update()
    dead_Objects = check_row(dead_Objects,points)
    nextObj = chooseObject()
    curObj = nextObj

