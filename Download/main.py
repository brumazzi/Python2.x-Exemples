#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys;
import os;
from sys import argv;
from os import system;

for x in argv:
	mirror = open(x,"r");

	path = mirror.readline();
	path = path.split();
	link = path[1];
	v = "0";
	while(v != ""):
		link = mirror.readline();
		v = link;
		link = link.split(" ");
		if link[0] == '201:':
			link = link[1].split("\"")[1];
			link = "%s%s" %(path[1],link);
			comman = "wget -c %s" %link;
			system(comman);
