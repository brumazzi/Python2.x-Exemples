l = []

print l

#insere valor em "l"
l.append(2)
l.append(1)
l.append(6)
print l

#insere valor em "l" na posicao "0"
l.insert(0,15)
print l

l.remove(2) #Apaga oque esta na posicao 2
print l

l.pop(2) #Retira o valor da posicao 2 e mostra
l.pop() #retira o ultimo valor e mostra
print l

l.index(15) # mostra a posicao do valor 15

l.extend([2,5,6,7,0,6,3,8,15,9,3,2,7,7,5,11]) # acrescenta array em "l"
print l

l.count(3) #Conta quantos "3" tem no array

l.sort()# coloca a lista em ordem crescente
print l

l.reverse() #inverte a ordem da lista
print l
