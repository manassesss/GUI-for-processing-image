from tkinter import *
from tkinter import filedialog, Frame, Canvas
import cv2
from PIL import ImageTk, Image
from skimage import color, filters, io, data, exposure, util
import matplotlib
import matplotlib.pyplot as plt 


window = Tk()
window.filename = filedialog.askopenfilename(initialdir = "/", title= "Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
f = Frame(window, height=400, width=400)
f.pack_propagate(0)
f.place(x=0, y=0)
img = ImageTk.PhotoImage(Image.open(window.filename))
label = Label(f, image = img)
label.pack(fill=Y, expand = 0)

window.mainloop()