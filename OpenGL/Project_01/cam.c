#include <GL/glu.h>

void lookAt(double a,double b,double c,double x,double y, double z,double rx,double ry, double rz){
	gluLookAt(a,b,c,x,y,z,rx,ry,rz);
}
