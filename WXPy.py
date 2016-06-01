#!/usr/bin/env python
import wx
 
ID_ABOUT = 101
ID_EXIT  = 102
 
class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title,
                         wx.DefaultPosition, wx.Size(200, 150))
        self.CreateStatusBar()
        self.SetStatusText("This is the statusbar")
        menu = wx.Menu()
        menu.Append(ID_ABOUT, "&About", "More information about this program")
        menu.AppendSeparator()
        menu.Append(ID_EXIT, "E&xit", "Terminate the program")
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "&File");
        self.SetMenuBar(menuBar)
 
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "Hello from wx.Python")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
 
app = MyApp(0)
app.MainLoop()
