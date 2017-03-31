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

#check if time == alarm if not keep in loop
while (alarm != now):
    #update time
    t = time.localtime()
    now = t.tm_hour, t.tm_min
    print "Time: ",time.strftime("%H:%M"), "Alarm: ","%d:%d" %(hour, minute)
    time.sleep(15)

#if out of loop
if alarm == now:
    #open file, get random link and open in webbrowser
    content = 'content.txt'
    x = open(content, 'r')
    line = x.readlines()
    randomLink = random.choice(line)
    x.close()
    webbrowser.open(randomLink)





