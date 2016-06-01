from commands import *

out = getstatusoutput

r0 = out('./r0')[0]

r1 = out('./r1')[0]

print 'valor retornado de r0:',r0,'\nvalor retornado de r1:',r1
