#!/usr/bin/env python

import sys

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class MainWindow:
	__slots__ = 'w','h','x','y','fScreen','title'

	def __init__(self):
		glutInit()
		self.w = 640
		self.h = 480
		self.x = 0
		self.y = 0
		self.title = ""
		self.fScreen = True

	def setSize(self,width,height):
		self.w = width
		self.h = height
		glutInitWindowSize(self.w,self.h)

	def setPosition(self,px,py):
		self.x = px
		self.y = py

	def setTitle(self,text):
		self.title = text
	
	def show(self):
		glutCreateWindow(self.title)
		glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
		
def keyboard(*key):
	if key[0] == "\x1b":
		sys.exit()

def initFunc():
	glClearColor(1.0,1.0,1.0,.0)
	glPointSize(10.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(.0,800,.0,600)

def displayFunc():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	glColor3f(.0,.0,.0)
	glVertex2i(100,50)
	glColor3f(1,0,0)
	glVertex2i(100,130)
	glColor3f(0,1,0)
	glVertex2i(150,130)
	glEnd()
	glFlush()

win = MainWindow()

if __name__ == '__main__':
	win.setSize(800,600)
	win.setTitle("Main OpenGL on Python")
	win.show()
	glutDisplayFunc(displayFunc)
	glutKeyboardFunc(keyboard)
	#glutIdleFunc(displayFunc)
	initFunc()
	glutMainLoop()
	
