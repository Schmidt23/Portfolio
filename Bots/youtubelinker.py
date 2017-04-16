import praw
import time
import re
import pafy

#scans reddit comments for yt links and retrieves(if able) title and length
#with possibilty of posting info as reply

r = praw.Reddit(client_id='*****',
                client_secret="*****",
                password='*****', user_agent="pythonScripts:0001:by/u/*****",
                username='*****')
parsed = set()

#format raw seconds data into h:m:s format
def ftime(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

while True:
    #getsubbreddit
    subreddit = r.subreddit("all")  
    #search comments in subreddit
    new_comments = subreddit.comments()
    for comment in new_comments:
        cmt = comment.body
        #look for yt links
        bot = re.search(r"https://www.youtube.com/watch\?v=(\w+-*\w+)", cmt)
        if bot:
            #if found check i not already posted
            if bot.group() in comment.body and comment.id not in parsed:
                parsed.add(comment.id)
                iD = bot.group(1)
                try:
                    #get video and info and post comment/print it out
                    url = "http://www.youtube.com/watch?v=%s" % iD
                    video = pafy.new(url)
                    tit = video.title
                    tim = ftime(video.length)
                    comment.reply("Title: %s \n\nDuration: %s" % (tit,tim))
                    print "URL: %s\nTitle: %s\nDuration: %s\n" % (url, tit, tim)
                except Exception, e:
                    print e
                    print
                    pass
        else:
            print "Nothing for now"
            time.sleep(5)