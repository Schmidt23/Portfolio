from dotenv import load_dotenv
import os
import praw
import datetime
import logging_posts

load_dotenv()

CLIENT_ID = os.getenv('REDDIT_CID')
CLIENT_SECRET = os.getenv('REDDIT_CS')
PASSWORD = os.getenv('REDDIT_PW')
USER_AGENT = os.getenv('REDDIT_UA')
USERNAME = os.getenv('REDDIT_UN')



r = praw.Reddit(client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                password=PASSWORD,
                user_agent=USER_AGENT,
                username=USERNAME)

hl= r.subreddit("Hololive")

mods =[mod for mod in hl.moderator()]

def check_age(submission_age):
    now = datetime.datetime.now()
    return now -datetime.datetime.utcfromtimestamp(submission_age) < datetime.timedelta(days=2)

def check_submissions():
    logging_posts.clear_log()
    posts = logging_posts.read_log()
    print(posts)
    link = None
    for submission in hl.new(limit=100,):
        if submission.author in mods and check_age(submission.created_utc) and submission.id not in posts:
            logging_posts.append_log(submission.id)
            posts = logging_posts.read_log()
            link = submission.permalink
            break
    return link
