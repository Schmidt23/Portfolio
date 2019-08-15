#! -*- coding: utf-8 -*-

# checks if local time == given alarm, if so opens random yt video from
# content.txt in webbrowser
# no feed without declaring at least one symbol group (tree, asciis, japemoji)
import random
import time
import os
import argparse
import sys
import datetime as dt


def bar(it):
    w_bar = ["/", "--", "\\", "|"]
    r_bar = ["\x1b[1;31;48m/\x1b[0m", "\x1b[1;31;48m--\x1b[0m", "\x1b[1;31;48m\\\x1b[0m", "\x1b[1;31;48m|\x1b[0m"]
    return w_bar[it]


def tree(n):
    # define 'leafs'
    """symsyms = ["\x1b[1;31;48m*\x1b[0m", "\x1b[1;32;48m'\x1b[0m","\x1b[1;31;48m'\x1b[0m",
                        "\x1b[1;32;48m*\x1b[0m", '*', "'"]
    """
    symsyms = ["*", "'"]

    # empty string used for indentation -shrinking
    emp = " "
    # multiplier for symbols
    mult = 1
    # multiplier for empty/whitespace; starts at same value as n but decreases per row
    emult = n
    # root
    trunk = 1
    # collection of leaf rows
    leafs = []
    for row in xrange(n):
        # symbols starts empty
        sym = []
        # choose a random leaf
        sym.append(random.choice(symsyms))
        # append random choice to symbol string
        [sym.append(random.choice(symsyms)) for sy in xrange(1,mult)]
        # add current row (12 is max time and center of tree)
        #n = baseline indentation(fixed); emp*multiplier is shrinking portion per row
        #ensures halfwaypoint is always in middle
        leafs.append("{}{}{}\n".format(' '*(11-n),emp*emult,"".join(sym)))
        if mult < n - 1:
            # trunk keeps growing until it#s bigger than number of rows
            trunk = mult
        # grow symbol multiplier and reduce whitespace
        mult += 2
        emult -= 1

    output = []
    output.append("".join(leafs))
    # finally create trunk via defining whitespace and trunk itself
    # same principle as above
    output.append("{}{}{}".format(' '*(11-n),emp*(mult /2 -trunk/2), "#"*trunk))
    #print 11-n
    #print emp*emult
    return "".join(output)


# time is displayed as digital clock
digital = {"1": ["   ", "  |", "  |"], "2": [" _ ", " _|", "|_ "], "3": [" _ ", " _|", " _|"],
           "4": ["   ", "|_|", "  |"], "5": [" _ ", "|_ ", " _|"], "6": [" _ ", "|_ ", "|_|"],
           "7": [" _ ", "  |", "  |"],
           "8": [" _ ", "|_|", "|_|"], "9": [" _ ", "|_|", "  |"], "0": [" _ ", "| |", "|_|"],
           ":": ["   ", " o ", " o "],
           " ": ["   ", "   ", "   "]
           }


def display(clock):
    clout = []
    # 3 elements per numeral
    #for i in xrange(3):
        # number elements in current time
    clout = ("".join((digital[j][i] for j in clock)) for i in xrange(3))
        #for j in clock:
            # append complete row
            #clout.append("%s" % digital[j][i])
        #clout.append("\n")
    return "\n".join(clout)


def open_link():
    import webbrowser
    print "opening"
    # open file, get random link and open in webbrowser
    content = 'content.txt'
    with open(content, 'r') as x:
        line = x.readlines()
        randomLink = random.choice(line)
    webbrowser.open(randomLink)


def time_til(time, alarm):
    start = time[:5]
    end = "{}:{}".format(str(alarm[0]), str(alarm[1]))
    start_dt = dt.datetime.strptime(start, '%H:%M')
    end_dt = dt.datetime.strptime(end, '%H:%M')
    diff = (end_dt - start_dt)
    hours = diff.seconds / 3600
    if hours > 12:
        hours = 12
    elif hours < 0:
        hours = 12
    elif hours == 0:
        hours = 1

    if int(str(diff).split(':')[1]) > 30:
        hours += 1

    return hours


def render_disout(src):
    #choose picture string from source list
    choice = random.choice(src)
    #only use tree generator if tree is chosen
    if args.tree:
        #src[0] = "{}".format("\n" * tree_len)
        if src.index(choice) == 0:
                    tree_out = [tree(tree_len)]
                    choice = "{}".format("".join(tree_out))
        else:
            choice = random.choice(src[1:])
    #get highest amount of newlines in source strings
    max_len = max((string.count("\n") for string in src))
    #get amount of newlines in chosen string
    choice_len = choice.count("\n")
    #get even amount of newlines
    new_lines = "\n" * (max_len - choice_len)
    #add missing newlines and format output unicode
    return "{}{}".format(new_lines, choice.encode("utf-8"))


