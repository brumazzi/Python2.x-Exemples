#!/usr/bin/env python
#*-* coding:utf-8 *-*

import socket
import sys

END_SERVER = False
F = None

# configurando Socket
s = socket.socket();
host = "127.0.0.1"; #socket.gethostname();
port = 5566;

# Liga porta ao host
s.bind((host,port));

# espera cliente
s.listen(5);

try:
    c, addr = s.accept(); # Estabelece a conexão (retorna um vetor)
    print "Conectado pelo cliente ",addr;
    c.send("Conectado com sucesso!"); # Retorna ao cliente
    c.close()   #fecha a conexão
except:
    print "Erro de conexão."

s.close()
