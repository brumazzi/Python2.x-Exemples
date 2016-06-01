#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Transcreve objetos e listas em texto e depois as recupera
import pickle as pk

class xobject(object):

	def __init__(self):
		self.x = 0;
		self.y = 1;
		self.z = -1;

vector = [1,2,3,4,5,6,{'field':7}];
obj = xobject();

class_str = pk.dumps(obj)
list_str = pk.dumps(vector)

fc = open("class.txt",'w')
fl = open("list.txt",'w')

fc.write(class_str)
fl.write(list_str)

fc.close()
fl.close()
