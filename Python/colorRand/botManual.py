import tweepy
import random
import time
from PIL import Image, ImageDraw, ImageFont
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

timeBreak = 86400.0

print("Waiting ("+str(round(timeBreak - ((time.time() - 1633798800) % timeBreak)))+")")

while True:
    time.sleep(timeBreak - ((time.time() - 1633798800) % timeBreak))

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

    # create image
    if (red+green+blue)/3>125 :
        fontColor = (0,0,0)
        overlay = "Overlay.png"
    else:
        fontColor = (255,255,255)
        overlay = "Overlay_Invert.png"

    color = Image.new('RGBA', (1920, 1080), (red, green, blue, 255))
    hexFont = ImageFont.truetype('AtkinsonHyperlegible-Regular.ttf', 80)
    rgbFont = ImageFont.truetype('AtkinsonHyperlegible-Regular.ttf', 60)
    userFont = ImageFont.truetype('AtkinsonHyperlegible-Regular.ttf', 40)
    d = ImageDraw.Draw(color)
    d.text((70,870), hexString, font=hexFont, fill=fontColor)
    d.text((70,950), rgbString, font=rgbFont, fill=fontColor)
    d.text((1635,970), "@colorRand", font=userFont, fill=fontColor)
    logo = Image.open(overlay) 
    color.paste(logo, (0, 0), logo) 

    color.save(fileName)

    media = api.media_upload(fileName)

    # Post tweet with image
    tweet = "Hex: "+hexString+"\nRGB: "+rgbString+"\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color="+hexString.replace("#","")
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

    os.remove(fileName)

    print(hexString)
