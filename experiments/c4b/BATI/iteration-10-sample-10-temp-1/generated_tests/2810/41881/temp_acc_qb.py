def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	global_list.append(int(((a - 1) / 2)))
	return global_list