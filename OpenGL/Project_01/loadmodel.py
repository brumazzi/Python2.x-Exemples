import os
import OpenGL
import PIL
import re

from OpenGL.GL import *
from PIL import Image as image

class PyModel():
	__slots__ = 'mname','vx','vy','vz','nx','ny','nz','u','v','x','y','z','scale','image','faces','vertex','imTex'

	def __init__(self):
		self.image = ""
		self.mname = ""
		self.vx = []
		self.vy = []
		self.vz = []
		self.nx = []
		self.ny = []
		self.nz = []
		self.u = []
		self.v = []
		self.x = 0
		self.y = 0
		self.z = 0
		self.scale = 6
		self.faces = 0
		self.vertex = 0
		self.imTex = False

	def load(self,fName):
		try:
			f = open(fName+".brzz","r")
		except:
			print('Arquivo n\xc3\xa3o encontrado.')
			return 0

		f.seek(0)
		fline = re.split(r'[ \n]',f.readline())
		if fline[0] != '!OGLModel' or fline[1] != 'BRZZ':
			print('N\xc3\xa3o foi possivel ler o arquivo', f.name + '.')
			return 0
	
		fline = re.split(r'[ \n]',f.readline())
		if fline[0] != 'Model_Name:':
			print("Erro ao ler o arquivo.")
			return 0
		for i in range(2,len(fline[1])-2):
			self.mname += fline[1][i]

		fline = re.split(r'[ \n]',f.readline())
		if fline[0] != 'Total_Vertex:':
			print("Erro ao ler o arquivo.")
			return 0
		self.vertex = int(fline[1])

		fline = re.split(r'[ \n]',f.readline())
		if fline[0] != 'Total_Faces:':
			print("Erro ao ler o arquivo.")
			return 0
		self.faces = int(fline[1])

		for i in range(0,self.vertex):
			fline = re.split(r'[ \n]',f.readline())
   
			if fline[0] != '&':
				print("N\xc3\xa3o foi possivel fazer a leitura dos verteces.")
				return 0
			elif fline[0] == '$':
				break
			else:
				if len(fline) < 8:
					print("Erro ao ler os vertices.")
					print(len(fline))
					return 0
				self.vx.append(float(fline[1]))
				self.vy.append(float(fline[2]))
				self.vz.append(float(fline[3]))
				self.nx.append(float(fline[4]))
				self.ny.append(float(fline[5]))
				self.nz.append(float(fline[6]))
				self.u.append(float(fline[7]))
				self.v.append(float(fline[8]))

		return 1

	def texture(self,iname):
		self.image = str(iname)

	def loadTexture(self):
		try:
			f = open(self.image)
			im = image.open(self.image)
			img = [0]
		except:
			print('Arquvivo n\xc3\xa3o encontrado ou invalido!')
			return None
		s = ""
		for i in range(0,4):
			s += f.read(1)
		if s != '\x89PNG':
			print('Formato de imagem n\xc3\xa3o suportado!\nApenas arquivo \"PNG\".')
			return None

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
		self.imTex = True
		return img

	def drawQuads(self):
		try:
			import tex
			img = self.loadTexture()
			glBindTexture(GL_TEXTURE_2D,img[0])

		except:
			print('Falha ao carregar textura.')

		glBegin(GL_QUADS)
		glColor3f(1,1,1)

		try:
			for i in range(0,self.vertex):
				glNormal3f(self.nx[i],self.ny[i],self.nz[i])
				glTexCoord2f(self.u[i],self.v[i])			
				glVertex3f(self.scale*self.vx[i] + self.x,self.scale*self.vy[i] + self.y,self.scale*self.vz[i] + self.z)
				#print self.nx[i],self,ny[i],self.nz[i]
		except:
			print('Erro ao iniciar a leitura dos verteces.')
		glEnd()

	def drawTriangles(self):
		try:
			if self.imTex:
				glBindTexture(GL_TEXTURE_2D,self.image[0])
		except:
			print('Falha ao carregar textura.')

		glBegin(GL_TRIANGLES)
		glColor3f(1,1,1)

		try:
			for i in range(0,self.vertex):
				glTexVoord2f(self.u[i],self.v[i])
				glNormal3f(self.nx[i],self.ny[i],self,nz[i])
				glVertex3f(self.scale*self.vx[i] + self.x,self.scale*self.vy[i] + self.y,self.scale*self.vz[i] + self.z)
		except:
			print('Erro ao iniciar a leitura dos verteces.')
		glEnd()

