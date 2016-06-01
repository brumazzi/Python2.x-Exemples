############################################################
#
#		Verificador.
#
############################################################

import sys

try:
	from wx import *
except:
	print "\"WX\" not found."
	sys.exit()
try:
	import OpenGL
	from OpenGL.GL import *
	from OpenGL.GLU import *
except:
	print "\"PyOpenGL\" not found."
	sys.exit()

from canva import *

class GameFrame(Frame):

	def __init__(self,*args,**kw):
		kwds["style"] = NO_BORDER
		Frame.__init__(self,*args,**kw)

		############Components############
		self.pnl = Panel(self)
		self.canvas = GLC(self.pnl)
		

def __start__(argv):
	if(argv[1] != ""):
		exit()
	root = App()
	GameFrame(None)
	root.MainLoop()
