#!/usr/bin/env python
# *-* coding: utf-8 *-*

class Static_Method(object):
    res = 0
    @staticmethod
    def static_sum(x, y):
        Static_Method.res = x+y
    
    @classmethod
    def static_div(this, x, y):
        this.res = x/y

Static_Method.static_sum(15,5)
print "O código da:", Static_Method.res
Static_Method.static_div(15,5)
print "A divisão é:", Static_Method.res
