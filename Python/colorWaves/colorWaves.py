print('Please wait')

import sys
import numpy as np
import skimage.color
import skimage.io
from matplotlib import pyplot as plt

name = input('File name: ')

# Read Grayscale Image
image = skimage.io.imread(fname=name, as_gray=True)

# Create Grayscale Histogram
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
grayscale = open('histogramGrayscale.txt', 'w')
grayscale.write(str(histogram))
grayscale.write('\n')
grayscale.write(str(bin_edges))
grayscale.write('\n\n')
grayscale.close()
print('Grayscale Histogram Successful')

# Draw Grayscale Histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Value")
plt.ylabel("Pixels")
plt.xlim([0.0, 1.0])

plt.plot(bin_edges[0:-1], histogram)
plt.savefig('histogramGrayscale.png')

# Read Image
image = skimage.io.imread(fname=name)

# Create Histogram
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)
plt.figure()
plt.title("Color Histogram")
plt.xlim([0, 256])
color = open('histogramColor.txt', 'w')
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
plt.xlabel("Value")
plt.ylabel("Pixels")
plt.savefig('histogramColor.png')
print('Color Histogram Successful')
