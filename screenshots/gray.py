import cv2
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
from skimage import io, data, filters, color

im = cv2.imread('anne.jpg', 0)
#grey = color.rgb2grey(im)
io.imshow(im)
io.show()