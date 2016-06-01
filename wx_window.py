#!/usr/bin/env python

import wx;

class App(wx.App):
	def OnInit(self):
		form = wx.Frame(None, -1, "Titule",wx.DefaultPosition,wx.Size(800,600))
		form.Show(True)
		return True

App().MainLoop()



