# checks if local time == given alarm, if so opens random yt video from
# content.txt in webbrowser

import webbrowser
import random
import time
import random
import os


def bar(it):
    test =["/", "-", "\\", "|"]
    return test[it]


def tree(n):
    # define 'leafs'
    symsyms = ["*", "'"]
    # empty string used for indentation
    emp = " "
    # multiplier for symbols
    mult = 1
    # multiplier for empty/whitespace
    emult = n
    # root
    trunk = 1
    # collection of leaf rows
    leafs = ""
    for row in xrange(n):
        # symbols starts as empty string
        sym = ""
        # choose a random leaf
        sym = random.choice(symsyms)

        for sy in xrange(1, mult):
            # append random choice to symbol string
            sym += random.choice(symsyms)
        # add current row
        leafs += "       " + emp * emult + sym + "\n"

        if mult < n - 1:
            # trunk keeps growing until it#s bigger than number of rows
            trunk = mult
        # grow symbol multiplier and reduce whitespace
        mult += 2
        emult -= 1

    output = ""
    output += leafs
    # finally create trunk via defining whitespace and trunk itself
    output += "       " + emp * (mult / 2 - trunk / 2) + "#" * (trunk)
    return output


# time is displayed as digital clock
digital = {"1": ["   ", "  |", "  |"], "2": [" _ ", " _|", "|_ "], "3": [" _ ", " _|", " _|"],
           "4": ["   ", "|_|", "  |"], "5": [" _ ", "|_ ", " _|"], "6": [" _ ", "|_ ", "|_|"],
           "7": [" _ ", "  |", "  |"],
           "8": [" _ ", "|_|", "|_|"], "9": [" _ ", "|_|", "  |"], "0": [" _ ", "| |", "|_|"],
           ":": ["   ", " o ", " o "],
           " ": ["   ", "   ", "   "]
           }


def display(clock):
    clout = ""
    # 3 elements per numeral
    for i in xrange(3):
        # number elements in current time
        for j in clock:
            # append complete row
            clout += "%s" % digital[j][i]
        clout += "\n"
    return clout


def open_link():
    print "opening"
    # open file, get random link and open in webbrowser
    content = 'content.txt'
    with open(content, 'r') as x:
        line = x.readlines()
        randomLink = random.choice(line)
    webbrowser.open(randomLink)


setTime = raw_input("Alarm? ")
# split input into tuple of hour and minutes
hour, minute = int(setTime[:2]), int(setTime[2:])
alarm = (hour, minute)

flag = False 
cmd = 'cls' if os.name=='windows' else 'clear'
tree_out = tree(5)
bardisp = bar(0)
bar_it = -1

# check if time == alarm if not keep in loop
while (not flag):

    now = time.localtime()
    clock = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
    if bar_it <= 2:
        bar_it += 1
        bardisp = bar(bar_it)
        print "  "+(bardisp+" ") * 11
        print tree_out
        time_disp = display(clock)
        print time_disp
        print "  "+(bardisp+" ") * 11
        time.sleep(0.1)
    else:
        # update tree display after bar list was looped through
        bar_it = 0
        bardisp = bar(bar_it)
        tree_out = tree(5)
        time_disp = display(clock)
        print "  "+(bardisp+" ") * 11
        print tree_out
        print time_disp
        print "  "+(bardisp+" ") * 11
        time.sleep(0.1)

    if alarm == (now.tm_hour, now.tm_min):
        print "wat"
        open_link()
        # set Flag to stop loop
        flag = True
    os.system(cmd)
