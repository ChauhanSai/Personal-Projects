import random
from datetime import datetime
from io import BytesIO
from os import remove

import tweepy
from PIL import Image, ImageDraw, ImageFont
from pytz import timezone
from requests import get

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###",
                           "###")
auth.set_access_token("###",
                      "###")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###", "###")
auth.set_access_token("###",
                      "###")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Log
tz = timezone('America/Chicago')
today = datetime.now(tz).strftime("%y%m%d")
print(today)

# Generate
message = ""
# REGULAR
rgb = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

# OVERRIDE      # Date "%y%M%D", "r, g, b", message ""
overrideArray = [["220330", "77,210,254", "I never had to look farther than the darkness inside my own heart.\n#MarvelStudios' #MoonKnight"],
                 ["220401", "84,163,163", "Sony Pictures' #Morbius"],
                 ["220506", "220, 6, 3", "Forget everything that you think you know.\n#MarvelStudios' #DrStrange #MultiverseOfMadness"]]

for i in range(len(overrideArray)):
    if today in overrideArray[i][0]:
        rgb = eval(overrideArray[i][1])
        message = overrideArray[i][2]
        print("Override", today)
        print(message)
        break

typeRandom = random.random()
if typeRandom <= .01:
    # GRAYSCALE
    gray = random.randint(0, 256)
    rgb = (gray, gray, gray)
    print("Feeling Gray")
else:
    if typeRandom <= .02:
        # SINGLE
        rRGB = [0, 0, 0]
        colors = ['Red', 'Green', 'Blue']
        num = random.randint(0, 3)
        rRGB[num] = random.randint(0, 256)
        rgb = eval(str(rRGB[0]) + ", " + str(rRGB[1]) + ", " + str(rRGB[2]))
        message = "Feeling " + colors[num]
        print(message)

red, green, blue = rgb
rgbString = str(red) + ", " + str(green) + ", " + str(blue)
hexString = '#%02x%02x%02x' % rgb
fileName = hexString
fileName += ".png"

# Create image
if (red + green + blue) / 3 > 125:
    fontColor = (0, 0, 0)
    overlay = get("https://chauhansai.github.io/Script-Projects/Python/colorRand/Overlay.png")
else:
    fontColor = (255, 255, 255)
    overlay = get("https://chauhansai.github.io/Script-Projects/Python/colorRand/Overlay_Invert.png")
Font = get("https://chauhansai.github.io/Script-Projects/Python/colorRand/AtkinsonHyperlegible-Regular.ttf")

color = Image.new('RGBA', (1920, 1080), (red, green, blue, 255))
hexFont = ImageFont.truetype(BytesIO(Font.content), 80)
rgbFont = ImageFont.truetype(BytesIO(Font.content), 60)
userFont = ImageFont.truetype(BytesIO(Font.content), 40)
d = ImageDraw.Draw(color)
d.text((70, 870), hexString, font=hexFont, fill=fontColor)
d.text((70, 950), rgbString, font=rgbFont, fill=fontColor)
d.text((1635, 970), "@colorRand", font=userFont, fill=fontColor)
logo = Image.open(BytesIO(overlay.content))
color.paste(logo, (0, 0), logo)

color.save(fileName)
print("File saved")
print("...")
media = api.media_upload(fileName)

# Post tweet with image
if message != "":
    tweet = message + "\nHex: " + hexString + "\nRGB: " + rgbString + "\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color=" + hexString.replace(
        "#", "")
else:
    tweet = "Hex: " + hexString + "\nRGB: " + rgbString + "\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color=" + hexString.replace(
        "#", "")
post_result = api.update_status(status=tweet, media_ids=[media.media_id])

remove(fileName)

print(hexString)