def render_ticker(index, text):
    return "    " + text[index:index + 15]


def fill_ticker(feed='https://www.heise.de/rss/heise-atom.xml'):
    import feedparser
    d = feedparser.parse(feed)
    headlines = []
    for i in xrange(len(d.entries)):
        headlines.append(d.entries[i].title)
    return "...".join(headlines).encode("utf-8")

# set initial vars. functions will only be called when they have to update

setTime = raw_input("Alarm? ")
# split input into tuple of hour and minutes
hour, minute = int(setTime[:2]), int(setTime[2:])
alarm = (hour, minute)

flag = False
cmd = 'cls' if os.name == 'nt' else 'clear'
bardisp = bar(0)
bar_it = -1


ascii_1 = "\t.___.\n\t{o,o}\n\t/)__)\n\t-\"-\"-"
ascii_11 = "\t.___.\n\t{o,o}\n\t(__(\\\n\t-\"-\"-"
ascii_2 = "\t (\_/)\n\t(='.'=)\n\t(\")_(\")"
ascii_22 = "\t (\_/)\n\t(=*.*=)\n\t(\")_(\")"
d_1 = u"      (ノ￣ー￣)ノ"
d_2 = u"      ＼(^ω^＼)"
d_3 = u"      (〜￣△￣)〜"
d_33 =u"      〜(￣△￣ 〜)"
d_4 = u"      （〜^∇^)〜"
d_44 = u"      〜(^∇^〜)"
d_5 = u"      (ノ￣ω￣)ノ"
k = 0
ticker = "\t All work and no play make Jack a dull boy."
dis_out = ""
al_text = "      Alarm: %02d:%02d" % (alarm[0], alarm[1])

if __name__ == "__main__":
    #define sysargs
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tree", action="store_true",
                        help="activate tree")
    parser.add_argument("-a", "--ascii", action="store_true",
                        help="activate ascii")
    parser.add_argument("-j", "--japanese", action="store_true",
                        help="activate japanese emoji")
    parser.add_argument("-f", "--feed", nargs='?', const='https://www.heise.de/rss/heise-atom.xml',
                        help="display rss feed default=heise.de")
    args = parser.parse_args()

    #get initial tree length
    now = time.localtime()
    clock = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
    tree_len = time_til(clock, alarm)
    org_tree_len = tree_len
    #initial tree
    tree_out = [tree(tree_len)]

    #parse sysargs and fill picture_string list
    disp_choice = []
    #if no args are given all pics can be displayed but not feed
    if len(sys.argv)==1:
        args.ascii = True
        args.japanese = True
        args.tree = True

    if args.feed:
        print args.feed
        ticker = fill_ticker(feed=args.feed)

    if args.tree:
        disp_choice += tree_out

    if args.ascii:
        asciiL = [ascii_1, ascii_11, ascii_2, ascii_22]
        disp_choice += asciiL

    if args.japanese:
        japL = [d_1, d_2, d_3, d_33, d_4, d_44, d_5]
        disp_choice += japL


# check if time == alarm if not keep in loop
    while not flag:
        #update time continuously
        now = time.localtime()
        clock = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
        tree_len = time_til(clock, alarm)
        #update feed based on tree_len, i.e once per hour
        if tree_len < org_tree_len:
            ticker = fill_ticker()
            org_tree_len = tree_len
        #update clock
        time_disp = display(clock)
        #if ticker list is once through, go back to beginning
        k = (k + 1 if k < len(ticker) else 0)
        #update bar
        bar_it = (bar_it + 1 if bar_it <= 2 else 0)
        bardisp = bar(bar_it)
        #create bars
        bdsp = "  {} ".format((bardisp + " ") * 11)
        #create ticker
        tckr = render_ticker(k, ticker)
        #create complete output
        print_list = [bdsp, dis_out, tckr, al_text, time_disp, bdsp]

        dis_out = (render_disout(disp_choice) if bar_it > 2 else dis_out)
        print "\n".join(print_list)
        time.sleep(0.1)
        #check if time == alarm
        if alarm == (now.tm_hour, now.tm_min):
            #choose link and open browser
            open_link()
            # set Flag to stop loop
            flag = True
        #clear the screen
        os.system(cmd)
    sys.exit(0)
