#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shelve as sl

class obj:
    def __init__(self):
        pass

data = sl.open('data.txt')

def printer():
    print "text"

print(data['object'])
