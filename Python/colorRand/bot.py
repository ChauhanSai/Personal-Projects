import tweepy
import random
from PIL import Image
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###",
    "###")
auth.set_access_token("###",
    "###")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###", "###")
auth.set_access_token("###", "###")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# generate
red = round(random.random()*256)
green = round(random.random()*256)
blue = round(random.random()*256)

# setColor
rgb = (red, green, blue)
rgbString=str(red)+", "+str(green)+", "+str(blue)
hexString = '#%02x%02x%02x' % rgb
fileName = hexString
fileName += ".png"

color = Image.new('RGBA', (1920, 1080), (red, green, blue, 255))
color.save(fileName)

media = api.media_upload(fileName)

# Post tweet with image
tweet = "Hex: "+hexString+"\nRGB: "+rgbString+"\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color="+hexString.replace("#","")
post_result = api.update_status(status=tweet, media_ids=[media.media_id])

os.remove(fileName)

print(hexString)