#checks every 15 seconds if local time == given alarm, if so opens random yt video from
#content.txt in webbrowser

import webbrowser
import random
import time
import random 
import os

# time is displayed as digital clock 
digital = {"1":["   ","  |", "  |"], "2":[" _ "," _|", "|_ "], "3":[" _ ", " _|", " _|"], 
	"4":["   ","|_|","  |"],"5":[" _ ", "|_ ", " _|"], "6":[" _ ", "|_ ", "|_|"], "7":[" _ ", "  |", "  |"],
	"8":[" _ ", "|_|", "|_|"],"9":[" _ ", "|_|", "  |"], "0":[" _ ","| |","|_|"], ":":["   ", " o ", " o "],
	" ":["   ", "   ", "   "]
}


def display(clock):
	for i in xrange(3):
		for j in clock:
			print digital[j][i]+"\f",
		print


def open_link():
	print "opening"
	#open file, get random link and open in webbrowser
	content = 'content.txt'
	x = open(content, 'r')
	line = x.readlines()
	randomLink = random.choice(line)
	x.close()
	webbrowser.open(randomLink)

setTime = raw_input("Alarm? ")
#split input into tuple of hour and minutes
hour, minute = int(setTime[:2]), int(setTime[2:])
alarm = (hour, minute)


flag = False

	#check if time == alarm if not keep in loop
while (not flag):
	#update time
	os.system('clear')
	now = time.localtime()
	clock = "%02d" % now.tm_hour +":"+ "%02d" % now.tm_min
	display(clock)
	if alarm != (now.tm_hour,now.tm_min):
		time.sleep(15)
	elif alarm == (now.tm_hour,now.tm_min):
		print "wat"
		open_link()
		#set Flag to stop loop
		flag = True





