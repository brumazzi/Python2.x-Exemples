#!/usr/bin/env python3
try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    from Tkinter import messagebox

import sys
import ctypes
from ctypes import cdll

root = tk.Tk()

chk = tk.IntVar()
msg = tk.StringVar()
key = tk.StringVar()
res = tk.StringVar()

try:
    libcesar = cdll.LoadLibrary("./libcesar.so")
except:
    print("Can't found libcesar.so")
    sys.exit(1)
try:
    libvigenere = cdll.LoadLibrary("libvigenere.so")
except:
    print("Can't found libvigenere.so")
    sys.exit(1)


cesar = libcesar.cesar
vigenere = libvigenere.vigenere

def cript():
    r = None
    if chk.get() == 1:
        try:
            k = int(key.get())
        except:
            print(key.get())
            messagebox.showerror("Erro","Chave inválida!")
            return 0;
        r = cesar(k, 1, bytes(msg.get(),'utf-8'))
    elif chk.get() == 2:
        r = vigenere(key.get(), 1, bytes(msg.get(),'utf-8'))

    res.set(ctypes.c_char_p(r).value)

def decript():
    r = None
    if chk.get() == 1:
        try:
            k = int(key.get())
        except:
            tk.messagebox.showerror("Erro","Chave inválida!")
            return 0;
        r = cesar(k, 2, bytes(msg.get(),'utf-8'))
    elif chk.get() == 2:
        r = vigenere(key.get(), 2, bytes(msg.get(),'utf-8'))
    
    res.set(ctypes.c_char_p(r).value)
