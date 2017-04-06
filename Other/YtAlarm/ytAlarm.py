#checks every 15 seconds if local time == given alarm, if so opens random yt video from
#content.txt in webbrowser

import webbrowser
import random
import time


setTime = raw_input("Alarm? ")
#split input into tuple of hour and minutes
hour, minute = int(setTime[:2]), int(setTime[2:])
alarm = (hour, minute)

t = time.localtime()
now = t.tm_hour, t.tm_min
flag = False

#check if time == alarm if not keep in loop
while (not flag):
    #update time
    t = time.localtime()
    now = t.tm_hour, t.tm_min
    print "Time: ",time.strftime("%H:%M"), "Alarm: ","%02d:%02d" %(hour, minute)
    if alarm != now:
        time.sleep(15)
    elif alarm == now:
        #open file, get random link and open in webbrowser
        #AND SET FLAG !!!!!!!!!!!
        content = 'content.txt'
        x = open(content, 'r')
        line = x.readlines()
        randomLink = random.choice(line)
        x.close()
        webbrowser.open(randomLink)
        flag = True




