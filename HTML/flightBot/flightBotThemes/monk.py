from os import makedirs

def run(name, back, root, text, airln, aArr, cArr):
    if airln:
        airln = 'airln'
    else:
        airln = 'color'
    htm = '<div id="choice" class="' + airln + '" style="background-color: #303030;" ><a style="color: #f5f5f5;" onclick="choice(\'default\')">default</a></div> \n'
    if airln == 'airln':
        add(aArr, htm.replace("303030", back).replace("f5f5f5", text).replace("default", name))
    else:
        add(cArr, htm.replace("303030", back).replace("f5f5f5", text).replace("default", name))
    # textDark = "#" + color_variant("#" + text, -20)
    name = "themes\\" + name + ".css"
    with open("default.css") as f:
        with open(name, "w") as f1:
            for line in f:
                f1.write(line.replace("303030", root).replace("1a1a1a", back).replace("f5f5f5", text))


def color_variant(hex_color, brightness_offset=1):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])


def add(arr, line):
    index = 0
    while index < len(arr):
        if compareTo(cut(line), cut(arr[index])) > 0:
            index += 1
        else:
            break
    arr.insert(index, line)


def compareTo(self, that):
    return (self > that) - (self < that)


def cut(line):
    return line[line.index('choice(\'') + 8:line.index('\')">')]


makedirs('themes/')

cArr = []
aArr = []
Arr = ['default.css']

run("monkey", "323437", "2c2e31", "e2b714", False, aArr, cArr)
run("lavender", "786e96", "ada6c2", "e4e3e9", False, aArr, cArr)
run("vscode", "1e1e1e", "191919", "007acc", False, aArr, cArr)
run("charm", "1b3238", "1c292f", "6bde3b", False, aArr, cArr)
run("eclipse", "0e0506", "1a0b0c", "ff3a32", False, aArr, cArr)
run("aal", "dfe4e8", "cad1d7", "eb2023", True, aArr, cArr)
run("astral", "0a1928", "030613", "4fcdb9", False, aArr, cArr)
run("berry", "f37f83", "bd4f56", "fcfcf8", False, aArr, cArr)
run("dal", "003268", "001934", "df0e39", True, aArr, cArr)
run("jbu", "b4d2ee", "6ba6dd", "152c40", True, aArr, cArr)
run("aca", "c8dee1", "8dc1c9", "b9082c", True, aArr, cArr)

file = open("text.txt", "w")
for item in range(len(cArr)):
    file.write(cArr[item])
    Arr.append(cut(cArr[item]) + '.css')
for item in range(len(aArr)):
    file.write(aArr[item])
    Arr.append(cut(aArr[item]) + '.css')
file.close()

print(Arr)
