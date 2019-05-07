def openFile () :
	global im
	janela.filename = filedialog.askopenfilename(initialdir = "/", title= "Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
	#print(janela.filename)
	im = io.imread(janela.filename)
	plt.imshow(im)
	plt.show()

def saveFile() :
	global im
	# = filedialog.asksaveasfilename(initialfile='Unfield.jpg', defaultextension=".jpg", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
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