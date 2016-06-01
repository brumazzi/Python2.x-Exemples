#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

size = {
	"KB":1,
	"MB":1024,
	"GB":1024*1024
}

file = open(sys.argv[1]);

cnt = 0;
size=0;
char = "0";

while(True):
	out = open(sys.argv[1]+".part."+str(cnt),'w');
	for i in range(0, 10):
		char = file.read(1024);
		out.write(char);
	out.close();
	if char == "": break;
