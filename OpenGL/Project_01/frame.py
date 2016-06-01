try:
	import OpenGL
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print('OpenGL not found!')
	import sys
	sys.exit()

import sys

import keyFunc
import drawFunc
from keyFunc import *
from drawFunc import *

class GLWindow:
	__slots__ = 'w','h','x','y','title','mode3D','fScreen'

	def __init__(self):
		self.w = 640
		self.h = 480
		self.x = 0
		self.y = 0
		self. title = ""
		self.mode3D = False
		self.fScreen = True

	def setTitle(self,text):
		self.title = text

	def setSize(self,width,height):
		self.w = width
		self.h = height

	def setPosition(self,px,py):
		self.x = px
		self.y =py

	def show(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
		glutInitWindowSize(self.w,self.h)
		glutInitWindowPosition(self.x,self.y)
		glutCreateWindow(self.title)
#		initFunc(self.w,self.h)
		glutDisplayFunc(displayFunc)
		glutIdleFunc(displayFunc)
		glutKeyboardFunc(keyboard)

		glutMainLoop()
