#!/usr/bin/env python
#*-* coding:utf-8 *-*

#######################################################
# A classe RSA, possui os métodos de criptografia onde#
# P e Q são chaver para o calculo dos valores para se-#
# rem usados na criptografia.                         #
# N é resultado de P e Q, sendo ele o valor para a di-#
# visão, que resultara no valor criptografado.        #
# D e E são respectivamente as chaves pública e priva-#
# da.                                                 #
#                                                     #
# Obs. No código, foi invertido as chaves, sendo D pa-#
# ra criptografar e E para descriptografar, assim a v-#
# elocidade de criptografia aumenta consideravelmente.#
#######################################################

class RSA(object):
    __slots__ = ['P','Q','D','E','N','L']

    def __init__(self,P=257,Q=271,D=251):
        self.P = P
        self.Q = Q
        self.D = D
        self.N = P*Q
        self.L = len(hex(self.N))
        z = (self.P-1)*(self.Q-1)
        x = 1
        while (x*self.D)%z != 1:
            x+=1
        self.E = x

    def encode(self, data):
        res = ""
        for x in data:
            res += format((ord(x)**self.D)%self.N,"#0%ix" %(self.L))
        return res

    def decode(self, data):
        res = ""
        data.replace('L','')
        data = [data[x:x+self.L] for x in range(0, len(data), self.L)]
        for x in data:
            res += unichr((int(x,16)**self.E)%self.N)
        return res

msg = """@Memo"""
#Daniel Borges Brumazzi
#Este texto descreve sobre
#um exemplo de código de criptografia
#RSA, criptografando essa frase!
#"""

c = RSA()

#print "Criptografando", msg+"..."

enc = c.encode(msg)
print enc
dec = c.decode(enc)
print dec
