import math
import os
from PIL import Image, ImageOps

if not path.exists('textures/'):
    makedirs('textures/')

input("Directory created, please add textures and press ENTER to begin")

textureDir = "textures"
ui = [f for f in os.listdir(textureDir) if os.path.isfile(os.path.join(textureDir, f))]
amount = math.ceil(math.sqrt(len(ui)))
dim = amount * 135
Matrix = [[0 for x in range(amount)] for y in range(amount)]

back = Image.new('RGBA', (dim, dim), (15, 15, 15, 255))
image = back.load()

margin = 135 - 128

i = 0
for r in range(amount):
    for c in range(amount):
        try:
            Matrix[r][c] = ui[i]
            file = (textureDir + '/' + ui[i])
            paste = Image.open(file)
            width, height = paste.size
            if width != height:
                resize = math.ceil((height-width)/2)
                paste = ImageOps.expand(paste, resize, (0, 0, 0, 0))
                paste = paste.crop((0, resize, height, height+resize))
            paste = paste.resize(eval("128, 128"), Image.NEAREST)
            back.paste(paste, (c * 128 + 2 * margin, r * 128 + 2 * margin), paste)
        except IndexError:
            pass
        i += 1

back.save("matrix.png")
