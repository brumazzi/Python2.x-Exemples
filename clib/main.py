#!/usr/bin/env python
# *-* coding: utf-8 *-*
#
import ctypes
from ctypes import cdll
from sys import exit
from sys import platform
try:
    if platform == "win32":
        library = cdll.LoadLibrary('./sum.dll')
    else:
        library = cdll.LoadLibrary('./sum.so')
except:
    print ("Erro ao carregar biblioteca.")
    exit(1)

lsum = library.sum
ltex = library.texto

if __name__ == "__main__":
    print ("O código da ", lsum(5,15))
    print ("")
    x = ctypes.c_wchar_p("Brumazzi")

    res = ltex(b"Brumazzi")
    print ("------")
    print(res)
    print (ctypes.c_char_p(res).value)
