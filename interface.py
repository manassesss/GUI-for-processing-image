from tkinter import *
from tkinter import filedialog, Frame, Canvas
import cv2
from PIL import ImageTk, Image
from skimage import color, filters, io, data, exposure, util, feature
from skimage.morphology import dilation, opening, closing, erosion, square
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

janela = Tk()
janela.title("iEditor")
#L x A + ME + MT
janela.geometry("1200x600+200+100")
janela.configure(background='gray20')
frameRight = Frame(janela,width=250, height=700, background='gray20')
frameRight.pack(side=RIGHT)
frameLeft = Frame(janela,width=950, height=700, background='gray7')
frameLeft.pack(side=LEFT)

# FUNÇÕES IMPLEMENTADAS 

def showImage (master, image, imx, *args, **kwargs) :
	h, w = imx.size[1], imx.size[0] 
	wdth, hght = w/1.5, h/1.5
	resized = image.resize((int(wdth), int(hght)), Image.ANTIALIAS) #tentativa de ajustar o tamanho da imagem, entretanto não funciona para JPEG
	photo = ImageTk.PhotoImage(resized)
	ima = Label(frameLeft, image=photo, background='gray7')
	ima.place(x= 0, y=0, width=900, height=600)
	

def openFile () :
	global im
	janela.filename = filedialog.askopenfilename(initialdir = "/", title= "Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
	im = io.imread(janela.filename)
	img = Image.open(janela.filename)
	
	image = Image.open(janela.filename)
	h, w = img.size[1], img.size[0] 
	print(h, w)
	wdth, hght = w/1.5, h/1.5
	resized = image.resize((int(wdth), int(hght)), Image.ANTIALIAS) #tentativa de ajustar o tamanho da imagem, entretanto não funciona para JPEG
	photo = ImageTk.PhotoImage(resized)
	ima = Label(frameLeft, image=photo, background='gray7')
	ima.place(x= 0, y=0, width=900, height=600)
	
	#showImage(janela, img, img)
	
	plt.imshow(im)
	plt.show()

def saveFile() :
	global im
	im2 = filedialog.asksaveasfilename(initialfile='Unfield.jpg', defaultextension=".jpg", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
	cv2.imwrite("imagedm.jpg", im)

def gamma() :
  global im
  indicator = Label(frameRight, text='Gamma: ', padx=12)
  entry_indicator = Entry(frameRight)
  indicator.grid(row=0, column=0)
  entry_indicator.grid(row=0, column=1)
  apply = Button(frameRight, text='Apply', padx=12)
  apply.grid(row=0, column=2)
  
  gamma = exposure.adjust_gamma(im, 0.4)

  plt.imshow(gamma, cmap='gray')
  plt.show()
  im = gamma

def logaritmic () :
	global im
	log = exposure.adjust_log(im, 2)
	plt.imshow(log, cmap='gray')
	plt.show()
	im = log

def inverter() :
	global im
	invert = util.invert(im)
	plt.imshow(invert, cmap=plt.cm.gray)
	plt.show()
	im = invert

def showHistogram () :
	global im
	im = color.rgb2gray(im)
	hist, hist_center = exposure.histogram(im)
	fig, axe = plt.subplots(ncols=2, figsize=(10,6))
	axe[0].plot(hist_center, hist, lw=2)
	axe[0].set_title("Histograma")
	axe[1].imshow(im, cmap='gray')
	axe[1].set_title("Imagem")
	plt.show()

def equalizeHistogram () :
	global im
	im_eq = exposure.equalize_hist(im)
	hist, hist_center = exposure.histogram(im_eq)
	fig, axes = plt.subplots(ncols=2, figsize=(10,6))
	axes[0].plot(hist_center, hist, lw=2)
	axes[0].set_title("Histograma Equalizado")
	axes[1].imshow(im_eq, cmap='gray')
	axes[1].set_title("Imagem Equalizado")
	plt.show()
	im = im_eq

def medianFilter() :
	global im
	square = 5
	med = cv2.medianBlur(im, square)
	plt.imshow(med, cmap="gray")
	plt.show()
	im = med

def averageFilter() : 
	global im
	blur = cv2.blur(im, (10,10))
	plt.imshow(blur, cmap="gray")
	plt.show()
	im = blur

def laplacianFilter():
	global im
	lap = cv2.Laplacian(im, -1)
	lap = im+lap
	plt.imshow(lap, cmap='gray')
	plt.show()
	im = lap

def colorHSV() :
	global im
	hsv = color.rgb2hsv(im)
	hsv = hsv[:, :, 2]
	plt.imshow(hsv)
	plt.show()
	im = hsv

def colorGray() :
	global im
	gray = color.rgb2gray(im)
	plt.imshow(gray, cmap='gray')
	plt.show()
	im = gray

def colorHSI() :
	global im
	hsi = cv2.cvtColor(im, COLOR_RGB2HLS)
	plt.imshow(hsi)
	plt.show()

def morphErosion():
	global im
	e = color.rgb2gray(im)
	e = erosion(e, square(5))
	plt.imshow(e, cmap='gray')
	plt.show()

def morphDilation():
	global im
	e = color.rgb2gray(im)
	e = dilation(e, square(5))
	plt.imshow(e, cmap='gray')
	plt.show()

def morphOpening():
	global im
	e = color.rgb2gray(im)
	e = opening(e, square(5))
	plt.imshow(e, cmap='gray')
	plt.show()

def morphClosing():
	global im
	e = color.rgb2gray(im)
	e = closing(e, square(5))
	plt.imshow(e, cmap='gray')
	plt.show()

def noiseGaussian ():
	global im
	row,col,ch= im.shape
	mean = 0
	var = 0.1
	sigma = var**0.5
	gauss = np.random.normal(mean,sigma,(row,col,ch))
	gauss = gauss.reshape(row,col,ch)
	noisy = im + gauss
	plt.imshow(noisy)
	plt.show()

def noiseSaltAndPepper():
	global im
	row,col,ch= im.shape
	s_vs_p = 0.9
	amount = 0.04
	out = np.copy(im)
	# Salt mode
	num_salt = np.ceil(amount * im.size * s_vs_p)
	coords = [np.random.randint(0, i - 1, int(num_salt))for i in im.shape]
	out[coords] = 1
	# Pepper mode
	num_pepper = np.ceil(amount* im.size * (1. - s_vs_p))
	coords = [np.random.randint(0, i - 1, int(num_pepper))for i in im.shape]
	out[coords] = 0
	plt.imshow(out)
	plt.show()

def segCanny():
	global im
	im = color.rgb2gray(im)
	im = feature.canny(im, 3)
	plt.imshow(im, cmap='gray')
	plt.show()

def segPrewitty() :
	global im
	im = color.rgb2gray(im)
	im_g = cv2.GaussianBlur(im, (3,3),0)
	kX = np.array([[1,1,1,],[0,0,0],[-1,-1,-1]])
	kY = np.array([[-1,0,1,],[-1,0,1],[-1,0,1]])
	im_pX = cv2.filter2D(im_g, -1, kX)
	im_pY = cv2.filter2D(im_g, -1, kY)
	im_p = im_pX + im_pY
	plt.imshow(im_p, cmap='gray')
	plt.show()



# ESTRUTURA DA INTERFACE
menubar = Menu(janela)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir arquivo", command = openFile)
filemenu.add_command(label="Salvar arquivo", command=saveFile)
filemenu.add_separator()
#filemenu.add_command(label="Exit")
highlightmenu = Menu(menubar, tearoff=0)
highlightmenu.add_command(label="Gamma", command= gamma)
highlightmenu.add_command(label="Logaritmico", command=logaritmic)
highlightmenu.add_command(label="Inverter", command=inverter)
histogrammenu = Menu(menubar, tearoff=0)
histogrammenu.add_command(label="Exibir histograma", command=showHistogram)
histogrammenu.add_command(label="Equalizar histograma", command=equalizeHistogram)
modelscormenu = Menu(menubar, tearoff=0)
modelscormenu.add_command(label="Transformar HSV", command=colorHSV)
#modelscormenu.add_command(label="Transformar HSI", command=colorHSI)
modelscormenu.add_command(label="Transformar Preto e Branco", command=colorGray)
#modelscormenu.add_command(label="Exibir canais de cor")
filtersspacial = Menu(menubar, tearoff=0)
filtersspacial.add_command(label="Mediana", command=medianFilter)
filtersspacial.add_command(label="Media", command=averageFilter)
#filtersspacial.add_command(label="Media ponderada")
filtersspacial.add_command(label="Laplaciano", command=laplacianFilter)
morphologymenu = Menu(menubar, tearoff=0)
morphologymenu.add_command(label='Erosão', command=morphErosion)
morphologymenu.add_command(label='Dilatação', command=morphDilation)
morphologymenu.add_command(label='Abertura', command=morphOpening)
morphologymenu.add_command(label='Fechamento', command=morphClosing)
noisymenu = Menu(menubar, tearoff=0)
noisymenu.add_command(label="Sal e Pimenta", command=noiseSaltAndPepper)
menubar.add_cascade(label="Arquivo", menu=filemenu)
menubar.add_cascade(label="Realces", menu=highlightmenu)
menubar.add_cascade(label="Histograma", menu=histogrammenu)
menubar.add_cascade(label="Modelos de Cor", menu=modelscormenu)
menubar.add_cascade(label="Filtros Espaciais", menu=filtersspacial)
menubar.add_cascade(label="Morfologia", menu=morphologymenu)
menubar.add_cascade(label="Ruidos", menu=noisymenu)


janela.config(menu=menubar)




janela.mainloop()
