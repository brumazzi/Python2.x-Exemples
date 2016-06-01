#!/usr/bin/env python

BAT1="/sys/class/power_supply/BAT1/capacity"

fcap = open(BAT1,"r")

cap = int(fcap.read())

fcap.close()

import time
import os

while (True):
	if cap < 7:
		os.system("zenity --warning --text='Bateria em %i%%'" %cap)
		time.sleep(50)
		continue
	time.sleep(10)

