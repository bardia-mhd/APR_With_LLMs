def original_func(*args):
	global_list = []
	
	x1 = args[0].split()
	x2 = args[1].split()
	x3 = args[2].split()
	x4 = args[3].split()
	x5 = args[4].split()
	lst = ['0', '0', '0', '0', '0']
	i = 0
	for i in range(5):
	    if ((x1[i] != lst[i]) or (x5[i] != lst[i])):
	        if ((i == 0) or (i == 4)):
	            z = 4
	        elif ((i == 1) or (1 == 3)):
	            z = 3
	        else:
	            z = 2
	    elif ((x2[i] != lst[i]) or (x4[i] != lst[i])):
	        if ((i == 0) or (i == 4)):
	            z = 3
	        elif ((i == 1) or (1 == 3)):
	            z = 2
	        else:
	            z = 1
	    elif (x3[i] != lst[i]):
	        if ((i == 0) or (i == 4)):
	            z = 2
	        elif ((i == 1) or (1 == 3)):
	            z = 1
	        else:
	            z = 0
	    i += 1
	global_list.append(z)
	return global_list