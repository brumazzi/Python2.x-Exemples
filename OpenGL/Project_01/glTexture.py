import os
import sys
import ctypes
from ctypes import *

#libTexture = None

#if os.path.isfile('./SDLTexture.so') == False:
#	print('Arquivo "SDLTexture.so" n\xc3\xa3o encontrado!')
#	sys.exit()
#else:
#	libTexture = cdll.LoadLibrary("./SDLTexture.so")
	
def loadTexture(iname):
	if not os.path.isfile(iname):
		print('Arquivo n\xc3\xa3o existente.')
		return 0
	f = open(iname,'r')
	format = f.read(1)
	format += f.read(1)
	format += f.read(1)
	if format != 'BMF':
		print("Arquivo n\xc3\xa3o valido")
		return 0
	Tex = None# = libTexture.loadTexture(str(iname))
	return Tex
