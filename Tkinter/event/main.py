#!/usr/bin/env python3
# *-* coding:utf-8 *-*

from tkinter import *
from tkinter import ttk

root = Tk()

lb = ttk.Label(root, text="Waiting...")
lb.grid()
#lb.bind('<Enter>', lambda e: lb.configure(text="Moved mouse inside"))
lb.bind('<Motion>', lambda e: lb.configure(text="Moved mouse inside %dx%d" %(e.x, e.y)))
lb.bind('<Leave>', lambda e: lb.configure(text="Moved mouse outside"))
lb.bind('<1>', lambda e: lb.configure(text="Clicked left mouse button"))
lb.bind('<Double-1>', lambda e: lb.configure(text="Double clicked"))
lb.bind('<B3-Motion>', lambda e: lb.configure(text="right button drag to %d %d" %(e.x, e.y)))

root.mainloop()
