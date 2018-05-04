"""Just a simple representation of a digital clock in 24-hour format."""

import time
import os

# map elements of digital number to its corresponding integer/ symbol to symbol
digital = {"1": ["   ", "  |", "  |"], "2": [" _ ", " _|", "|_ "], "3": [" _ ", " _|", " _|"],
           "4": ["   ", "|_|", "  |"], "5": [" _ ", "|_ ", " _|"], "6": [" _ ", "|_ ", "|_|"],
           "7": [" _ ", "  |", "  |"],
           "8": [" _ ", "|_|", "|_|"], "9": [" _ ", "|_|", "  |"], "0": [" _ ", "| |", "|_|"],
           ":": ["   ", " o ", " o "],
           " ": ["   ", "   ", "   "]
           }


def display(clck):
    # 3 elements per numeral
    for i in xrange(3):
        # number elements in current time
        for j in clck:
            # print complete row
            print "%s" % digital[j][i],
        # move to next row
        print


disp = True

if __name__ == "__main__":
    while True:
        now = time.localtime()
        # switch between displaying ':' and omitting it to achieve the blink effect
        if disp:
            clock = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
            disp = False
        else:
            clock = "%02d %02d %02d" % (now.tm_hour, now.tm_min, now.tm_sec)
            disp = True
        # command is of course system dependent
        os.system('cls')
        display(clock)
        # sleep can be responsible for delay/hiccups but is preferable to not having it
        time.sleep(1)
