#!/usr/bin/env python3
# *-* coding: utf-8 *-*

try:
    from tkinter import *
except:
    from Tkinter import *

import cifra as c
from cifra import root

root.title("Criptografia")
frame = [
    PanedWindow(root),
    Frame(root),
    Frame(root),
    Frame(root),
    Frame(root),
]

comp = [
    Radiobutton(frame[0],text="Cesar",value=1,variable=c.chk),
    Radiobutton(frame[0],text="Vigenere",value=2,variable=c.chk),
    Label(frame[1],text="Palavra:",width=8),
    Entry(frame[1],textvariable=c.msg),
    Label(frame[2],text="Chave:",width=8),
    Entry(frame[2],textvariable=c.key),
    Label(frame[3],text="Saida:",width=8),
    Entry(frame[3],textvariable=c.res),
    Button(frame[4],text="Descriptografar",command=c.decript),
    Button(frame[4],text="Criptografar",command=c.cript)
]

for x in frame:
    x.pack()

for x in comp:
    x.pack(side=LEFT)

root.maxsize(206,108)
root.minsize(206,108)

root.mainloop()
