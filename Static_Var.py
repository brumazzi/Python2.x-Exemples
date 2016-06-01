#!/usr/bin/env python
#*-* coding:utf-8 *-*

def static_vars(**kwds):
    def decorate(func):
        for key in kwds:
            setattr(func, key, kwds[key])
        return func
    return decorate

def static_var(var,value):
    def decorate(func):
        setattr(func, var, value)
        return func
    return decorate

@static_vars(var=0,name="User")
def function():
    function.var += 1
    User = "%s count %i" %(function.name, function.var)
    print User

@static_var('x','')
def one_var():
    one_var.x += '#'
    return one_var.x

for x in range(13):
    function()
    print one_var()
