def original_func(*args):
	global_list = []
	
	a = str(args[0])
	length = len(a)
	count = 0
	if (a[0].islower() == True):
	    count = 1
	for i in range(length):
	    if (a[i].isupper() == True):
	        count = 1
	    elif ((a[i].islower() == True) and (i != 0)):
	        count = 2
	        global_list.append(a)
	        exit()
	if (count == 2):
	    global_list.append(a)
	elif (count == 1):
	    b = a.lower()
	    b = b.capitalize()
	    global_list.append(b)
	return global_list