#!/usr/bin/env python

class MainClass:
        def __init__(self):
            print("__INIT__")
        def __call__(self):
            print("__CALL__")
        def __del__(self):
            print("__DEL__")
        def __new__(self):
            print("__NEW__")

c = MainClass()
MainClass()
del c
