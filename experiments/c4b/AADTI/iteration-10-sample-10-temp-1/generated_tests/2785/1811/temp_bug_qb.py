def original_func(*args):
	global_list = []
	
	s = args[0].strip()
	c = 0
	if (len(s) > 2):
	    c += s.count('VK')
	    l = s.split('VK')
	    for i in l:
	        if (('VV' in i) or ('KK' in i)):
	            c += 1
	            break
	elif (len(s) == 2):
	    c = 1
	global_list.append(c)
	return global_list