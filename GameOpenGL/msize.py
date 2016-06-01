import loadmodel as lm

m = lm.Ply()

m.load('Corpo_model')

x = []
y = []
z = []

x.append(0.0)
x.append(0.0)
y.append(0.0)
y.append(0.0)
z.append(0.0)
z.append(0.0)

for i in range(len(m.vx)):
	if m.vx[i] < 0:
		x[0] += m.vx[i]
	elif m.vx[i] > 0:
		x[1] += m.vx[i]
	if m.vy[i] < 0:
		y[0] += m.vy[i]
	elif m.vy[i] > 0:
		y[1] += m.vy[i]
	if m.vz[i] < 0:
		z[0] += m.vz[i]
	elif m.vz[i] > 0:
		z[1] += m.vz[i]
