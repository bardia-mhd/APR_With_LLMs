def original_func(*args):
	global_list = []
	
	(n, k) = list(map(int, args[0].split()))
	l = [(i * 5) for i in range(1, (n + 1))]
	count = 0
	global_list.append(l)
	for i in range(0, n):
	    if (sum(l[:(i + 1)]) > (240 - k)):
	        break
	    count += 1
	global_list.append(count)
	return global_list