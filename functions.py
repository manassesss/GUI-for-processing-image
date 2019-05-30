import numpy as np 
from skimage import io, color, feature
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
import matplotlib.pyplot as plt
import math

filename  = 'anne5.jpg'
im = io.imread(filename)
#imPIL = Image.open(filename)

h, w, c = im.shape
im = color.rgb2gray(im)
#im = feature.canny(im, 3)

im_g = cv2.GaussianBlur(im, (3,3),0)
kX = np.array([[1,1,1,],[0,0,0],[-1,-1,-1]])
kY = np.array([[-1,0,1,],[-1,0,1],[-1,0,1]])
im_pX = cv2.filter2D(im_g, -1, kX)
im_pY = cv2.filter2D(im_g, -1, kY)
im_p = im_pX + im_pY


plt.imshow(im_p, cmap='gray')

plt.show()


