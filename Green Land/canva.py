import sys
try:
	import wx
	from wx.glcanvas import *
except:
	sys.exit()

class GLC(GLCanvas):

	def __init__(self,parent,att = None, id = wx.ID_ANY):
		if not att:
			att = [WX_GL_RGBA, WX_GL_DOUBLEBUFFER, WX_GL_DEPTH_SIZE, 20]
		GLCanvas.__init__(self, parent, id, attribList = att)
