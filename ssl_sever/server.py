#!/usr/bin/env python

print "running..."

import socket as sk
import ssl

bs = sk.socket();
bs.bind(('',5000));
bs.listen(5);
ns, fa = bs.accept();

c = ssl.wrap_socket(ns, server_side=True, certfile="cert.pem", keyfile="key.pem", ssl_version=ssl.PROTOCOL_SSLv3);

print c.read();

c.write('200 OK\r\n\r\n');
c.close();

bs.close();

print "Exit"
