#!/usr/bin/python
# *-* coding:utf-8 *-*

gen1 = (x for x in range(10))
def gen_function():
    yield 5
    yield 3
    yield 5
    yield 1
    yield 8
    yield 7

gen2 = gen_function()

# gen1 e gen2, são ambos geradores, a diferença é que o gen1 por
# ser gerado pela estrutura, é um objeto do tipo genexpr.
# por gen2 ser criado pelo yield da função, seu tipo é o nome da
# função "gen_function"

print type(gen1),type(gen2)
print gen1
print gen2

# para remover as informações, basta coloca-los em um for ou r-
# emover através do método next

print "Valores do gen1:"

while(True):
    try:
        print gen1.next()
    except:
        break

print "Valores do gen2:"

for x in gen2:
    print x
