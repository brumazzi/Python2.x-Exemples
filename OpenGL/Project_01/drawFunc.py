import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import loadmodel as lm

import tex

import ctypes
from ctypes import cdll

import time

try:
	lib = cdll.LoadLibrary("./cam.so")
except:
	print "lib not found."

m = lm.PyModel()
m.load('data/models/cube')
m.texture('data/images/caixa.png')

def initFunc(x,y):
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,800/600,.1,500)

	glClearColor(0.545098039,0.741176471,0.925490196,.0)
	glPointSize(10.0)
	glMatrixMode(GL_MODELVIEW)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glEnable(GL_TEXTURE_2D)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

	ambLight = [.1,.1,.1,.1]
	diffuse = [.6,.6,.6,1]
	specular = [.7,.7,.3,1]
	lPosition = [.2,.2,2.0]

	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambLight)
	glLightfv(GL_LIGHT0,GL_DIFFUSE,diffuse)
	glLightfv(GL_LIGHT0,GL_SPECULAR,specular)
	glLightfv(GL_LIGHT0,GL_POSITION,lPosition)

	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	glShadeModel(GL_SMOOTH)
	glLightModeli(GL_LIGHT_MODEL_TWO_SIDE,GL_FALSE)
	glDepthFunc(GL_LEQUAL)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

#	gluPerspective(40,x/y,.1,500.0)
	#gluOrtho2D(.0,x,.0,y)
	gluLookAt(0,2,4,0,0,0,0,1,0)
	
starttime = time.time()

def rotation( period = 10):
	"""Do rotation of the scene at given rate"""
	angle = ((time.time()-starttime)%(period)/period)* 360
	glRotate( angle, 0,1,0)
	print time.time(),starttime,'\n',time.time()-starttime
	return angle

def displayFunc(swap=1,clear=1):
	glClearColor(0.5, 0.5, 0.5, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# establish the projection matrix (perspective)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(
		45, # field of view in degrees
		glutGet(GLUT_WINDOW_WIDTH)/float(glutGet(GLUT_WINDOW_HEIGHT) or 1), # aspect ratio
		1, # near clipping plane
		30000, # far clipping plane
	)
	# and then the model view matrix
	glRotate(1,0,1,0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(
		0,0,5, # eyepoint
		0,0,0, # center-of-view
		0,1,0, # up-vector
	)
	rotation()
	img = tex.loadTexture("data/images/caixa.png")
	glBindTexture(GL_TEXTURE_2D,img[0])
	m.drawQuads()
	
	glBegin(GL_QUADS)
	glColor3f(1,1,1)
	glNormal3f(1,1,1)
	glTexCoord2f(0.0,0.0)
	glVertex3f(-1.0,1.0,.0)
	glTexCoord2f(0.0,1.0)
	glVertex3f(-1.0,-1.0,.0)
	glTexCoord2f(1.0,1.0)
	glNormal3f(0,0,0)
	glVertex3f(1.0,-1.0,.0)
	glTexCoord2f(1.0,0.0)
	glVertex3f(1.0,1.0,.0)
	glEnd()
	
#	glFlush()
#	if swap:
	glutSwapBuffers()
#	os.system("sleep 0.5")

