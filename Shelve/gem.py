#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shelve as sl

class obj():
	def __init__(self):
		self.x=0;

o = obj();
o.x = 6;

def printer():
	print "New Message.";

user = sl.open('data.txt')
user['name'] = 'Brumazzi';
user['login'] = 'brumazzi';
user['age'] = 20;
user['vec'] = [1,2,3,4,5,6]
user['object'] = o;
user['def'] = printer;
user.close();
