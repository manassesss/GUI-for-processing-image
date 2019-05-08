import numpy as np
import cv2
from cv2 import imread, morphologyEx
import matplotlib
import matplotlib.pyplot as plt
from skimage.morphology import erosion, dilation, opening, closing

im = imread('screenshots/anne.jpg', 0)
#e = erosion(im)
#e = dilation (im)
#e = opening (im)
kernel = np.array(([0,1,0],[1,-1,1],[0,1,0]), dtype="int")
e = morphologyEx(im, cv2.MORPH_HITMISS, kernel)
e = im + e
plt.imshow(e, cmap='gray')
plt.show()