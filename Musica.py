#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import os.path
import pygame.mixer ,pygame.time

rdir = os.path.split(os.path.abspath(__file__))[0]

def Sound_Play(file_name=None):
    _mixer = pygame.mixer
    _time = pygame.time
    
    if file_name == None:
        file_name = os.path.join(rdir,"Música","house_lo.wav")
        
    _mixer.init(11025)
    _som = _mixer.Sound(file_name)
        
    print "Tocando"
        
    _play = _som.play()
    
    #while _play.get_busy():
    #    print "Tocando..."
    #    _time.wait(1000)
    #print "Fim"

class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):

        self.pnl = wx.Panel(self)
        self.button = wx.Button(self.pnl,label="&Click")
        #self._sair = wx.Button(self.pnl,label="&Sair",pos=(0,35))
        
        # ######################### Events ################################
        
        self.button.Bind(wx.EVT_BUTTON, self.Event_Button)
        #self._sair.Bind(wx.EVT_BUTTON, self.Evt_Close)
        self.pnl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.full = False
        
        # #################################################################
        
        self.pnl.SetFocus()

        self.SetSize((250, 180))
        self.SetTitle("")
        self.Centre()
        self.Show(True)
        self.pnl.SetSize(self.GetSize())
        self.SetBackgroundColour(wx.BLUE)
        self.Layout()
        print self.IsEnabled()
    
    def Event_Button(self, e):
        print "evento ativado com sucesso"
        Sound_Play()
        #self.ShowFullScreen(True)
        #self.pnl.SetFocus()
    
    def Evt_Close(self, e):
        print "teste"
        self.Close()
        #self.ShowFullScreen(False)

    def OnKeyDown(self, e):
        key = e.GetKeyCode()
        print key
        if key == wx.WXK_F11:
            #if self.IsFullScreen == False:
            if self.full == True: self.full = False
            else: self.full = True
            self.ShowFullScreen(self.full)
            #else: self.ShowFullScreen(False)
        #if key == wx.WXK_ESCAPE:
        #    self.ret  = wx.MessageBox('Are you sure to quit?', 'Question', 
        #    wx.YES_NO | wx.NO_DEFAULT, self)
        #if self.ret == wx.YES:
        #    self.Close()
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  
