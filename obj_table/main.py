#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle as pk
import psycopg2 as pg

class MyClass(object):
	def __init__(self):
		self.s = ''
		self.i = 0
		self.f = .0

obj = MyClass()

obj.s = ''
obj.i = 0
obj.f = .0

con = pg.connect("host='localhost' dbname='object' user='brumazzi'")
cur = con.cursor()

o_str = pk.dumps(obj)

print o_str
