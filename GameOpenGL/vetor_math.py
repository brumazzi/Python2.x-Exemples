import math

def _vectorSize3p(vector):
	x,y,z = vector
	vxy = (x[0]*x[0] + x[1]*x[1] + x[2]*x[2])*(y[0]*y[0]+y[1]*y[1]+y[2]*y[2])
	vyz = (y[0]*y[0] + y[1]*y[1] + y[2]*y[2])*(z[0]*z[0]+z[1]*z[1]+z[2]*z[2])
	vzx = (z[0]*z[0] + z[1]*z[1] + z[2]*z[2])*(x[0]*x[0]+x[1]*x[1]+x[2]*x[2])

	vxy = sqrt(vxy)
	vyz = sqrt(vyz)
	vzx = sqrt(vzx)

	
