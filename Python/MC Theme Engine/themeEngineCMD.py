import os
import shutil
import uuid
import numpy as np
from PIL import Image
import webcolors


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


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


def pix(img, loc, color):
    """
    Sets pixel color and returns image object
    :param img : image object
    :type img: PIL.Image.Image
    :param loc: length 2 tuple pos
    :type loc: tuple
    :param color: length 3 tuple rbg
    :type color: tuple
    :returns PIL.Image.Image
    """
    im = img.load()
    im[loc] = color

    return img

# TODO : Add fail safe
mainColor = eval(input("Main color: "))

borderColorRed, borderColorGreen, borderColorBlue = lighten_color('#%02x%02x%02x' % mainColor, 1.75)
borderColor = round(borderColorRed * 255), round(borderColorGreen * 255), round(borderColorBlue * 255)

accentColor = eval(input("Accent color: "))

accentColorDarkRed, accentColorDarkGreen, accentColorDarkBlue = lighten_color('#%02x%02x%02x' % accentColor, 1.5)
accentColorDark = round(accentColorDarkRed * 255), round(accentColorDarkGreen * 255), round(accentColorDarkBlue * 255)


accentColorLightRed, accentColorLightGreen, accentColorLightBlue = lighten_color('#%02x%02x%02x' % accentColor, .6)
accentColorLight = round(accentColorLightRed * 255), round(accentColorLightGreen * 255), round(
    accentColorLightBlue * 255)

try:
    accentColorDarkLightRed, accentColorDarkLightGreen, accentColorDarkLightBlue = lighten_color(
        '#%02x%02x%02x' % accentColorDark, .9)
    accentColorDarkLight = round(accentColorDarkLightRed * 255), round(accentColorDarkLightGreen * 255), round(
        accentColorDarkLightBlue * 255)
except ValueError:
    accentColorDarkLight = accentColorLight

accentBorderColorRed, accentBorderColorGreen, accentBorderColorBlue = lighten_color('#%02x%02x%02x' % accentColor, .15)
accentBorderColor = round(accentBorderColorRed * 255), round(accentBorderColorGreen * 255), round(
    accentBorderColorBlue * 255)

colorName = closest_colour(mainColor)
accentName = closest_colour(accentColor).title()
dirName = colorName
dirName += "/textures/ui/"
print("\nCreating", colorName.title(), "UI with", accentName, "accents\n")

ui = [f for f in os.listdir("assets/ui") if os.path.isfile(os.path.join("assets/ui", f))]
colors = ["198, 198, 198", mainColor,
          "0, 0, 0", borderColor]
for i in range(len(ui)):
    fileName = "assets/ui/"
    fileName += ui[i]
    im = Image.open(fileName)
    im = im.convert('RGBA')
    data = np.array(im)
    red, green, blue, alpha = data.T

    # Replace replaceToRed, Green, Blue with replaceWith...
    j = 0
    while j < len(colors):
        replaceTo = eval(colors[j])
        replaceToRed, replaceToBlue, replaceToGreen = replaceTo
        replaceWith = colors[j + 1]

        color = (red == replaceToRed) & (blue == replaceToBlue) & (green == replaceToGreen)
        data[..., :-1][color.T] = replaceWith

        j += 2

    try:
        os.makedirs(dirName)
    except Exception:
        pass
    fileName = fileName.replace("assets/ui/", dirName)
    Image.fromarray(data).save(fileName)
    print(fileName)

ac = accentColor
acd = accentColorDark
acdl = accentColorDarkLight
acl = accentColorLight
abc = accentBorderColor

button_borderless_darkhover = [ac, ac, ac, acdl, ac, acdl, acdl, acd, ac, acdl, acdl, acd, acdl, acd, acd, acd]
button_borderless_darkpressed = [acd, acd, acd, acdl, acd, acdl, acdl, ac, acd, acdl, acdl, ac, acdl, ac, ac, ac]
button_borderless_lighthover = [acl, acl, acl, ac, acl, ac, ac, acd, acl, ac, ac, acd, ac, acd, acd, acd]
button_borderless_lightpressed = [acd, acd, acd, ac, acd, ac, ac, acl, acd, ac, ac, acl, ac, acl, acl, acl]
slider_button_hover = [abc, abc, abc, abc, abc, abc, abc, acl, acl, acl, ac, abc, abc, acl, ac, ac, acd, abc, abc, acl,
                       ac, ac, acd, abc, abc, ac, acd, acd, acd, abc, abc, abc, abc, abc, abc, abc]
