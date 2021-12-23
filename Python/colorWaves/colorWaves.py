print('Initializing...')
print('Please Wait')

import sys
import numpy as np
import skimage.color
import skimage.io
from matplotlib import pyplot as plt
from tkinter import *
from PIL import Image
import os

window = Tk()
window.title("Color Waves")
try:
    window.iconbitmap('colorWaves.ico')
except Exception:
    pass

mainFrame = Frame(master=window, width=150, height=150)
mainFrame.pack(padx=5, pady=5)

inputFrame = Frame(master=mainFrame, width=150, height=150)
inputFrame.pack()
inputEntry = Entry(master=inputFrame, width=100)
inputEntry.pack(side=RIGHT)
inputEntry.insert(0, "C:")
inputLabel = Label(master=inputFrame, text="Directory", width=10, anchor="e")
inputLabel.pack(side=RIGHT)

def colorWaves():
    window.update()
    src = inputEntry.get()
    fileName= src[src.rindex('\\')+1:src.rindex('.')]
    window.update()
    
    try:
        nameDir = fileName
        nameDir+= '/'
        os.makedirs(nameDir)
        nameTemp = nameDir
        nameTemp+= 'temp.png'
        nameGrayscale = nameDir
        nameGrayscale+= 'histogramGrayscale.txt'
        nameGrayscaleImage = nameDir
        nameGrayscaleImage+= 'histogramGrayscale.png'
        nameColor = nameDir
        nameColor+= 'histogramColor.txt'
        nameColorImage = nameDir
        nameColorImage+= 'histogramColor.png'
        print('Directory Creation Successful')

        rnm= 'temp.png'
        Image.open(src).save(nameTemp)
        print('Temporary File Creation Successful')
    except Exception:
        print("Error Creating Files: Please remove '", nameDir, "' Directory")
        inputEntry.delete(0, END)
        return None
    window.update()

    # Read Grayscale Image
    image = skimage.io.imread(fname=nameTemp, as_gray=True)
    window.update()
    
    # Create Grayscale Histogram
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    grayscale = open(nameGrayscale, 'w')
    grayscale.write(str(histogram))
    grayscale.write('\n')
    grayscale.write(str(bin_edges))
    grayscale.write('\n\n')
    grayscale.close()
    print('Grayscale Histogram Successful')
    window.update()

    # Draw Grayscale Histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Value")
    plt.ylabel("Pixels")
    plt.xlim([0.0, 1.0])
    plt.plot(bin_edges[0:-1], histogram)
    plt.savefig(nameGrayscaleImage)
    print('Grayscale Plot Successful')
    window.update()

    grayscaleWindow = Toplevel()
    grayscaleWindow.title('Grayscale Histogram')
    try:
        grayscaleWindow.iconbitmap('colorWaves.ico')
    except Exception:
        pass
    grayscaleCanvas = Canvas(grayscaleWindow, width = 640, height = 480)
    grayscaleCanvas.pack(expand = YES, fill = BOTH)
    grayscaleIm = PhotoImage(file = nameGrayscaleImage)
    grayscaleCanvas.create_image(0, 0, image = grayscaleIm, anchor = NW)
    grayscaleCanvas.grayscaleIm = grayscaleIm
    window.update()

    # Read Image
    image = skimage.io.imread(fname=nameTemp)
    window.update()

    # Create Histogram
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)
    plt.figure()
    plt.title("Color Histogram")
    plt.xlim([0, 256])
    color = open(nameColor, 'w')
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=256, range=(0, 256)
        )
        color.write(str(histogram))
        color.write('\n')
        color.write(str(bin_edges))
        color.write('\n\n')
        plt.plot(bin_edges[0:-1], histogram, color=c)
    color.close()
    print('Color Histogram Successful')
    window.update()

    plt.xlabel("Value")
    plt.ylabel("Pixels")
    plt.savefig(nameColorImage)
    print('Color Plot Successful')
    window.update()

    colorWindow = Toplevel()
    colorWindow.title('Color Histogram')
    try:
        colorWindow.iconbitmap('colorWaves.ico')
    except Exception:
        pass
    colorCanvas = Canvas(colorWindow, width = 640, height = 480)
    colorCanvas.pack(expand = YES, fill = BOTH)
    colorIm = PhotoImage(file = nameColorImage)
    colorCanvas.create_image(0, 0, image = colorIm, anchor = NW)
    colorCanvas.colorIm = colorIm
    window.update()

    os.remove(nameTemp)

buttonFrame = Frame(master=mainFrame, width=150, height=150)
buttonFrame.pack()
try:
    startButton = Button(master=buttonFrame, text="Start", width=40, height=2, command=colorWaves)
    startButton.pack(padx=5, pady=5)
except Exception:
    pass
creditLabel = Label(master=buttonFrame, text="Created By ChauhanSai on GitHub", width=40)
creditLabel.pack()

window.mainloop()
