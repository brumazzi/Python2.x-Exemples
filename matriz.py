import random as rnd

mz = []

l = input("Linhas: ")
c = input("Colunas: ")
for i in range(l):
	mz.append([])
	for j in range(c):
		mz[i].append(rnd.randint(0,9))

for i in range(len(mz)):
	print mz[i]

print mz
