import os
import OpenGL
import PIL
import re

from OpenGL.GL import *
from PIL import Image as image

class _basicModel():
	__slots__ = 'mname','vx','vy','vz','nx','ny','nz','u','v','x','y','z','scale','image','faces','vertex','face_points','vertex_face','direction'

	def __init__(self):
		self.mname = ''
		self._config()

	def _config(self):
		self.vx = []
		self.vy = []
		self.vz = []
		self.nx = []
		self.ny = []
		self.nz = []
		self.u = []
		self.v = []
		self.x = .0
		self.y = .0
		self.z = .0
		self.scale = 1.0
		self.image = None
		self.faces = 0
		self.vertex = 0
		self.face_points = []
		self.vertex_face = []
		self.r = []
		self.g = []
		self.b = []
		self.direction = .0

	def texture(self,iname):
		self.image = 'data/textures/'+str(iname)+'.png'

	def _texture(self):
		try:
			f = open(self.image)
			im = image.open(self.image)
			img = [0]
		except:
			return None
		s = ""
		for i in range(0,4):
			s += f.read(1)
		if s != '\x89PNG':
			return None

		tdata = im.tostring('raw','RGBX',0,-1)
		#exit()
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

class Ply(_basicModel):
	
	def load(self,fname):
		self._config()
		try:
			f = open('data/models/ply/'+fname+'.ply','r')
		except:
			print('Arquivo n\xc3\xa3o encontrado.')
			return 0

		f.seek(0)

		lines = 0
		while(True):
			l = f.readline()
			if l == '':
				break
			else:
				lines += 1

		f.seek(0)
		for i in range(0,lines):
			fline = re.split(r'[ \n]',f.readline())
			if fline[0] == 'ply':
				x=0
			elif fline[0] == 'format':
				if fline[1] == 'ascci':
					x=0
			elif fline[0] == 'comment':
				x = 0
			elif fline[0] == 'element':
				if fline[1] == 'vertex':
					self.vertex = int(fline[2])
				elif fline[1] == 'face':
					self.faces = int(fline[2])
			elif fline[0] == 'property':
				x = 0
			elif fline[0] == 'end_header':
				break

		for i in range(0,self.vertex):
			fline = re.split(r'[ \n]',f.readline())

			if (len(fline)-1) == 8:
				self.vx.append(float(fline[0]))
				self.vy.append(float(fline[1]))
				self.vz.append(float(fline[2]))
				self.nx.append(float(fline[3]))
				self.ny.append(float(fline[4]))
				self.nz.append(float(fline[5]))
				self.u.append(float(fline[6]))
				self.v.append(float(fline[7]))
			elif (len(fline)-1) == 11:
				self.vx.append(float(fline[0]))
				self.vy.append(float(fline[1]))
				self.vz.append(float(fline[2]))
				self.nx.append(float(fline[3]))
				self.ny.append(float(fline[4]))
				self.nz.append(float(fline[5]))
				self.u.append(float(fline[6]))
				self.v.append(float(fline[7]))
				self.r.append(float(fline[8])/255)
				self.g.append(float(fline[9])/255)
				self.b.append(float(fline[10])/255)
			elif (len(fline)-1) == 6:
				self.vx.append(float(fline[0]))
				self.vy.append(float(fline[1]))
				self.vz.append(float(fline[2]))
				self.nx.append(float(fline[3]))
				self.ny.append(float(fline[4]))
				self.nz.append(float(fline[5]))
			elif (len(fline)-1) == 9:
				self.vx.append(float(fline[0]))
				self.vy.append(float(fline[1]))
				self.vz.append(float(fline[2]))
				self.nx.append(float(fline[3]))
				self.ny.append(float(fline[4]))
				self.nz.append(float(fline[5]))
				self.r.append(float(fline[6])/255)
				self.g.append(float(fline[7])/255)
				self.b.append(float(fline[8])/255)
			else:
				return 0

		for i in range(0,self.faces):
			self.face_points.append([])
			self.vertex_face.append([])

		for i in range(0,self.faces):
			fline = re.split(r'[ \n]',f.readline())

			if fline[0] == '3':
				self.vertex_face[i] = int(fline[0])
				self.face_points[i] = (int(fline[1]),int(fline[2]),int(fline[3]))

			if fline[0] == '4':
				self.vertex_face[i] = int(fline[0])
				self.face_points[i] = (int(fline[1]),int(fline[2]),int(fline[3]),int(fline[4]))

			if fline[0] == '5':
				self.vertex_face[i] = int(fline[0])
				self.face_points[i] = (int(fline[1]),int(fline[2]),int(fline[3]),int(fline[4]),int(fline[5]))

		return 1

	def draw(self):
		try:
			img = self._texture()
			glBindTexture(GL_TEXTURE_2D,img[0])
		except:
			a=0

		for i in range(0,int(self.faces)):
			fc = self.vertex_face[i]

			if fc == 3:
				glBegin(GL_TRIANGLES)
				x,y,z = self.face_points[i]
			elif fc == 4:
				glBegin(GL_QUADS)
				x,y,z,w = self.face_points[i]
			elif fc == 5:
				glBegin(GL_POLYGON)
				x,y,z,w,k = self.face_points[i]
			else:
				break

			try: glTexCoord2f(self.u[x],self.v[x])
			except:
				a=0
			try: glColor3f(self.r[x],self.g[x],self.b[x])
			except:
				a=0
			glNormal3f(self.nx[x],self.ny[x],self.nz[x])
			glVertex3f(self.vx[x]*self.scale+self.x,self.vy[x]*self.scale+self.y,self.vz[x]*self.scale+self.z)

			try: glTexCoord2f(self.u[y],self.v[y])
			except:
				a=0
			try: glColor3f(self.r[y],self.g[y],self.b[y])
			except:
				a=0
			glNormal3f(self.nx[y],self.ny[y],self.nz[y])
			glVertex3f(self.vx[y]*self.scale+self.x,self.vy[y]*self.scale+self.y,self.vz[y]*self.scale+self.z)

			try: glTexCoord2f(self.u[z],self.v[z])
			except:
				a=0
			try: glColor3f(self.r[z],self.g[z],self.b[z])
			except:
				a=0
			glNormal3f(self.nx[z],self.ny[z],self.nz[z])
			glVertex3f(self.vx[z]*self.scale+self.x,self.vy[z]*self.scale+self.y,self.vz[z]*self.scale+self.z)

			if fc > 3:
				try: glTexCoord2f(self.u[w],self.v[w])
				except:
					a=0
				try: glColor3f(self.r[w],self.g[w],self.b[w])
				except:
					a=0
				glNormal3f(self.nx[w],self.ny[w],self.nz[w])
				glVertex3f(self.vx[w]*self.scale+self.x,self.vy[w]*self.scale+self.y,self.vz[w]*self.scale+self.z)
				if fc > 4:
					try: glTexCoord2f(self.u[k],self.v[k])
					except:
						a=0
					try: glColor3f(self.r[k],self.g[k],self.b[k])
					except:
						a=0
					glNormal3f(self.nx[k],self.ny[k],self.nz[k])
					glVertex3f(self.vx[k]*self.scale+self.x,self.vy[k]*self.scale+self.y,self.vz[k]*self.scale+self.z)
				
			glEnd()

