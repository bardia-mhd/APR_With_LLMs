def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	week = [int(x) for x in args[1].split()]
	s = sum(week)
	n %= s
	if n:
	    i = 0
	    while (n > week[i]):
	        n -= week[i]
	        i += 1
	    global_list.append((i + 1))
	else:
	    i = 6
	    while ((not week[i]) and (i >= 0)):
	        i -= 1
	    global_list.append((i + 1))
	return global_list