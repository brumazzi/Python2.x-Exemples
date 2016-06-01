#!/usr/bin/python
# *-* coding:utf-8 *-*

import os

DIR_FILES = "/home/brumazzi/Público/"

def get_all_files(path):
    __files__ = ""

    if not os.path.isdir(path):
        return "None"
    for x in os.listdir(path):
        if os.path.isdir(path+x):
            __files__ = __files__+get_all_files(path+x+"/")
        elif os.path.isfile(path+x):
            __files__ = __files__+path+x+"|"

    return __files__

