def original_func(*args):
	global_list = []
	
	(a, b) = list(map(int, args[0].split()))
	c = max(a, b)
	ans = 0
	for i in range(c):
	    for j in range(c):
	        if ((((i ** 2) + j) == a) and ((i + (j ** 2)) == b)):
	            ans += 1
	global_list.append(ans)
	return global_list