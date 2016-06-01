#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg="black")

cord = [10,50,240,210]

arc = canvas.create_arc(cord, start=0, extent=150, fill="yellow")

canvas.pack()

root.mainloop()
