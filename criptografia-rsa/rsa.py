#!/usr/bin/env python
#*-* coding:utf-8 *-*

class RSA(object):
    def encode(self, str):
        swap = []
        for x in str:
            swap.append(unichr((ord(x)**23)%187))
        res = ''
        for x in swap:
            res += x
        return res

    def decode(self, str):
        swap = []
        for x in str:
            swap.append(unichr((ord(x)**7)%187))
        res = ''
        for x in swap:
            res += x
        return res

rsa = RSA()

nome = raw_input("palavra: ")
enc = rsa.encode(nome)
dec = rsa.decode(enc)

print "nome normal:",nome
print "nome criptografado:",enc.encode("utf-8")
print "nome descriptografado:",dec
