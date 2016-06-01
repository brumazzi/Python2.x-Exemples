import sys, os

import Xlib
from Xlib.display import Display

class WinData:

	def __init__(self, dname = "data.cfg"):
		display = Display(':0').screen().root.get_geometry()
		self.width = 0
		self.height = 0
		self.x = 0
		self.y = 0
		self.fullscreen = True
		self.display = "0x0"
		self.oldisplay = str(str(display.width)+"x"+str(display.height))
		self.dataName = dname

	def setGeometry(self,w,h,x,y):
		self.width = w
		self.height = h
		self.x = x
		self.y = y

	def setDisplay(self,width,height):
		self.display = str(width) + "x" + str(heigh)

	def save(self):
		fs = 1
		file = open(self.dataName,"w")
		file.write("\x01####GENERAL#GAME#CONFIG####\x01\n")
		file.write("win_dimension %i %i\n" %(self.width,self.height))
		file.write("win_position %i %i\n" %(self.x,self.y))
		if self.fullscreen == True:
			fs = 1
		else:
			fs = 0
		file.write("win_fullscreen %i\n" %(fs))
		file.write("newDisplay %s\n" %(self.display))
		file.write("oldDisplay %s\n" %(self.oldisplay))
		file.close()

	def load(self):
		fs = 0
		file = open(self.dataName,"r")
		line = file.readline().split()
		line = file.readline().split()
		self.width = int(line[1])
		self.height = int(line[2])

		line = file.readline().split()
		self.x = int(line[1])
		self.y = int(line[2])

		line = file.readline().split()
		fs = line[1]
		if fs == 1: self.fullscreen = True
		else: self.fullscreen = False

		line = file.readline().split()
		self.display = line[1]

		line = file.readline().split()
		self.oldisplay = line[1]

#########################################################################################################################################################

def newScreen(data):
	comman = "xrandr -s " + str(data.display)
	os.system(comman)

def restoreScreen(data):
	comman = "xrandr -s " + str(data.oldisplay)
	os.system(comman)







