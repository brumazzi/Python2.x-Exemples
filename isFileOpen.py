import commands

output = commands.getoutput('ps -A')
file = raw_input("Arquivo a ser procurado: ")

if str(file) in output:
	print file,'est\xc3\xa1 em execu\xc3\xa7\xc3\xa3o.'
else:
	print file,'n\xc3\xa3o encontrado.'
