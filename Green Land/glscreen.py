def Init():
	glclearColor(.0,.0,.0,1.)

def Projection():
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glViewport(0,0,800,600)

	Menu()

	glMatixMode(GL_MODELVIEW)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)

	Light()



def Game():
	glLoadIdentity()
	gluLookAt(0,0,0,0,0,0,0,0,0)



def Menu():
	glMatixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerpective(40,800/600,1.0,500.)

def Light():
	x=0
