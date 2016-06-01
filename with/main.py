#!/usr/bin/python
# *-* coding: utf-8 *-*

with open('file') as f:
    data = f.read()
    data = data.split('\n')
    print data

    class vec:
        def __init__(self):
            print "Init"
        def __enter__(self):
            print "Enter"
            return [1,3,5,2,0,'texto']
        def __exit__(self, type, val, tback):
            print "Exit"
            return "Exiting..."

    with vec() as v:
        print v

    print "#########################"

    x = vec()
