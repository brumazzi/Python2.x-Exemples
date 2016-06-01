#!/usr/bin/env python
# *-* coding: utf-8 *-*

import sys;
from sys import argv;

options = {
	'file_in':None,
	'file_out':None,
	'break':None,
	'block_size':0
};

fout = None;

def manual():
	print "break_file -b -s 10 <file>";

if argv[1] == '-h' or argv[1] == '--help':
	manual();
	sys.exit();

for i in range(len(argv)):
	if argv[i] == '-b' or argv[i] == '--break':
		options['break'] = True;
	elif argv[i] == '-r' or argv[i] == '--restore':
		options['break'] = False;
	elif argv[i] == '-s'or argv[i] == '--size':
		options['block_size'] = int(argv[i+1]);
		i+=1;
	else:
		try:
			options['file_in'] = open(argv[i]);
			fout = argv[i];
		except:
			options['file_in'] = None;

if options['file_in'] == None or options['break'] == None or options['block_size'] == 0:
	print "Parametros Invalidos."
	sys.exit()

if options['break'] == True:
	cnt = 1;
	while(True):
		name = "%s.part.%i" %(fout,cnt);
		options['file_out'] = open(name,'w');
		for i in range(0,1024*1024*options['block_size']):
			c = options['file_in'].read(1);
			options['file_out'].write(c);
			if(c == ""): sys.exit();
		options['file_out'].close();
		print "Maked %s" %(name);
		cnt+=1;
