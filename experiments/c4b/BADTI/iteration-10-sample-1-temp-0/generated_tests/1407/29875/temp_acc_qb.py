def patched_func(*args):
	global_list = []
	
	(a, b) = map(str, args[0].split())
	global_list.append((int(a) + int(b[::(- 1)])))
	return global_list