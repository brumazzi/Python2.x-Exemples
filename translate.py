#!/usr/bin/env python

from string import maketrans

old_order = "abcdefghijklmnopqrstuvwxyz0123456789"
new_order = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0p"

cript = maketrans(old_order, new_order)
decript = maketrans(new_order, old_order)

mess = "mensagem 01 para a criptografia"
mesc = mess.translate(cript)

print mesc
print mesc.translate(decript)
print mesc.translate(decript, '1')
