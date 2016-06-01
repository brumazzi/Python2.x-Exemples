#!/usr/bin/env python

import Tkinter

class Main:
    
    def __init__(self,master):
        mf = Tkinter.Frame(master,cursor="pirate")
        mf.mainloop()

root = Tkinter.Tk()
root.title("ABC")
Main(root)