class Obj(_basicModel):

	def load(self,fname,ani):
		self._config()
		self.material = []
		mtl = ''
		#self.material.append('')
		self.face_normal = []
		self.face_uv = []
		fc = 0
		matLib = None
		try:
			if ani == False:
				f = open('data/models/obj/'+fname+'.obj')
			else:
				f = open(fname)
		except:
			return 0

		while(True):
			fline = re.split(r'[ / \n]',f.readline())

			if fline[0] == 'mtllib':
				try:
					matLib = open('data/models/obj/'+fline[1]+'.mtl')
				except:
					a=0
			elif fline[0] == 'o':
				self.mname = fline[1]
			elif fline[0] == 'v':
				self.vx.append(float(fline[1]))
				self.vy.append(float(fline[2]))
				self.vz.append(float(fline[3]))
				self.vertex += 1
			elif fline[0] == 'vn':
				self.nx.append(float(fline[1]))
				self.ny.append(float(fline[2]))
				self.nz.append(float(fline[3]))
			elif fline[0] == 'vt':
				self.u.append(float(fline[1]))
				self.v.append(float(fline[2]))
			elif fline[0] == 'usemtl':
				mtl == fline[1]
			elif fline[0] == 's':
				a=0
			elif fline[0] == 'f':
				self.material = mtl
				if len(fline) == 14:
					self.vertex_face.append(4)
					self.face_points.append((int(fline[1]),int(fline[4]),int(fline[7]),int(fline[10])))
					self.face_uv.append((int(fline[2]),int(fline[5]),int(fline[8]),int(fline[11])))
					self.face_normal.append((int(fline[3]),int(fline[6]),int(fline[9]),int(fline[12])))
				elif len(fline) == 11:
					self.vertex_face.append(3)
					self.face_points.append((int(fline[1]),int(fline[4]),int(fline[7])))
					self.face_uv.append((int(fline[2]),int(fline[5]),int(fline[8])))
					self.face_normal.append((int(fline[3]),int(fline[6]),int(fline[9])))
				fc += 1

			elif fline[0] == '':
				break
			elif fline[0] == '#':
				a = 0
			else:
				return 0
		self.faces = fc
		return 1
	
	
	def draw(self):
		try:
			img = self._texture()
			glBindTexture(GL_TEXTURE_2D,img[0])
		except:
			a = 0

		for i in range(0,self.faces):
			if self.vertex_face[i] == 4:
				x,y,z,w = self.face_points[i]
				try: ux,uy,uz,uw = self.face_uv[i]
				except: a=0
				try: nx,ny,nz,nw = self.face_normal[i]
				except: a=0
				glBegin(GL_QUADS)
			elif self.vertex_face[i] == 3:
				x,y,z = self.face_points[i]
				try: ux,uy,uz = self.face_uv[i]
				except: a=0
				try: nx,ny,nz = self.face_normal[i]
				except: a=0
				glBegin(GL_TRIANGLES)

			try: glTexCoord(self.u[ux-1],self.v[ux-1])
			except: a=0
			try: glNormal3f(self.nx[nx-1],self.ny[nx-1],self.nz[nx-1])
			except: a=0
			glVertex3f(self.vx[x-1]*self.scale+self.x,self.vy[x-1]*self.scale+self.y,self.vz[x-1]*self.scale+self.z)

			try: glTexCoord(self.u[uy-1],self.v[uy-1])
			except: a=0
			try: glNormal3f(self.nx[ny-1],self.ny[ny-1],self.nz[ny-1])
			except: a=0
			glVertex3f(self.vx[y-1]*self.scale+self.x,self.vy[y-1]*self.scale+self.y,self.vz[y-1]*self.scale+self.z)

			try: glTexCoord(self.u[uz-1],self.v[uz-1])
			except: a=0
			try: glNormal3f(self.nx[nz-1],self.ny[nz-1],self.nz[nz-1])
			except: a=0
			glVertex3f(self.vx[z-1]*self.scale+self.x,self.vy[z-1]*self.scale+self.y,self.vz[z-1]*self.scale+self.z)

			try:
				try: glTexCoord(self.u[uw-1],self.v[uw-1])
				except: a=0
				try: glNormal3f(self.nx[nw-1],self.ny[nw-1],self.nz[nw-1])
				except: a=0
				glVertex3f(self.vx[w-1]*self.scale+self.x,self.vy[w-1]*self.scale+self.y,self.vz[w-1]*self.scale+self.z)
			except: a=0

			try:
				glEnd()
			except:
				break

