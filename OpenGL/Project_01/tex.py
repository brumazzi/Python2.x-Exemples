import PIL
from PIL import Image as image
import OpenGL
from OpenGL.GL import *

def loadTexture(iname):
		try:
			f = open(iname)
			im = image.open(iname)
		except:
			print('Arquvivo n\xc3\xa3o encontrado ou invalido!')
			return None
		s = ""
		for i in range(0,4):
			s += f.read(1)
		if s != '\x89PNG':
			print('Formato de imagem n\xc3\xa3o suportado!\nApenas arquivo \"PNG\".')
			return None

		img = [0]
		tdata = im.tostring('raw','RGBX',0,-1)
		glGenTextures(1,img)
		glBindTexture(GL_TEXTURE_2D, img[0])
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
		glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,im.size[0],im.size[1],0,GL_RGBA,GL_UNSIGNED_BYTE, tdata)
		glEnable(GL_TEXTURE_2D)
		return img
