def patched_func(*args):
	global_list = []
	
	name = args[0]
	chars = set(name)
	if ((len(chars) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list