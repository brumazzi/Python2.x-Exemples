#!/usr/bin/env python
# -*- coding:utf-8 -*-

import marshal as ms

lista = [1,8,3,'texto']

msg = ms.dumps(lista)
print msg
msg = ms.loads(msg)
print msg
