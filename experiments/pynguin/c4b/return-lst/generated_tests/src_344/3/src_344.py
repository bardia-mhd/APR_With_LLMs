def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    exit()
	if (abs((a - b)) <= 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values