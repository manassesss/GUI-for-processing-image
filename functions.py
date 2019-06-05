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
'''
im_g = cv2.GaussianBlur(im, (3,3),0)
kX = np.array([[1,1,1,],[0,0,0],[-1,-1,-1]])
kY = np.array([[-1,0,1,],[-1,0,1],[-1,0,1]])
im_pX = cv2.filter2D(im_g, -1, kX)
im_pY = cv2.filter2D(im_g, -1, kY)
im_p = im_pX + im_pY
'''
'''
img = im.copy()
i, j = 0, 0
while i < h-1:
    while j < w-1:
        img[i][j] = im[i][j+1] + im[i][j-1] + im[i+1][j] +im[i-1][j] + (-8*(im[i][j]))
        j = j+1
    i = i+1
'''
h, w = im.shape[0], im.shape[1]
print (h, w)
print (im)
'''
wdth, hght = w/1.5, h/1.5
resized = image.resize((int(wdth), int(hght)), Image.ANTIALIAS) #tentativa de ajustar o tamanho da imagem, entretanto não funciona para JPEG
photo = ImageTk.PhotoImage(resized)
ima = Label(frameLeft, image=photo, background='gray7')
ima.place(x= 0, y=0, width=900, height=600)
'''
'''
#im = cv2.Laplacian(im, cv2.CV_64F)
plt.imshow(im, cmap='gray')

plt.show()'''