#!/usr/bin/python

'''Spinning cube wxPython and PyOpenGL app'''

import wx
from wx.glcanvas import *

import OpenGL
from OpenGL import GLU
from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLU import *

Near    = 1.0
Far     = 20.0

Verts = [
    ( -0.5,  0.5, -0.5 ),   # left top rear
    (  0.5,  0.5, -0.5 ),   # right top rear
    (  0.5, -0.5, -0.5 ),   # right bottom rear
    ( -0.5, -0.5, -0.5 ),   # left bottom rear
    ( -0.5,  0.5,  0.5 ),   # left top front
    (  0.5,  0.5,  0.5 ),   # right top front
    (  0.5, -0.5,  0.5 ),   # right bottom front
    ( -0.5, -0.5,  0.5 ),   # left bottom front
]

Faces = [
    7, 6, 5, 4,     # front
    6, 2, 1, 5,     # right
    3, 7, 4, 0,     # left
    5, 1, 0, 4,     # top
    3, 2, 6, 7,     # bottom
    2, 3, 0, 1,     # rear
]

def drawCube ():
    glBegin(GL_QUADS)
    for idx in Faces:
        glColor3f(0.0, 1.0, 0.0)
        glVertex3fv(Verts[idx])
    glEnd()
#

class MyCanvas (GLCanvas):
    '''Actual OpenGL scene'''
    #
    def __init__ (self, parent, attribs = None, id = wx.ID_ANY):
        if not attribs:
            attribs = [WX_GL_RGBA, WX_GL_DOUBLEBUFFER, WX_GL_DEPTH_SIZE, 24]
        GLCanvas.__init__(self, parent, id, attribList = attribs)
        self.init   = False
        self.width  = 0
        self.height = 0
        # Display event handlers
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        # Simple keyboard handler
        self.Bind(wx.EVT_CHAR, self.key)
        # Animation
        self.spin = 0.0
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.spinCube)
        self.timer.Start(1000.0 / 60.0)
    #
    def OnPaint (self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent()
        if not self.init:
            self.initGL()
        self.clear()
        self.setProjection()
        self.setViewpoint()
        self.drawWorld()
        self.SwapBuffers()
    #
    def OnSize (self, event):
        # Note these are ints, not floats, for glViewport
        self.width, self.height = self.GetSizeTuple()
    #
    def initGL (self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.init = True
    #
    def clear (self):
        glViewport(0, 0, self.width, self.height)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #
    def setProjection (self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(self.width) / float(self.height), Near, Far)
        glMatrixMode(GL_MODELVIEW)
    #
    def setViewpoint (self):
        glLoadIdentity()
        gluLookAt(0.0, 1.0, -5.0,
                  0.0, 0.0, 0.0,
                  0.0, 1.0, 0.0)
    #
    def drawWorld (self):
        glPushMatrix()
        glRotatef(self.spin, 0, 1, 0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # glEnable(GL_CULL_FACE)
        drawCube()
        glPopMatrix()
    #
    def key (self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.GetParent().Close()
    #
    def spinCube (self, event):
        self.spin = (self.spin + 2) % 360
        self.Refresh()
    #
#

class MyApp (wx.App):
    '''Very simple wxPython app to test OpenGL'''
    #
    def OnInit (self):
        self.frame = wx.Frame(parent = None, id = wx.ID_ANY,
                    title="Hello OpenGL",
                    pos = wx.DefaultPosition, size = (800, 600))
        self.canvas = MyCanvas(self.frame)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    #
#

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

