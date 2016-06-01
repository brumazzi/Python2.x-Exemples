import PIL
from PIL import Image

def openImage(fname):
	im = Image.open(fname)
	#im.rotate(45).show() #Rotaciona 45°

	im.thumbnail((268,268),Image.ANTIALIAS) # redimensiona a imagem
	im.save("Imagem Modificada","JPEG") #Salva com o formato JPEG
