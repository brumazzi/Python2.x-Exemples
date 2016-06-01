import sys
import OpenGL
from OpenGL.GLU import gluLookAt

def keyboard(*key):
	print key
	if key[0] == '\x1b':
		sys.exit()
	if key[0] == '\r':
		gluLookAt(0,0,1,0,0,0,1,1,1)
