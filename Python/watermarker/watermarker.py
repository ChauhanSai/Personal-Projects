from PIL import Image
  
def resize(file):
    image = Image.open(file)
    width, height = image.size
    if height > 1080:
        width = (width*1080)//height
        height = 1080
        image = image.resize((width, height))
    return(image)

def watermark(image, ext, fileName):
    overlayDef = {'svg1': 'svgOverlay1.png', 'png1': 'pngOverlay1.png', 'svg2': 'svgOverlay2.png', 'png2': 'pngOverlay2.png', 'svg3': 'svgOverlay3.png', 'png3': 'pngOverlay3.png', }
    fileName+='.png'
    width, height = image.size
    amountWidth = width//500
    amountHeight = height//500
    firstPlacementX = (width-(amountWidth*500))//amountWidth//2
    firstPlacementY = (height-(amountHeight*500))//amountHeight//2
    spacingX = 500+(width-(amountWidth*500))//amountWidth
    spacingY = 500+(height-(amountHeight*500))//amountHeight

    overlay = Image.open(overlayDef[ext])
    
    if amountWidth > 1:
        if amountHeight > 1:
            for j in range(0, amountHeight):
                for i in range(0,amountWidth):
                    if (i+j)%2 == 1:
                        image.paste(overlay, (firstPlacementX+spacingX*i, firstPlacementY+spacingY*j), overlay)
        else:  
            for i in range(0,amountWidth):
                if i%2 == 1:
                    image.paste(overlay, (firstPlacementX+spacingX*i, firstPlacementY+spacingY*i), overlay)
    else:
        image.paste(overlay, (firstPlacementX, firstPlacementY), overlay)

    image.save(fileName)

if __name__ == '__main__':
    watermark(resize())
