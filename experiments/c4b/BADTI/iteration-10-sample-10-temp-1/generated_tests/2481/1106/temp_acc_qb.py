def patched_func(*args):
	global_list = []
	
	n = (int(args[0]) - 1)
	while (n > 4):
	    n = ((n - 5) >> 1)
	global_list.append(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][n])
	return global_list