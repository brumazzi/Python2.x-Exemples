#!/usr/bin/env python

from socket import socket as sk
import ssl
s = sk();

c = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_SSLv3, ca_certs='ca.pem');

s.connect(('www.google.com.br',443))

cert = c.getpeercert();
if not cert or ('commonName', u'www.google.com.br') not in cert['subject'][4]:
    #raise Exception("Danger!");
    print "Danger!"

s.write("GET / \n");
s.close()
