#!/usr/bin/env python
#*-* coding:utf-8 *-*

msg = "Mensagem para ser desmenbrada!"

max = 6

vec = [msg[x:x+max] for x in range(0, len(msg), max) ]

for x in vec:
    print x
