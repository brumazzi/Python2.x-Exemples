#!/usr/bin/env python


var = iter('vetor')
print type(var)

print "tamanho:", var.__length_hint__()
print "saida:", var.next() # Vai para o proximo elemento

for x in var:
    print "saida:",x
