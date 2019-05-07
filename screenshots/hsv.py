import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from skimage import io, data, filters, color

im = io.imread("anne.jpg")
hsi = cv2.cvtColor(im, COLOR_BGR2HLS)
grey = color.rgb2grey(im)


fig, axes = plt.subplots(nrows=3, figsize=(10,10))
axes[0].imshow(im)
axes[0].set_title("RGB scale")
axes[1].imshow(hsv, cmap='hsv')
axes[1].set_title("HSV scale")
axes[2].imshow(grey, cmap='gray')
axes[2].set_title("GRAY Scale")

plt.show()