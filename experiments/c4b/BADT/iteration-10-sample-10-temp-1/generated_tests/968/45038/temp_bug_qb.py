def original_func(*args):
	global_list = []
	
	import math
	(m, d) = map(int, args[0].split())
	if ((m < 8) and ((m % 2) == 1)):
	    c = 31
	elif (m < 8):
	    c = 30
	elif ((m >= 8) and ((m % 2) == 0)):
	    c = 31
	else:
	    c = 30
	l = (8 - d)
	c -= l
	global_list.append((math.ceil((c / 7)) + 1))
	return global_list