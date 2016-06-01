#!/usr/bin/env python
#*-* codgin: utf-8 *-*

def cifer(key, value):
    swap = ''
    value = value.replace(" ",'').upper()
    key = key.replace(" ",'').upper()

    for x in range(len(value)):
        i = ord(value[x])-65
        j = ord(key[x%len(key)])-65
        k = (i+j)%26
        k += 65
        if(x%len(key) == 0): swap += ' '
        swap += str(unichr(k))

    print swap

def decifer(key, value):
    swap = ''
    value = value.replace(" ",'').upper()
    key = key.replace(" ",'').upper()

    for x in range(len(value)):
        i = ord(value[x])-65
        j = ord(key[x%len(key)])-65
        k = (i-j)%26
        k += 65
        if(x%len(key) == 0): swap += ' '
        swap += str(unichr(k))

    print swap

#cifer("galileu","o livro da natureza esta escrito em caracteres matematicos")
cifer("galileu","o livro da natureza esta")
decifer("galileu","YCCQESY SCLZLGN KRPAXEN KMLBTGI Y")
