#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mysql

con = mysql.connect("127.0.0.1","root","root")
con.select_db("local");

cursor = con.cursor()

cursor.execute("select * from data");
datas = cursor.fetchall()

print datas
