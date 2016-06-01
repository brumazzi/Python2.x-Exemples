#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shelve as sl

class obj():
	def __init__(self):
		self.x=0;

def printer():
	print "";

data = sl.open('data.txt')

print data;
