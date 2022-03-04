from json import load
from math import ceil
from os.path import exists
from PIL import Image, ImageOps

# Clean file of comments
craft = 'drink_carrot_thick.json'
file = open(craft, 'r')
lines = file.readlines()
file = open(craft, 'w')
for line in lines:
    if '//' not in line.strip("\n"):
        file.write(line)
    else:
        file.write(line[:line.index('//')] + '\n')

# Load JSON
file = open(craft)
data = load(file)

# Create file
Image.open('ui.png').save("file.png")
image = Image.open('file.png')


def place(file, loc):
    # TODO: Grid coordinates for location
    grid = ["", "", "",
            "", "", "",
            "", "", "",
            ""]
    paste = Image.open("textures\\" + file)
    width, height = paste.size
    if width != height:
        resize = ceil((height - width) / 2)
        paste = ImageOps.expand(paste, resize, (0, 0, 0, 0))
        paste = paste.crop((0, resize, height, height + resize))
    paste = paste.resize(eval("128, 128"), Image.NEAREST)
    image.paste(paste, grid[loc], paste)


try:
    # Shapeless
    name = data["minecraft:recipe_shapeless"]["description"]["identifier"]
    arr = []
    for i in range(len(data["minecraft:recipe_shapeless"]["ingredients"])):
        item = data["minecraft:recipe_shapeless"]["ingredients"][i]['item']
        item = item[item.index(':') + 1:]
        if exists("textures\\" + item + ".png"):
            arr.append(item + ".png")
        else:
            arr.append(input(item + " not found, enter alternative: ") + ".png")
    print(arr)
    # TODO: Place arr files at grid i
    for i in range(len(arr)):
        place(arr[i], i)
    # TODO: Rename file.png to identifier

except KeyError:
    # Shaped
    # TODO: Shaped recipes
    print(data["minecraft:recipe_shaped"])
