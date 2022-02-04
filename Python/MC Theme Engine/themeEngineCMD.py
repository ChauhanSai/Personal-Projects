import os
import numpy as np
from PIL import Image


def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


mainColor = eval(input("Main color: "))
# 71,111,206
borderColorRed, borderColorGreen, borderColorBlue = lighten_color('#%02x%02x%02x' % mainColor, 1.75)
borderColor = round(borderColorRed*255), round(borderColorGreen*255), round(borderColorBlue*255)

accentColor = eval(input("Accent color: "))
# 184,144,48
accentColorDarkRed, accentColorDarkGreen, accentColorDarkBlue = lighten_color('#%02x%02x%02x' % accentColor, 1.5)
accentColorDark = round(accentColorDarkRed * 255), round(accentColorDarkGreen * 255), round(accentColorDarkBlue * 255)

accentColorDarkLightRed, accentColorDarkLightGreen, accentColorDarkLightBlue = lighten_color(
    '#%02x%02x%02x' % accentColorDark, .9)
accentColorDarkLight = round(accentColorDarkLightRed * 255), round(accentColorDarkLightGreen * 255), round(
    accentColorDarkLightBlue * 255)

accentColorLightRed, accentColorLightGreen, accentColorLightBlue = lighten_color('#%02x%02x%02x' % accentColor, .6)
accentColorLight = round(accentColorLightRed * 255), round(accentColorLightGreen * 255), round(
    accentColorLightBlue * 255)

ui = [f for f in os.listdir("ui") if os.path.isfile(os.path.join("ui", f))]
colors = ["198, 198, 198", mainColor,
          "0, 0, 0", borderColor,
          "67, 160, 28", accentColor]
          #"2, 95, 0", accentColorDark,
          #"3, 115, 0", accentColorDarkLight,
          #"55, 214, 30", accentColorLight]

for i in range(len(ui)):
    fileName = "ui/"
    fileName += ui[i]
    im = Image.open(fileName)
    im = im.convert('RGBA')
    data = np.array(im)
    red, green, blue, alpha = data.T

    # Replace replaceToRed, Green, Blue with replaceWith... (leaves alpha values alone...)
    j = 0
    while j < len(colors):
        replaceTo = eval(colors[j])
        replaceToRed, replaceToBlue, replaceToGreen = replaceTo
        replaceWith = colors[j + 1]
        print(replaceTo)
        print(replaceWith)
        print("")

        color = (red == replaceToRed) & (blue == replaceToBlue) & (green == replaceToGreen)
        data[..., :-1][color.T] = replaceWith

        j += 2

    try:
        os.makedirs("myUI")
    except Exception:
        pass
    fileName = fileName.replace("ui", "myUI")
    Image.fromarray(data).save(fileName)
