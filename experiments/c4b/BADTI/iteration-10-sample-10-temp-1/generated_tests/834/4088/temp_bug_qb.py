def original_func(*args):
	global_list = []
	
	f = [1, 1]
	n = int(args[0])
	i = 0
	while ((f[0] + f[1]) < n):
	    i += 1
	    (f[0], f[1]) = (f[1], (f[0] + f[1]))
	if (n == 2):
	    i = 1
	if (n == 3):
	    i = 2
	global_list.append(i)
	return global_list