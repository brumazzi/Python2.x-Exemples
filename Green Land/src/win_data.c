#include <stdio.h>
#include <stdlib.h>

typedef struct{
	int width;
	int height;
	int x,y;
	char fullscreen;
	char new_display[16];
	char old_display[16];
	char dataName[64];
}win_data;

win_data newData(){
	win_data wd;
	wd.width = 0;
	wd.height = 0;
	wd.x = 0;
	wd.y = 0;
	wd.fullscreen = 1;
	sprintf(wd.new_display,"0x0");
	sprintf(wd.old_display,"0x0");
	sprintf(wd.dataName,"data.cfg");

	return wd;
}

char saveData(win_data wd){
	FILE *save = fopen(wd.dataName,"w");
	fprintf(save,"\x01####GENERAL#CONFIG#FILE####\x01\n");
	fprintf(save,"\x10[%i|%i]\n",wd.width,wd.height);
	fprintf(save,"\x11[%i|%i]\n",wd.x,wd.y);
	fprintf(save,"\x12[%i]\n",wd.fullscreen);
	fprintf(save,"\x20[%s]\n",wd.new_display);
	fprintf(save,"\x21[%s]\n",wd.old_display);
	fclose(save);
	return 1;
}

win_data loadData(const char *fname){
	win_data wd;
	FILE *load = fopen(fname,"r");
	fscanf(load,"\x10[%i|%i]\n",&wd.width,&wd.height);
	fscanf(load,"\x11[%i|%i]\n",&wd.x,&wd.y);
	fscanf(load,"\x12[%i]\n",&wd.fullscreen);
	fscanf(load,"\x20[%s]\n",wd.new_display);
	fscanf(load,"\x21[%s]\n",wd.old_display);
	fclose(load);

	return wd;
}

char newDisplay(win_data wd){
	char dpy[64];
	sprintf(dpy,"xrandr -s %s",wd.new_display);
	system((const char *)dpy);
	return 1;
}

char oldDisplay(win_data wd){
	char dpy[64];
	sprintf(dpy,"xrandr -s %s",wd.old_display);
	system((const char *)dpy);
	return 1;
}

