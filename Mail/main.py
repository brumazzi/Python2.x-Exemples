#!/usr/bin/env python
#*-* coding:utf-8 *-*

import smtplib

sender = 'brumazzi_daniel@yahoo.com.br'
receivers = ['wander.lopes@novaandradina.org']#['daniel.brumazzi@novaandradina.org']

message = """From: From Person <%s>
To: To Person <%s>
Subject: SMTP e-mail teste with python

This mail sended with pythom SMTP.
""" %(sender, receivers[0])

server = ['localhost','imap.mail.yahoo.com:25','smtp.mail.yahoo.com']

try:
    mail = smtplib.SMTP(server[0])
    mail.sendmail(sender, receivers, message)
    mail.quit()
    print "Mail sended by success!"
except:
    print "Error to send mail"
