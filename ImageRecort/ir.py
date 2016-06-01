import sys
import PIL
from PIL import Image as image

def recImage(fIn,fOut,resol,x,y,w,h):
	try:
		img = image.open(fIn)
	except:
		return "Arquivo invalido."

	itype = 'JPEG'

	img = img.crop((x,y,w+x,h+y))
	
	try:
		img.save(fOut,itype,quality = int(resol))
	except:
		return 'Erro ao salvar a imagem'

	return "Imagem salva!"

def resize(w,h,img):
	img = image.open(img)

	img.thumbnail((w,h),image.ANTIALIAS)

	img.sava(img,'JPEG',quality = 255)
