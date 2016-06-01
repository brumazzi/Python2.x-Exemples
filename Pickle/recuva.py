#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Restaura objetos em forma de texto
import pickle as pk

class xobject(object):
	def __init__(self):
		x=0;
		y=0;
		z=0;

fc = open("class.txt")
fl = open("list.txt")

sc = fc.read()
sl = fl.read()

obj = pk.loads(sc)
vec = pk.loads(sl)

print obj.x,obj.y,obj.z
print vec
