#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys;
import time;
import os;
import conio;

from sys import argv;
from conio import printxy;

argc = len(argv);

s_time = None;
version = "timer 1.0";

opt = {
	'alarm':False,
	'loop':False,
	'time':False,
	'atime':["00","00","00"],
	'date':None,
	'day':None
}

def error():
	print "timer [--option] <value>";
	print "timer -t -a 12:00:00 -d 5/Fev/2014";
	print "timer -t -a 12:00:00 -D Seg";
	print "Commands:";
	print "\t-a, --alarm\tHorário para o alarme despertar.";
	print "\t-d, --date\tData que o alarme será tocado.";
	print "\t-D, --day\tDia da semana que será ativo.";
	print "\t-h, --help\tImprime essa tela."
	print "\t-l, --loop\tEntra em loop.";
	print "\t-t, --time\tImprime horário atual.";
	print "\t-v, --version\tImprime a versão.\n";
	sys.exit();

if argc == 1:
	sys.exit();

for i in range(argc):
	if argv[i] == '-a' or argv[i] == '--alarm':
		opt['alarm'] = True;
		i += 1;
		opt['atime'] = argv[i].split(':');

		if(len(opt['atime']) != 3):
			error();

	elif argv[i] == '-l' or argv[i] == '-loop':
		opt['loop'] = True;
	elif argv[i] == '-t' or argv[i] == '--time':
		opt['time'] = True;
	elif argv[i] == '-d' or argv[i] == '--date':
		i += 1;
		opt['date'] = str(argv[i]).split('/');
		if(len(opt['date']) != 3):
			error();
	elif argv[i] == '--day' or argv[i] == "-D":
		i += 1;
		opt['day'] = argv[i];
	elif argv[i] == '-v' or argv[i] == '--version':
		print version;
		sys.exit();
	elif argv[i] == '--help' or argv[i] == '-h':
		error();

if opt['time'] and opt['alarm'] != True:
	while(opt['loop']):
		os.system('clear');
		printxy(0,0,time.ctime());
	print time.ctime();
	sys.exit();

os.system('clear');

clock = "";
date = "";

while(opt['alarm']):
	s_time = str(time.ctime()).split();
	
	if(opt['time']):
		printxy(1,0,'Date: %s/%s/%s' %(s_time[2], s_time[1], s_time[4]));
		printxy(2,0,'Hour: %s' %(s_time[3]));
		printxy(3,0,'Alarm: %s:%s:%s' %(opt['atime'][0], opt['atime'][1], opt['atime'][2]));
	
	clock = "%s:%s:%s" %(opt['atime'][0], opt['atime'][1], opt['atime'][2]);

	if clock == s_time[3]:
		if opt['day'] != None:
			if s_time[0].upper() == opt['day'].upper():
				break;
		elif opt['date'] != None:
			if opt['date'][0] == s_time[2] and opt['date'][1] == s_time[1] and opt['date'][2] == s_time[4]:
				break;
		else:
			break;
	
	time.sleep(1);
