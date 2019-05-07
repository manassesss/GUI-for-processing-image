import cv2
import matplotlib
import matplotlib.pyplot as plt
from skimage import color

im = cv2.imread("moonNaza2.jpg")
#raio = input("Raio: ")
#print(raio)
im = color.rgb2gray(im)
plt.imshow(im, cmap="gray")
plt.show()
blur = cv2.Laplacian(im, -1000)
blur = im + blur
plt.imshow(blur, cmap="gray")
plt.show()