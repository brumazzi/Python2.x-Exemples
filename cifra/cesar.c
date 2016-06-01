#include <malloc.h>
#include <string.h>

#define CRIPT 1
#define DECRIPT 2

/*
 * Este método usa a criptografia de cesar para criptografar menssagens
 * Parametros:
 * 	chave de valor inteiro
 * 	tipo de ação do método "criptografar" ou "descriptografar"
 * 	texto a ser processado
 * O retorno deverá ser o texto criptografado ou descriptografado
 */
char *cesar(unsigned int key, unsigned char action, const char *value){
	int len = strlen(value);
	char *swap;
	if(action == CRIPT){ /*Verifica se vai criptografar*/
		swap = (char*) malloc(len);
		strcpy(swap, value);
		while(len--){
			if(swap[len] != 13 && swap[len] != ' '){
				swap[len] = toupper(swap[len]);	// Passa os caracteres para maiusculo
				/*
				 * Este block passa o caracter para "65" para "0"
				 */
				swap[len] -= 65;
				if(swap[len] < 0 || swap[len] > 26) // se o valor nao estiver entre 0 e 26, nao e' feito a criptografia
					return NULL;
				swap[len] = ((int)swap[len] + key) % 26;
				swap[len] += 65;
			}
		}
	}
	else if(action == DECRIPT){ /*Verifica se vai descriptografar*/
		swap = (char*) malloc(len);
		strcpy(swap,value);
		while(len--){
			if(swap[len] != 13 && swap[len] != ' '){
				swap[len] = toupper(swap[len]); // Passa os caracteres para maiusculo
				/*
				 * Este block passa o caracter para "65" para "0"
				 */
				swap[len] -= 65;
				if(swap[len] < 0 || swap[len] > 26) // se o valor nao estiver entre 0 e 26, nao e' feito a criptografia
					return NULL;
				signed int x = ((signed int) swap[len] - key);
				x = (x < 0 ? 26+x : x);
				swap[len] = (char) x;
				swap[len] += 65;
			}
		}
	}

	return swap;
}
