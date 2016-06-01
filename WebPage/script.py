#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Content-type: text/html\n"

import cgi

form = cgi.FieldStorage()
edit_1 = form["edit_1"].value
#print "sdasdsad"
print "<h1>O valor da caixa de texto é: %s</h1>" %(edit_1)
