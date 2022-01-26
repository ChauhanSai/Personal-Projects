from PIL import Image
import numpy as np

ui = ["", ""]
colors = {"x": ""}
replaces = [""]

for i in range(len(ui)):
    im = Image.open('test.png')
    im = im.convert('RGBA')
    data = np.array(im)
    red, green, blue, alpha = data.T

    # Replace replaceRed, Green, Blue with replaces... (leaves alpha values alone...)
    for j in range(len):
        replace = eval(colors[j])
        replaceRed, replaceBlue, replaceGreen = replace
        color = (red == replaceRed) & (blue == replaceBlue) & (green == replaceGreen)
        data[..., :-1][color.T] = (eval(replaces[j]))

    im2 = Image.fromarray(data)
    im2.show()