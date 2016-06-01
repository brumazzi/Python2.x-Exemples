import time
import os
t = 0.001#time.time()
#varit = 0.4744334399
#varit2 = 273.167928524
x = 0
for i in range(0,361):
	os.system('clear')
	#print ((time.time() - t)%(10)/10)*360
	#nt = time.time() - t
	a = i*0.001
	print round(a,6)
	print ((i*t)%(.36)/.36)*360
	#print '|',nt,'|'
	print i
#	t += 0.0013187561
	os.system("sleep 0.0005")

t = time.time()	
os.system('sleep 0.00001')
for i in range(1,5):
	nt = time.time() - t
	print nt
	nt = time.time() - t
	print nt
	nt = time.time() - t
	print nt
	nt = time.time() - t
	print nt
	nt = time.time() - t
	print nt
	os.system('sleep 0.5')
