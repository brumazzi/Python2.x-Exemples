def total_lines(file):
	file.seek(0)
	lines = 0
	ss = ""
	while(True):
		ss = file.readline()
		if ss == '':
			break
		else:
			lines += 1
	
	return lines
