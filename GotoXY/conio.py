#!/usr/bin/env python
# -*- coding:utf-8 -*-

def printxy(x,y,text):
	print "%c[%i;%if%s" %(0x1B, y, x,text);


