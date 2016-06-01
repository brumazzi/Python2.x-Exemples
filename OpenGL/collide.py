#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class createpoint:
	def __init__(self,p,c=(1,0,0)):
		self.point_size=0.5
		self.color=c
		self.x=p[0]
		self.y=p[1]
		self.z=p[2]

#return the corrdinates
	def get_pos(self):
		return self.x,self.y,self.z

	def glvertex(self):
		glVertex3f(self.x,self.y,self.z)

	def draw(self,c=(0,1,0)):
		glPointSize(self.point_size)
		glBegin(GL_POINTS)
		glColor3f(self.color[0],self.color[1],self.color[2])
		glVertex3f(self.x,self.y,self.z);# front face
		glEnd()
	
class createline:
	def __init__(self,p1,p2):
		self.color=0,1,0
		self.p1=p1
		self.p2=p2
		self.direction=self.direction_vector()
		self.newPoint=None
	
	#calculate direction line is travelling using its points
	def direction_vector(self):
		return createpoint((self.p2.x-self.p1.x,self.p2.y-self.p1.y,self.p2.z-self.p1.z))
	
	def glvertex(self):
		glVertex3f(self.p1.x,self.p1.y,self.p1.z)
	
	#vertexs to draw a line use with glbegin(GL_LINES)
	def glvertexlist(self):
		glVertex3f(self.p1.x,self.p1.y,self.p1.z)
		glVertex3f(self.p2.x,self.p2.y,self.p2.z)
	
	#t=0 returns first point t=1 returns last point values in between are long the line
	#returns a new point cordinate
	def get_point_along_line(self,t=0):
		self.newPoint=None
		if t and t!=0 and t!=1:
			self.newPoint=createpoint((self.p1.x+(self.direction.x*t),self.p1.y+(self.direction.y*t),self.p1.z+(self.direction.z*t)))
		else:
			return None
		return self.newPoint
	
class createplane:
	def __init__(self,p1,p2,p3):
		self.p1=createpoint(p1)
		self.p2=createpoint(p2)
		self.p3=createpoint(p3)
		self.normal=createpoint((0,1,0))
	
	def dot_product(self,v1,v2):
		result=0
		for i in range(0,3):
			result+=v1[i]*v2[i]
		return result
	
	def find_intersection_distance(self,p1,p2):
		d=((self.p2.y*self.p3.z)-(self.p3.y*self.p2.z)-(self.p3.y*self.p1.z-self.p1.y*self.p3.z)-(self.p1.y*self.p2.z-	self.p2.y*self.p1.z))
		a1=self.dot_product(((-d-p1.x),(-d-p1.y),(-d-p1.z)),(0,1,0))
		a2=self.dot_product(((p2.x-p1.x),(p2.y-p1.y),(p2.z-p1.z)),(0,1,0))
	
		if a1!=0 and a2!=0:
			return a1/a2
		else:
			return None
	  
	def draw(self):
		glBegin(GL_TRIANGLE_STRIP)
		glColor3f(1.0, 1.0, 1.0)
		glNormal3f(self.normal.x,self.normal.y,self.normal.z)
		glVertex3f(self.p1.x,self.p1.y,self.p1.z)
		glVertex3f(self.p2.x,self.p2.y,self.p2.z)
		glVertex3f(self.p3.x,self.p3.y,self.p3.z)
		glEnd()
		self.p1.draw((1,0,0))
		self.p2.draw((0,1,0))
		self.p3.draw((0,0,1))
	
	def draw_normals(self):
		glBegin(GL_LINES)
		glColor3f(0.0, 1.0, 1.0)
		glVertex3f(self.p1.x,self.p1.y,self.p1.z)
		glVertex3f(self.normal.x*10,self.normal.y*10.0,self.normal.z*10.0)
		glEnd()
	
	
	def get_normal(self):
		return self.normal
