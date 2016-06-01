#!/usr/bin/python
#*-* coding:utf8 *-*

var1 = set('palavra')    # Ordena a string e remove caracteres repetidos
                        # O mesmo vale para numeros

var2 = {x**x for x in range(5)} # Essa estrutura retorna um set
                                # x**x insere x^x tal que x recebe o valor
                                # diretamente do for

print type(var1),"-",type(var2)

print "var1:",var1
print "removendo de var1:",var1.pop()
print "var1:",var1
print "var2:",var2
var2.add('texto')
print "var2:",var2

# Perceba que o texto foi inserido inteiro ao contrario de var1
# pois apenas o texto é considerado um vetor de bytes, já o me-
# todo add, inseri a informação em um vetor, por isso que o te-
# xto não foi desmenbrado.


# Para remover os itens, basta usar o metodo clear, ou o pop
# O for apenas percore as informações
for x in var2:
    print x

var1.clear()

print var1,var2
