#define C_LIB

#include <string.h>
#include <malloc.h>
extern int sum(int x, int y){
	return x+y;
}

char *texto(const char *str){
	puts(str);
	char *cstr = malloc(64); // é obrigatorio q seja um ponteiro
	strcpy(cstr,"Bem Vindo! ");
	strcat(cstr, str);
	return cstr;
}
