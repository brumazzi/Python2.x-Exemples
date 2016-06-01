#!/usr/bin/env python
#*-* coding:utf-8 *-*

text = "message"

chars = []

for x in range(len(text)):
    chars.append(ord(text[x]))

out = ""

for x in chars:
    out += str(unichr(x))

print "texto:", text
print "chars:", chars
print "out:",out
