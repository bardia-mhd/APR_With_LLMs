def patched_func(*args):
	global_list = []
	
	s = args[0]
	a = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        a += 1
	if ((a == 4) or (a == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list