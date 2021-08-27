from PIL import Image

name=input("Image name: ")
WaveImage = Image.open(name, 'r')
WaveIm = WaveImage.load()

width, height = WaveImage.size

print(width,height)

recordR = open("recordR.txt", 'w')
recordG = open("recordG.txt", 'w')
recordB = open("recordB.txt", 'w')

for y in range(height):
    for x in range(width):
        if ".png" in name:
            r, g, b, xx = WaveIm[x,y]
        else:
            r, g, b = WaveIm[x,y]

        print("[",x,",",y,"]",": {",r,",",g,",",b,"}"," of  [",width,",",height,"]")
        
        recordR.write(str(r))
        recordR.write("\n")
        recordG.write(str(g))
        recordG.write("\n")
        recordB.write(str(b))
        recordB.write("\n")

recordR.close()
recordG.close()
recordB.close()
