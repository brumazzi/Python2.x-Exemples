# *-* coding: utf-8 *-*

import pygtk
pygtk.require('2.0')
import gtk

def add_event(widget, event, function, data=None):
    try:
        widget.connect(event,function,data)
    except:
        print ("Erro ao efetuar ligação de eveto")

def evt(widget, data=None):
    print ("button")

class MainFrame():

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.button = gtk.Button("Close")

        self.configure()

        self.window.show_all()
        gtk.main()

    def configure(self):
        self.window.connect("destroy",self.destroy)
        self.button.connect("clicked",self.destroy)

        self.window.add(self.button)
        self.window.set_title("Main Frame")
        self.window.set_default_size(800,600)
        self.window.fullscreen()

    def destroy(self, widget, data=None):
        gtk.main_quit()
