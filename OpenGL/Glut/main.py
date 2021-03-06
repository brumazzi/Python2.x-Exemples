#!/usr/bin/env python

try:
	import OpenGL
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print 'OpenGL not found'

x = 1
y = 1

def ini():
	glMatrixMode(GL_PROJECTION)
	glViewport(0,0,800,600)
	glLoadIdentity()
	gluPerspective(40,800/600,.5,500.0)
	glMatrixMode(GL_MODELVIEW)
	glClearDepth(1.0)
	glEnable(GL_DEPTH_TEST)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

	glClearColor(.0,.0,.0,1.0)
#	gluLookAt(x,y,5,0,0,0,0,1,0)


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	gluLookAt(2,2,5,0,0,0,0,0,0)

	r = 0
	

	glBegin(GL_QUADS)
	glNormal3f(1,1,1)
	glVertex3f(1,1,0)
	glVertex3f(1,0,0)
	glNormal3f(0,0,0)
	glVertex3f(0,0,0)
	glVertex3f(0,1,0)

	glEnd()

	glutSwapBuffers()

#if __name__ == '__main__':
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(800,600)
glutCreateWindow("Primari Frame")
ini()
glutDisplayFunc(display)

glutMainLoop()	
