def original_func(*args):
	global_list = []
	
	a = int(args[0])
	
	def f(a):
	    if ((a % 2) == 0):
	        return 'YES'
	    return 'NO'
	global_list.append(f(a))
	return global_list