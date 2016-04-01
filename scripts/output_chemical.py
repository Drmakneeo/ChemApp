def convert(a):
	out = []
	keys = a.keys()
	values = a.values()
	for i in range(len(keys)):
		out.append(keys[i])
		out.append(str(values[i]))
	return ''.join(out)