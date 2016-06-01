import gtk
 
class HelloWorld(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect("delete_event", gtk.main_quit)
        self.set_border_width(10)
        self.set_title("Hello World!")
        hbox = gtk.HBox()
        self.add(hbox)
        self.button1 = gtk.Button("Button 1")
        self.button1.connect("clicked", self.button_pressed_cb)
        hbox.pack_start(self.button1)
        self.button2 = gtk.Button("Button 2")
        self.button2.connect("clicked", self.button_pressed_cb)
        hbox.pack_start(self.button2)
 
    def button_pressed_cb(self, button):
        print "Hello again - %s was pressed" % button.get_label()
 
if __name__ == "__main__":
    win = HelloWorld()
    win.show_all()
    gtk.main()