slider_progress_hover = [ac, ac, ac, ac, ac, ac, ac, ac, ac]
slider_step_background_hover = [acd, acd, acd, acd, acd, acd, acd, acd, acd]
slider_step_progress_hover = [acd, acd, acd, acd, acd, acd, acd, acd, acd]
toggle_off_hover = [abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, abc, acl, acl, acl, acl, acl, acl, acl, ac, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, abc, abc, abc, abc, abc, abc, abc,
                    abc, abc, abc, abc, abc, abc, abc, abc, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc,
                    acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc,
                    acl, ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd,
                    acd, acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd,
                    acdl, acdl, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac,
                    ac, ac, acd, abc, acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc,
                    0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd, acdl, acdl, acd, acd,
                    acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, acd,
                    acd, acd, acd, acdl, acdl, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc, acl,
                    ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd, acd, acd, acd,
                    acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd, acdl,
                    acdl, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac,
                    ac, acd, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0,
                    0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd,
                    acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, abc, abc, abc,
                    abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, 0, 0, 0, 0, abc, ac, acd, acd, acd,
                    acd, acd, acd, acd, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, abc, abc, abc,
                    abc, abc, abc, abc, abc, abc, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
toggle_on_hover = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, abc, abc, abc, abc, abc, abc, abc, abc,
                   abc, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, abc, acl, acl, acl, acl, acl,
                   acl, acl, ac, abc, 0, 0, 0, 0, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc,
                   abc, abc, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd, acd,
                   acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0,
                   abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, acl, ac, ac, ac,
                   ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acdl, acdl, acd,
                   acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd,
                   acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0,
                   0, 0, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd, abc, acl, ac,
                   ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acdl,
                   acdl, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd,
                   acd, acd, acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd,
                   abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd, acd, acd, acd, acd, acdl, acdl, acd, acd, acd, acd,
                   abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd, acd, acd, acd, acd, acd, acd, acd,
                   acd, acd, acd, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, abc, acd,
                   acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, acd, abc, acl, ac, ac, ac, ac, ac,
                   ac, acd, abc, 0, 0, 0, 0, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc,
                   abc, abc, acl, ac, ac, ac, ac, ac, ac, acd, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, abc, ac, acd, acd, acd, acd, acd, acd, acd, abc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, abc, abc, abc, abc, abc, abc, abc, abc, abc, abc]

button = [button_borderless_darkhover, button_borderless_darkpressed, button_borderless_lighthover,
          button_borderless_lightpressed, slider_button_hover, slider_progress_hover, slider_step_background_hover,
          slider_step_progress_hover, toggle_off_hover, toggle_on_hover]
buttonName = ["button_borderless_darkhover.png", "button_borderless_darkpressed.png",
              "button_borderless_lighthover.png", "button_borderless_lightpressed.png", "slider_button_hover.png",
              "slider_progress_hover.png", "slider_step_background_hover.png", "slider_step_progress_hover.png",
              "toggle_off_hover.png", "toggle_on_hover.png"]

for i in range(len(button)):
    fileName = "assets/button/"
    fileName += buttonName[i]
    im = Image.open(fileName)
    width, height = im.size
    arr = button[i]

    curr = 0
    for j in range(height):
        for k in range(width):
            replaceLoc = (k, j)
            replaceWith = arr[curr]
            if replaceWith != 0:
                im = pix(im, replaceLoc, replaceWith)
            curr += 1

    fileName = fileName.replace("assets/button/", dirName)
    im.save(fileName)
    print(fileName)

dst = (colorName
       + '/manifest.json')
name = (colorName.title()
        + ' UI')
desc = (colorName.title()
        + ' with '
        + accentName
        + ' accents, auto-generated by Theme Engine')
with open("assets/manifest.json", 'r') as original, open(dst, 'w') as new:
    for line in original:
        new.write(line.replace("415", str(desc)).replace("417", name).replace("488", str(uuid.uuid4())).replace("489", str(uuid.uuid4())))
    new.close()

# TODO : Create pack_icon
icon = (colorName
       + '/pack_icon.png')
Image.open("assets/pack_icon.png").save(icon)

# FIXME : Unhide following to create zip
# TODO : Possibly rename extenstion to .mpack
# shutil.make_archive(colorName, 'zip', colorName)
# shutil.rmtree(dirName)
print('\nSuccessfully compressed', colorName, '. zip')
