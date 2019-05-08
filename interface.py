from tkinter import *
from tkinter import filedialog, Frame, Canvas
import cv2
from PIL import ImageTk, Image
from skimage import color, filters, io, data, exposure, util
from skimage.morphology import dilation, opening, closing, erosion
import matplotlib
import matplotlib.pyplot as plt 

janela = Tk()
janela.title("iEditor")
#L x A + ME + MT
janela.geometry("1000x600+200+100")
janela.configure(background='#404238')

# FUNÇÕES IMPLEMENTADAS 

def showImage (master, *args, **kwargs) :
	image = PhotoImage(file = master.filename)
	label = Label(master, image = image)
	label.pack()
	#return label

def openFile () :
	global im
	janela.filename = filedialog.askopenfilename(initialdir = "/", title= "Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
	#showImage(janela)

	im=io.imread(janela.filename)
	plt.imshow(im)
	plt.show()

def saveFile() :
	global im
	im2 = filedialog.asksaveasfilename(initialfile='Unfield.jpg', defaultextension=".jpg", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
	cv2.imwrite("imagedm.jpg", im)

def gamma() :
  global im
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
	e = erosion(e)
	plt.imshow(e, cmap='gray')
	plt.show()

def morphDilation():
	global im
	e = dilation(im)
	plt.imshow(e, cmap='gray')
	plt.show()

def morphOpening():
	global im
	e = opening(im)
	plt.imshow(e, cmap='gray')
	plt.show()

def morphClosing():
	global im
	e = closing(im)
	plt.imshow(e, cmap='gray')
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
menubar.add_cascade(label="Arquivo", menu=filemenu)
menubar.add_cascade(label="Realces", menu=highlightmenu)
menubar.add_cascade(label="Histograma", menu=histogrammenu)
menubar.add_cascade(label="Modelos de Cor", menu=modelscormenu)
menubar.add_cascade(label="Filtros Espaciais", menu=filtersspacial)
menubar.add_cascade(label="Morfologia", menu=morphologymenu)


janela.config(menu=menubar)

janela.mainloop()
