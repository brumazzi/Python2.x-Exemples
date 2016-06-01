#!/bin/bash/env python

import random as rnd

f = open("Binary Codes",'w')

binary = [0]

for i in range(31):
	binary.append(0)

for i in range(120):
	for j in range(0,32):
		binary[j] = rnd.randint(0,1)

	code = ''
	for j in range(0,32):
		code = code + str(binary[j])

	f.write(code)
	#f.write('\n')
