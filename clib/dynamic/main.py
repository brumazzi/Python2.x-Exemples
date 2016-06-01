#!/usr/bin/env python
# *-* coding: utf-8 *-*

from ctypes import cdll

import sys
import os

libs = os.listdir("./libs/")

libs = [cdll.LoadLibrary("./libs/%s" % x) for x in libs]

for x in libs:
    x.run()
