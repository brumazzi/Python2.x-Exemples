#include "func.h"
#include <math.h>

int sum(int x,int y){
	int z = x+y;
	return z;
}

int sub(int x,int y){
	int z = x-y;
	return z;
}
double function(teste *p){
      return sqrt(p->x*p->x + p->y*p->y);
}
