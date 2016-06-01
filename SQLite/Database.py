#!/usr/bin/env python

import sqlite3

connec = sqlite3.connect("File.db")

_init = connec.cursor()
_init.execute("select * from cliente;")
