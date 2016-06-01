#!/usr/bin/env python

import random as r
from threading import Thread
import time as t

def message(ms,tmp):
	t.sleep(tmp)
	print "Tempo de demora da saida da menssagem <ms"+str(ms)+"> \xc3\xa9 de \""+str(tmp)+"\" segundos."

for i in range(10):
	th = Thread(target=message,args=(i,r.randint(1,10)))
	th.start()
