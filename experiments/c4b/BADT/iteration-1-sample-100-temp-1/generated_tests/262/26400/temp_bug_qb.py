def original_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a > 6):
	    global_list.append('25')
	else:
	    global_list.append('5')
	return global_list