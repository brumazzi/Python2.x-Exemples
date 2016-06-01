#!/usr/bin/python
# *-* coding:utf-8 *-*

import socket
import send_data as sd

DIR_FILES = "/home/brumazzi/Público/"
LOOP = True

s = socket.socket()

s.bind(('127.0.0.1',5566))

while LOOP:
    conn, addr = s.accept()
    action = conn.recv(1)
    if action == '1':
        sd.send_file(conn, addr)

s.close()
