#include <string.h>
#include <malloc.h>

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
char *vigenere(const char *key, unsigned char action, const char *value){
	int len = strlen(value);
	int klen = strlen(key);
	int x;

	char *swap;
	unsigned char *skey;
	skey = (unsigned char*) malloc(klen);
	strcpy(skey,key);
	if(action == CRIPT){ /*Verifica se vai criptografar*/
		swap = (char*) malloc(len);
		strcpy(swap, value);
		for(x=0; x<len; x++){
			if(swap[x] != 13 && swap[x] != ' '){
				skey[x] = toupper(skey[x]);
				swap[x] = toupper(swap[x]);	// Passa os caracteres para maiusculo
				/*
				 * Este block passa o caracter para "65" para "0"
				 */
				swap[x] -= 65;
				skey[x] -= 65;
				if(swap[x] < 0 || swap[x] > 26) // se o valor nao estiver entre 0 e 26, nao e' feito a criptografia
					return NULL;
				swap[x] = ((int)swap[x] + (skey[x%klen]+0)%26) % 26;
				swap[x] += 65;
			}
		}
	}
	else if(action == DECRIPT){ /*Verifica se vai descriptografar*/
		swap = (char*) malloc(len);
		strcpy(swap,value);
		for(x=0; x<len; x++){
			if(swap[x] != 13 && swap[x] != ' '){
				skey[x] = toupper(skey[x]);
				swap[x] = toupper(swap[x]); // Passa os caracteres para maiusculo
				/*
				 * Este block passa o caracter para "65" para "0"
				 */
				swap[x] -= 65;
				skey[x] -= 65;
				if(swap[x] < 0 || swap[x] > 26) // se o valor nao estiver entre 0 e 26, nao e' feito a criptografia
					return NULL;
				signed int c = ((signed int) swap[x] - (skey[x%klen]+0)%26);
				c = (c < 0 ? 26+c : c);
				swap[x] = (char) c;
				swap[x] += 65;
			}
		}
	}

	return swap;
}
