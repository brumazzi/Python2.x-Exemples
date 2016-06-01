#!/usr/bin/env python

import sqlite3
from sqlite3 import *

connect = sqlite3.connect("f.db")
nome="registro01"
reg=((1,'Primeiro','123456'),
     (4,'Quarta','123456'))

ini = connect.cursor()
#ini.execute("create table user (u_cod integer not null, u_nome varchar(30) not null, u_senha varchar(30) not null, primary key(u_cod));")

# este comando adiciona dados a tabela
ini.executemany("insert into user(u_cod,u_nome,u_senha) values(?,?,?);",reg)
#ini.execute()
ini.execute("insert into user(u_cod,u_nome,u_senha) values(2,'Segundo','123456');")
ini.execute("insert into user(u_cod,u_nome,u_senha) values(3,'Terceiro','123456');")

#connect.row_factory = lite_Row
ini.execute("select * from user")

n = ini.fetchall()

for row in n:
	print row

# este comando altera os dados da tabela
ini.execute("update user set u_nome = 'alterado1',u_senha = 'nova00' where u_cod = 1;")

ini.execute("select * from user;")
for row in n:
	print row

#este comando deleta dados da tabela
ini.execute("delete from user where u_cod = 1")

print ini.execute("select * from user;")

ini.execute("select * from user;")
for row in n:
	print row

