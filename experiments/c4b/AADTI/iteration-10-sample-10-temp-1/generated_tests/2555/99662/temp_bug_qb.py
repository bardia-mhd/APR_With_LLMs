def original_func(*args):
	global_list = []
	
	mas = args[0]
	if ((mas.count('1111111') > 1) or mas.count('0000000')):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list