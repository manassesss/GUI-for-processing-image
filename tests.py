from tkinter import *
from tkinter import filedialog, Frame, Canvas
from PIL import Image, ImageTk
from cv2 import imread
import scipy
janela = Tk()
janela.title("iEditor")
#L x A + ME + MT
janela.geometry("1200x600+200+100")
janela.configure(background='gray20')

frameRight = Frame(janela, width=250, height=700, background='gray20')
frameRight.pack(side=RIGHT)
frameLeft = Frame(janela,width=950, height=700, background='gray7')
frameLeft.pack(side=LEFT)

indicator = Label(frameRight, text='Gamma: ', padx=12)
entry_indicator = Entry(frameRight)
indicator.grid(row=0, column=0)
entry_indicator.grid(row=0, column=1)
apply = Button(frameRight, text='Apply', padx=12)
apply.grid(row=0, column=2)
'''
filename = filedialog.askopenfilename(initialdir = "/", title= "Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
print(filename)
'''
image = Image.open('anne5.jpg')
im = imread('anne5.jpg')
'''
altura = 500
a_perc = (altura/float(im.shape[1]))
wsize = int(float(im.shape[0]*float(a_perc)))
'''
h, w = im.shape[0], im.shape[1]
wdth, hght = w/1.5, h/1.5

resized = image.resize((int(wdth), int(hght)), Image.ANTIALIAS) #tentativa de ajustar o tamanho da imagem, entretanto não funciona para JPEG
photo = ImageTk.PhotoImage(resized)
im = Label(frameLeft, image=photo, background='gray7')
im.place(x= 0, y=0, width=1000, height=600)



menubar = Menu(janela)
filemenu = Menu(menubar, tearoff=0)
highlightmenu = Menu(menubar, tearoff=0)
histogrammenu = Menu(menubar, tearoff=0)
modelscormenu = Menu(menubar, tearoff=0)
filtersspacial = Menu(menubar, tearoff=0)
morphologymenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=filemenu)
menubar.add_cascade(label="Realces", menu=highlightmenu)
menubar.add_cascade(label="Histograma", menu=histogrammenu)
menubar.add_cascade(label="Modelos de Cor", menu=modelscormenu)
menubar.add_cascade(label="Filtros Espaciais", menu=filtersspacial)
menubar.add_cascade(label="Morfologia", menu=morphologymenu)
janela.config(menu=menubar)
janela.mainloop()



'''
kernel = np.array(([0,1,0],[1,-1,1],[0,1,0]), dtype="int")
e = morphologyEx(im, cv2.MORPH_HITMISS, kernel)
e = im + e
'''