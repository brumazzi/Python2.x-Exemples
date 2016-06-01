#!/usr/bin/env python2.7
#*-* coding: utf-8 *-*

import ctypes
import sys
import os
import wx

from ctypes import cdll

libs = []
for lib in os.listdir("./modules/"):
    libs.append(cdll.LoadLibrary("./modules/%s" % lib))

class Main(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds['style'] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self,*args,**kwds)
        self.Size = (800,600)
        self.pleft = wx.Panel(self,-1)
        self.pright = wx.Panel(self,-1)
        self.brun = wx.Button(self.pright,-1,"Abrir")

        self.__configure__()
        self.__events__()
        self.Show(True)

    def __configure__(self):
        self.SetTitle("App Manager")
        self.pleft.Position = (0,0)
        self.pleft.Size = (self.Size[0]*0.1,self.Size[1])
        self.pright.Position = (self.pleft.Size[0],0)
        self.pright.Size = (self.Size[0]-self.pleft.Size[0],self.Size[1])
        self.brun.Position = (16,16)

        self.pleft.SetBackgroundColour(wx.Colour(69,76,255))
        self.pright.SetBackgroundColour(wx.Colour(69,76,100))

        self.Layout()

    def __events__(self):
        self.Bind(wx.EVT_SIZE, self.OnResize)

    def OnResize(self, event):
        self.__configure__()

if __name__ == '__main__':
    root = wx.App()
    mw = Main(None)
    root.MainLoop()
