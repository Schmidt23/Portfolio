#! enc=utf-8
import pyimgur
import os
import random
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("I_C_ID")
im = pyimgur.Imgur(CLIENT_ID)


def link_cutie():
    gallery = im.get_subreddit_gallery("eyebleach", sort='new', limit=50)
    if len(gallery)<1:
        return "No images"
    else:
        image = random.choice(gallery)
        return im.get_image(image.id).link


print(link_cutie())