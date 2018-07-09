#imgur ClientSecret: ****************
import praw
import pyimgur
import re
import os

#get imgur links from reddit submissions and download them to folder

Client_ID = "*****"
im = pyimgur.Imgur(Client_ID)

r = praw.Reddit(client_id='*****',
                client_secret="*****",
                password='*****', user_agent="pythonScripts:0001:by/u/*****",
                username='93n15bot')


subreddit_name = "*****"

subreddit = r.subreddit(subreddit_name)



def append_to_file(path, data):
    with open(path, "a") as f:
        f.write(data + "\n")

def file_to_set(file_name):
    results = set()
    with open(file_name, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

#logfile that checks if images have been downloaded before
f = "log.txt"
already = file_to_set(f)

def saug(subreddit):

    for submission in subreddit.hot(limit=5):
        link = submission.url
        if submission.domain.endswith('imgur.com') and link not in already:
            try:
                append_to_file(f, link)
                imID = re.split("/", link)[-1]
                #check if single picture or album
                rmext = re.search(r'\w+(\.\w+)',imID)
                if rmext:
                    #if single pic
                    imID = re.split("\.", imID)[0]
                    #download
                    image = im.get_image(imID)
                    image.download(path="imdls", name="%s" %imID)
                else:
                    #create album folder, then download all pics
                    album = im.get_album(imID)
                    create_folder("imdls/%s" %imID)
                    for i in album.images:
                        i.download(path="imdls/%s"%imID)
            except Exception, e:
                 print e
                 print
                 pass

create_folder("imdls")
saug(subreddit)
