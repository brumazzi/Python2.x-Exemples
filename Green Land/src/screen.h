#ifndef SCREEN
#define SCREEN

#include <stdio.h>

#ifdef __GNUC__

#include <GL/glx.h>
#include <X11/X.h>
#include <X11/Xlib.h>

#endif

typedef struct{
	int position[2];
	int width;
	int height;
	char screen;
	int x;
	int y;
}winData;

#ifdef __GNUC__

typedef struct{
	Display                 *dpy;
	Window                  root;
	XVisualInfo             *vi;
	Colormap                cmap;
	XSetWindowAttributes    swa;
	Window                  win;
	GLXContext              glc;
	XWindowAttributes       gwa;
	XEvent                  xevt;
}x11_window;

#endif

winData loadWinData();
char saveWinData(winData win);

winData loadWinData(){
	winData win;
	FILE *f;

	f = fopen("Green Land","r");

	char buffer[256];
	fgets(buffer,256,f);

	fscanf(f,"%i %i",&win.width,&win.height);
	fscanf(f,"%i %i",&win.x,&win.y);
	fscanf(f,"%c",&win.screen);

	fclose(f);
	return win;
}

char saveWinData(winData win){
	FILE *f = fopen("orbis.cfg","w");

	fprintf(f,"\x01##CONFIG#FILE##\x01\n");
	fprintf(f,"%i %i\n",win.width,win.height);
	fprintf(f,"%i %i\n",win.x,win.y);
	fprintf(f,"%c",win.screen);

	fclose(f);
	return 1;
}

#endif