class draw_triangle:
	def __init__(self,p1,p2,p3):
	#3 points of the triangle
		self.points=createpoint(p1),createpoint(p2),createpoint(p3)
	
	#3 lines in the triangle
		self.lines=createline(self.points[0],self.points[1]),createline(self.points[1],self.points[2]),createline(self.points	[0],self.points[2])
	
	#triangles normal
		self.normal=createpoint(self.calculate_normal(self.points[0],self.points[1],self.points[2]))#(0,1,0)#
	
	#calculate vector / edge
	def calculate_vector(self,p1,p2):
		return -p1.x+p2.x,-p1.y+p2.y,-p1.z+p2.z
	
	def cross_product(self,p1,p2):
		return (p1[1]*p2[2]-p2[1]*p1[2]) , (p1[2]*p2[0])-(p2[2]*p1[0]) , (p1[0]*p2[1])-(p2[0]*p1[1])
	
	def get_lines(self):
		for l in self.lines:
			yield l
	
	def calculate_normal(self,p1,p2,p3):
		a=self.calculate_vector(p3,p2)
		b=self.calculate_vector(p3,p1)
	#calculate the cross product returns a vector
		return self.cross_product(a,b)
	
	#draw the triangle
	def draw(self):
		glBegin(GL_TRIANGLES)
		glColor3f(0.0, 0.0, 1.0)
		glNormal3f(self.normal.x,self.normal.y,self.normal.z)
		glVertex3f(self.points[0].x,self.points[0].y,self.points[0].z)
		glVertex3f(self.points[1].x,self.points[1].y,self.points[1].z)
		glVertex3f(self.points[2].x,self.points[2].y,self.points[2].z)
		glEnd()
	
	#draw the triangles points
		self.points[0].draw((1,0,0))
		self.points[1].draw((0,1,0))
		self.points[2].draw((0,0,1))
	  
	   #draw triangle normal
	def draw_normals(self):
		glBegin(GL_LINES)
		glColor3f(0.0, 1.0, 1.0)
		glVertex3f(self.points[0].x,self.points[0].y,self.points[0].z)
		glVertex3f(self.normal.x*5,self.normal.y*5,self.normal.z*5)
		glEnd()
	
	
	
	
		name=''
		center=createpoint((0,0,0))
	
	
		plane=createplane((0.0,0.0,0.0),(20.0,0.0,0.0),(0.0,0.0,20.0))
		p1=10.0,-5.0,10.0
		p2=0.0,5.0,0.0
		p3=10.0,5.0,10.0
		tri=draw_triangle(p1,p2,p3)
	#print 'plane'+str(tri.calculate_plane())
	
	#test intersection function
	def intersections():
		glPointSize(5)
		glBegin(GL_POINTS)
		glColor3f(0.0, 1.0, 0.0)
		count=0
		for l in tri.get_lines():
		#distance along a line will return null if no intersection
			t=plane.find_intersection_distance(l.p1,l.p2)
	
	#find the intersection point using t
		if t:
			np=l.get_point_along_line(t)
	
	#if there was an intersetion point display it, the point was stored in the class line as newPoint
		if l.newPoint:
			glVertex3f(l.newPoint.x,l.newPoint.y,l.newPoint.z)
			count+=1
		glEnd()
	
	
class draw_scene:
	def __init__(self,style=1):
		self.init_shading()
	
	#solid model with a light / shading
	def init_shading(self):
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_SMOOTH)  
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0)) 
		glMatrixMode(GL_MODELVIEW)
	
	def resize(self,(width, height)):
		if height==0:
			height=1
			glViewport(0, 0, width, height)
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluPerspective(45, 1.0*width/height, 0.1, 100.0)
			#gluLookAt(0.0,0.0,45.0,0,0,0,0,40.0,0)
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
	
	def init(self):
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_SMOOTH)  
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
	
		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0)) 
		glMatrixMode(GL_MODELVIEW)
	
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(0.0,-26.0, -100.0)
		size=3
		tri.draw()
		tri.draw_normals()
	
		plane.draw()
		plane.draw_normals()
		n=plane.get_normal()
		intersections()
	
	
	
	  
	#main program loop
def main():
	#initalize pygame
	pygame.init()
	pygame.display.set_mode((640,480), OPENGL|DOUBLEBUF)
		
	#setup the open gl scene
	scene=draw_scene()
	scene.resize((640,480))
	frames = 0
	ticks = pygame.time.get_ticks()
	while 1:
		event = pygame.event.poll()
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			break
	#draw the scene
	scene.draw()
	pygame.display.flip()
	frames = frames+1
	
	print "fps:  %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks))


if __name__ == '__main__': main()
