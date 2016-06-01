#!/usr/bin/env python
# *-* coding:utf-8 *-*

import sys
from sys import argv

file = None

try:
    file = open(argv[1],"r")
except:
    print "Erro de entrada de arquivo"
    sys.exit(1)

chars = {
    u'á':'\\\'a',
    u'é':'\\\'e',
    u'í':'\\\'i',
    u'ó':'\\\'o',
    u'ú':'\\\'u',
    u'ç':'\\c{c}',
    u'ã':'\\~a',
    u'ẽ':'\\~e',
    u'ĩ':'\\~i',
    u'õ':'\\~o',
    u'ũ':'\\~u',
    u'â':'\\^a',
    u'ê':'\\^e',
    u'î':'\\^i',
    u'ô':'\\^o',
    u'û':'\\^u',
    u'à':'\\`a',
    u'è':'\\`e',
    u'ì':'\\`i',
    u'ò':'\\`o',
    u'ù':'\\`u',
    u'Á':'\\\'A',
    u'É':'\\\'E',
    u'Í':'\\\'I',
    u'Ó':'\\\'O',
    u'Ú':'\\\'U',
    u'Ç':'\\c{C}',
    u'Ã':'\\~A',
    u'Ẽ':'\\~E',
    u'Ĩ':'\\~I',
    u'Õ':'\\~O',
    u'Ũ':'\\~U',
    u'Â':'\\^A',
    u'Ê':'\\^E',
    u'Î':'\\^I',
    u'Ô':'\\^O',
    u'Û':'\\^U',
    u'À':'\\`A',
    u'È':'\\`E',
    u'Ì':'\\`I',
    u'Ò':'\\`O',
    u'Ù':'\\`U',
}

string = unicode(file.read(), "utf-8")

for x in chars:
    string = string.replace(u"%s" %(x), chars[x])

print string,
