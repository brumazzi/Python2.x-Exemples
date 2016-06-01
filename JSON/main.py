#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

lista = [1,2,3,'texto',{'str':5}]

msg = json.dumps(lista)
print msg

msg = json.loads(msg)
print msg

print msg[3],msg[4]['str']
