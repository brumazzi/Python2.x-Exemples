#!/usr/bin/env python
#*-* coding:utf-8 *-*

class Res(object):
    def __init__(self,str=""):
        self.str=str

    def __str__(self):
        return self.str

    def set(self, str):
        self.str = str

r = Res(str="data")
print r