class ObjAnimat():

	__slots__ = 'ani_start','ani_end','total_frames','_object','frame'

	def __init__(self):
		import os
		self._config()

	def _config(self):
		self.ani_start = 0
		self_ani_end = 0
		self.total_frames = 0
		self._obj = []
		self.isfile = os.path.isfile
		self.char = []
		self.frame_name = []
		self.frame = []
		self.start = 0
		self.end = 0
		self.point = 0
		self.animat = False

		for i in range(6):
			self.char.append(0)

	def count_frames(self,fname):
		self._config()
		self.char[5] = 1
		f = ''
		while(True):
			f = 'data/models/obj_ani/'+fname+'/'+fname+'_'+str(self.char[0])+str(self.char[1])+str(self.char[2])+str(self.char[3])+str(self.char[4])+str(self.char[5])+'.obj'
			if self.isfile(f):
				self.frame_name.append(f)
				self.total_frames += 1
				self.frame.append(open(f,'r'))
			else:
				break
			self.char[5] += 1
			if self.char[5] > 9:
				self.char[4] += 1
				self.char[5] = 0
			if self.char[4] > 9:
				self.char[3] += 1
				self.char[4] = 0
			if self.char[3] > 9:
				self.char[2] += 1
				self.char[3] = 0
			if self.char[2] > 9:
				self.char[1] += 1
				self.char[2] = 0
			if self.char[1] > 9:
				self.char[0] += 1
				self.char[1] = 0
			if self.char[0] > 9:
				return 0
		return 1

	def draw(self,start,end):
		self.start = start
		self.end = end

		if self.animat == False:
			self._obj[self.start-1].draw()
		#else:
		#	for i in range(start,end):
		#		self._obj[i].draw()

	def animate(self,start,end,loop):
		if self.animat == False:
			self.animat = True
			if self.point < start or self.point >= end:
				self.point = start
				if loop == False:
					self.animat = False
			else:
				self.point += 1
			self._obj[self.point-1].draw()

	def texture(self,iname):
		for i in range(self.total_frames):
			self._obj[i].texture(iname)


	def load(self,fname):
		fc = []
		fline = None
		self.count_frames(fname)
		for i in range(self.total_frames):
			self._obj.append(Obj())
			self._obj[i].load(self.frame_name[i],True)

