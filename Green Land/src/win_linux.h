#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <X11/X.h>
#include <X11/Xlib.h>

#include <GL/gl.h>
#include <GL/glx.h>
#include <GL/glu.h>

#include <screen.h>
#include <control.h>

#define _error(str){printf(str);exit(0);}while(0)

x11_window win;
winData windta;

int start_window(){
	win.dpy = XOpenDisplay(NULL);
	if(win.dpy == NULL)
		_error("Erro ao executar o X11.\n");

	win.root = DefaultRootWindow(win.dpy);
	GLint att[5] = {GLX_RGBA, GLX_DEPTH_SIZE, 24, GLX_DOUBLEBUFFER, None};
	win.vi = glXChooseVisual(win.dpy,0,att);
	if(win.vi == NULL)
		_error("Falha ao carregar o vi.\n");

	win.cmap = XCreateColormap(win.dpy,win.root,win.vi->visual,AllocNone);
	win.swa.colormap = win.cmap;
	win.swa.event_mask = ExposureMask | KeyPressMask | KeyReleaseMask | ButtonPressMask | ButtonReleaseMask;

	if(!fopen("orbis.cfg","r")){
		Screen *screen = XScreenOfDisplay(win.dpy,0);
		windta.width = 1366;
		windta.height = 768;
		windta.x = screen->width/2;
		windta.y = screen->height/2;
		windta.screen = 0;

		saveWinData(windta);
	}else windta = loadWinData();

	win.win = XCreateWindow(win.dpy, win.root, windta.x, windta.y, windta.width, windta.height, 0, win.vi->depth, InputOutput, win.vi->visual, CWColormap|CWEventMask,&win.swa);

	XMapWindow(win.dpy,win.win);
	XStoreName(win.dpy,win.win,"");

	win.glc = glXCreateContext(win.dpy,win.vi,NULL,GL_TRUE);
	glXMakeCurrent(win.dpy,win.win,win.glc);

	glEnable(GL_DEPTH_TEST);

	//XSelectInput(win.dpy,win.win,KeyPressMask | ButtonPressMask | ExposureMask);

	char process = 1;
	while(process){
		XNextEvent(win.dpy,&win.xevt);
		switch(win.xevt.type){
			case ButtonPress:
				//printf("Mouse Funcionando.\n");
				_mouse(win.xevt,1);
				break;
			case ButtonRelease:
				_mouse(win.xevt,0);
				break;
			case KeyPress:
				//printf("Teclado Funcionando.\n");
				process = _keyboard(win.xevt,1);
				break;
			case KeyRelease:
				process = _keyboard(win.xevt,0);
			case Expose:
				XGetWindowAttributes(win.dpy, win.win, &win.gwa);
				_initGame();
				printf("Expose Funcionando.\n");
				glXSwapBuffers(win.dpy, win.win);
				break;
		}
	}

	glXDestroyContext(win.dpy,win.glc);
	XDestroyWindow(win.dpy,win.win);
	XCloseDisplay(win.dpy);

	return 0;
}
