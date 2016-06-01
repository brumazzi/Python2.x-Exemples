from ctypes import *

i = c_int(50)
pi = pointer(i)

pi[0] = 8

#O mesmo valo para um vetor normal quando se altera as suas posições
