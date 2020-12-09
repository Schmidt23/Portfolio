from dotenv import load_dotenv
import os
import praw
import datetime

load_dotenv()

CLIENT_ID = os.getenv('REDDIT_CID')
CLIENT_SECRET = os.getenv('REDDIT_CS')
PASSWORD = os.getenv('REDDIT_PW')
USER_AGENT = os.getenv('REDDIT_UA')
USERNAME = os.getenv('REDDIT_UN')

posts = []
print(posts)

r = praw.Reddit(client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                password=PASSWORD,
                user_agent=USER_AGENT,
                username=USERNAME)

hl= r.subreddit("Hololive")

mods =[mod for mod in hl.moderator()]

def check_age(submission_age):
    now = datetime.datetime.now()
    return now -datetime.datetime.utcfromtimestamp(submission_age) < datetime.timedelta(days=5)

def check_submissions():
    clear_posts(posts)
    link = None
    for submission in hl.new(limit=100,):
        if submission.author in mods and check_age(submission.created_utc) and submission.id not in posts:
            posts.append(submission.id)
            link = submission.permalink
            break
    return link


def clear_posts(posts):
    if len(posts)>=10:
        posts = posts[8:]