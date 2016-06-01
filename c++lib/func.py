#!/usr/bin/env python
import ctypes
from ctypes import cdll
from ctypes import *

class teste(Structure):
	_fields_ =[("numero",c_int),("nreal",c_double)]


libfunc = cdll.LoadLibrary("./libfunc.so")

soma = libfunc.sum(2,3)
subtrac = libfunc.sub(1,1)
tx = libfunc.function
tx.restype = c_double
tx.argtypes = [POINTER(teste)]

ts = teste(2,2)

print soma,"\n",subtrac

print "\n\n"

print tx(pointer(ts))
