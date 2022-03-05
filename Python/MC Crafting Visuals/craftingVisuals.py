from json import load
from math import ceil
from os.path import exists, isfile, join
from PIL import Image, ImageOps
from os import listdir

replace = {}
recipesDir = "recipes"
recipes = [f for f in listdir(recipesDir) if isfile(join(recipesDir, f))]
for recipe in range(len(recipes)):
    craft = 'recipes/' + recipes[recipe]
    print("Reading " + recipes[recipe])
    # Clean file of comments
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

    try:
        name = data["minecraft:recipe_shapeless"]["description"]["identifier"]
        craftType = 1  # Shapeless
    except KeyError:
        name = data["minecraft:recipe_shaped"]["description"]["identifier"]
        craftType = 0  # Shaped

    # Create file
    name = name[name.index(':') + 1:] + ".png"
    Image.open('ui.png').save(name)
    image = Image.open(name)


    def place(texture, loc):
        """
        Creates a repeating event Tuesdays at 5-6pm starting after exclude
        ex. debate(upcomingMeeting)
        :param texture: file name
        :type texture: basestring
        :param loc: grid location, 9 for result
        :type loc: int
        """
        grid = ["74, 74", "222, 74", "372, 74",
                "74, 222", "222, 222", "372, 222",
                "74, 372", "222, 372", "372, 372",
                "848, 214"]
        paste = Image.open("textures/" + texture)
        width, height = paste.size
        if width != height:
            resize = ceil((height - width) / 2)
            paste = ImageOps.expand(paste, resize, (0, 0, 0, 0))
            paste = paste.crop((0, resize, height, height + resize))
        if loc == 9:
            newSize = eval("133, 133")
        else:
            newSize = eval("117, 117")
        paste = paste.resize(newSize, Image.NEAREST)
        image.paste(paste, eval(grid[loc]), paste)


    if craftType:
        # Shapeless
        arr = []
        # Get ingredients in order
        for i in range(len(data["minecraft:recipe_shapeless"]["ingredients"])):
            item = data["minecraft:recipe_shapeless"]["ingredients"][i]['item']
            item = item[item.index(':') + 1:]
            if exists("textures\\" + item + ".png"):
                arr.append(item + ".png")
            else:
                try:
                    arr.append(replace[item])
                    print("Retrieved "+replace[item])
                except KeyError:
                    temp = input(item + " not found, enter alternative: ") + ".png"
                    arr.append(temp)
                    replace[item] = temp
        # Get result
        result = data["minecraft:recipe_shapeless"]["result"][0]["item"]
        result = result[result.index(':') + 1:]
        if exists("textures\\" + result + ".png"):
            arr.append(result + ".png")
        else:
            try:
                arr.append(replace[item])
                print("Retrieved "+replace[item])
            except KeyError:
                temp = input(item + " not found, enter alternative: ") + ".png"
                arr.append(temp)
                replace[item] = temp

    else:
        # Shaped
        # Get item with key
        items = {}
        for i in range(len(data["minecraft:recipe_shaped"]["key"])):
            char = list(data["minecraft:recipe_shaped"]["key"].keys())[i]
            item = data["minecraft:recipe_shaped"]["key"][char]["item"]
            item = item[item.index(':') + 1:]
            if exists("textures\\" + item + ".png"):
                items[char] = item + ".png"
            else:
                try:
                    items[char] = replace[item]
                    print("Retrieved "+replace[item])
                except KeyError:
                    temp = input(item + " not found, enter alternative: ") + ".png"
                    items[char] = temp
                    replace[item] = temp
        # Place items in pattern order
        arr = []
        for i in range(len(data["minecraft:recipe_shaped"]["pattern"])):
            string = data["minecraft:recipe_shaped"]["pattern"][i]
            for j in range(len(string)):
                arr.append(items[string[j:j + 1]])
        # Get result
        result = data["minecraft:recipe_shaped"]["result"][0]["item"]
        result = result[result.index(':') + 1:]
        if exists("textures\\" + result + ".png"):
            arr.append(result + ".png")
        else:
            try:
                arr.append(replace[item])
                print("Retrieved "+replace[item])
            except KeyError:
                temp = input(item + " not found, enter alternative: ") + ".png"
                arr.append(temp)
                replace[item] = temp

    # Create image
    for i in range(len(arr) - 1):
        place(arr[i], i)
    place(arr[len(arr) - 1], 9)
    image.save(name)
    print("Saved " + name + "\n")
