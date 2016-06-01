import sys

try:
	import wx
	from wx.glcanvas import *
except:
	print('Biblioteca \"wx\" n\xc3\xa3o encontrada.')
	sys.exit()

try:
	import OpenGL
	from OpenGL.GL import *
	from OpenGL.GLU import *
except:
	print('Biblioteca \"OpenGL\" n\xc3\xa3o encontrada.')
	sys.exit()

import cam
import loadmodel as lm

class _glCanvas(GLCanvas):

	def __init__(self, parent, attribs = None, id = wx.ID_ANY):
		if not attribs:
			attribs = [WX_GL_RGBA, WX_GL_DOUBLEBUFFER, WX_GL_DEPTH_SIZE, 20]
		GLCanvas.__init__(self, parent, id, attribList = attribs)
		self.init = False
		self.w = 0
		self.h = 0
		self.dist = 500
		self.menu = True
		self.pause = False
		self.fs = True

		self.timer = wx.Timer(self)
		self._events()
		self.timer.Start(1000.0/60.0)

		self.x = 0
		self.m = lm.Ply()
		#self.o = lm.Obj()
		self.n = lm.ObjAnimat()
		self.n.load('ico_open')
		#self.n.animate(1,60,True)
		#self.m.load('model')
		##self.o.load('cube',False)
		self.n.texture('roxo')
		#self.o.texture('madeira')
		#self.m.texture('parede_01')
		self.n.scale = .2

	def _distance(self,dist):
		self.dist = dist

	def _events(self):
		self.Bind(wx.EVT_PAINT, self._paint)
		self.Bind(wx.EVT_SIZE,self._size)
		self.Bind(wx.EVT_TIMER,self._refresh)
		self.Bind(wx.EVT_KEY_UP,self._keyUp)
		self.Bind(wx.EVT_KEY_DOWN,self._keyDown)

	def _paint(self,evt):
		dc = wx.PaintDC(self)
		self.SetCurrent()
		if not self.init:
			self.initGL()
		if self.menu == True:
			self._menu()
		self._projection()

	def _size(self,evt):
		self.w,self.h = self.GetSizeTuple()

	def _keyUp(self,evt):
		if evt.GetKeyCode() == wx.WXK_F11:
			self.fs = not self.fs
			self.GetParent().GetParent().ShowFullScreen(self.fs)

	def _keyDown(self,evt):
		key = evt.GetKeyCode()
		if key == wx.WXK_UP:
			print('[KEY UP PRESS]')
			cam.z += .1
		elif key == wx.WXK_DOWN:
			cam.z -= .1

		elif key == wx.WXK_ESCAPE and self.pause == True:
			self.menu = False
			self.pause = False
		elif key == wx.WXK_ESCAPE:
			self.GetParent().GetParent().Close()

		elif key == wx.WXK_F1:
			cam.vs += .5
		elif key == wx.WXK_F2:
			cam.vs -= .5

	def _refresh(self,evt):
		self.Refresh()

	def initGL(self):
		glClearColor(0.0,0.0,0.0,1.0)
		self.init = True
		self._light()

	def _projection(self):
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glViewport(0,0,self.w,self.h)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(cam.vs+0,float(self.w)/float(self.h),1.0,1000)#int(self.dist))
		glMatrixMode(GL_MODELVIEW)
		glShadeModel(GL_SMOOTH);

		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LEQUAL)

		glLoadIdentity()
		gluLookAt(cam.yx,cam.yy,cam.yz,cam.x,cam.y,cam.z,cam.rx,cam.ry,cam.rz)

		self._draw()

	def _draw(self):
		glRotate(self.x,0,0,1)

#		glBegin(GL_QUADS)
#		glTexCoord2f(0,0)
#		glNormal3f(1,1,1)
#		glVertex3f(0,0,0)
#		glTexCoord2f(1,0)
#		glVertex3f(1,0,0)
#		glNormal3f(0,0,0)
#		glTexCoord2f(1,1)
#		glVertex3f(1,1,0)
#		glTexCoord2f(0,1)
#		glVertex3f(0,1,0)
#		glEnd()

		self.n.animate(1,60,True)
		self.x += 1

		#self.n.draw(5,60)

#		self.m.draw()
		#self.o.draw()
		#self.o.x += 0.2
		self.SwapBuffers()

	def _menu(self):
		x = 0 

	def _showMenu(self):
		self.menu = True
		self.pause = True
		self._menu

	def _light(self):
		self.ambLight = .1,.1,.1,1
		self.diffuse = .6,.6,.6,1
		self.specular = .7,.7,.3,1
		self.lightPosition = 0,0,0

		glLightModelfv(GL_LIGHT_MODEL_AMBIENT,self.ambLight)
		glLightfv(GL_LIGHT0,GL_DIFFUSE,self.diffuse)
		glLightfv(GL_LIGHT0,GL_SPECULAR,self.specular)

		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_TEXTURE_2D)
		glLightModeli(GL_LIGHT_MODEL_TWO_SIDE,GL_TRUE)
		glShadeModel(GL_SMOOTH)

class GameFrame(wx.Frame):

	def __init__(self,*argv,**kw):
#		kw["style"] = wx.NO_BORDER
		super(GameFrame,self).__init__(*argv,**kw)

		self.pnl = wx.Panel(self)
		self.canvas = _glCanvas(self.pnl)
		self.cur = wx.StockCursor(wx.CURSOR_CROSS)

		self.Size = (800,600)
		self.w ,self.h = self.Size

		self.canvas.SetFocus()

		self.Bind(wx.EVT_SIZE,self._resize)

		self.ShowFullScreen(True)

#		self.canvas.Show(False)

		self.canvas.SetCursor(self.cur)

	def _resize(self,evt):
		self.pnl.Position = (0,0)
		self.pnl.Size = (self.Size[0]+1,self.Size[1]+1)
		self.canvas.Position = (0,0)
		self.canvas.Size = (self.pnl.Size[0]+1 ,self.pnl.Size[1]+1)
		

class App(wx.App):

	def OnInit(self):
		self.frame = GameFrame(None,title = "GL_Game")
		self.frame.Size = (800,600)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

