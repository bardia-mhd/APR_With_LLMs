def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	global_list.append(((a - 2) ** 2))
	return global_list