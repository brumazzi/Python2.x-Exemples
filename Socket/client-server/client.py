#!/usr/bin/env python
# *-* coding: utf-8 *-*

import socket
import sys

# Configurando socket
s = socket.socket();
host = "127.0.0.1";#socket.gethostnae();
port = 5566;

s.connect((host,port)); # Conecta ao servidor

print s.recv(1024); # Recebe resposta

s.close() # Fecha conexão
