def patched_func(*args):
	global_list = []
	
	(a, b) = [int(x) for x in args[0].split()]
	if ((a == 0) and (b == 0)):
	    global_list.append('NO')
	elif (abs((a - b)) <= 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list