import tweepy
from PIL import Image, ImageDraw, ImageFont
import os
import requests
from io import BytesIO

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

# CHANGE THIS
red, green, blue = eval("")
message = ""

# setColor
rgb = (red, green, blue)
rgbString=str(red)+", "+str(green)+", "+str(blue)
hexString = '#%02x%02x%02x' % rgb
fileName = hexString
fileName += ".png"

# create image
if (red+green+blue)/3>125 :
    fontColor = (0,0,0)
    overlay = requests.get("https://chauhansai.github.io/Script-Projects/Python/colorRand/Overlay.png")
else:
    fontColor = (255,255,255)
    overlay = requests.get("https://chauhansai.github.io/Script-Projects/Python/colorRand/Overlay_Invert.png")
Font = requests.get("https://chauhansai.github.io/Script-Projects/Python/colorRand/AtkinsonHyperlegible-Regular.ttf")

color = Image.new('RGBA', (1920, 1080), (red, green, blue, 255))
hexFont = ImageFont.truetype(BytesIO(Font.content), 80)
rgbFont = ImageFont.truetype(BytesIO(Font.content), 60)
userFont = ImageFont.truetype(BytesIO(Font.content), 40)
d = ImageDraw.Draw(color)
d.text((70,870), hexString, font=hexFont, fill=fontColor)
d.text((70,950), rgbString, font=rgbFont, fill=fontColor)
d.text((1635,970), "@colorRand", font=userFont, fill=fontColor)
logo = Image.open(BytesIO(overlay.content)) 
color.paste(logo, (0, 0), logo) 

color.save(fileName)

media = api.media_upload(fileName)

# Post tweet with image
if message != "":
    tweet = message+"\nHex: "+hexString+"\nRGB: "+rgbString+"\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color="+hexString.replace("#","")
else:
    tweet = "Hex: "+hexString+"\nRGB: "+rgbString+"\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color="+hexString.replace("#","")
post_result = api.update_status(status=tweet, media_ids=[media.media_id])

os.remove(fileName)

print(hexString)
