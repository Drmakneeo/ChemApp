def convert(a):
	l = []
	x = {}
	for letter in a:
		l.append(letter)
	for i in range(len(l)):
		if l[i].isupper():
			l1 = []
			l2 = []
			if i==len(l)-1:
				if x.has_key(l[i]):
					x[l[i]] = x[l[i]] + 1
				else:
					x[l[i]] = 1
			elif l[i+1].isupper():
				if x.has_key(l[i]):
					x[l[i]] = x[l[i]] + 1
				else:
					x[l[i]] = 1
			else:
				l1.append(l[i])
		elif l[i].islower():
			l1.append(l[i])
			if i==len(l)-1:
				if x.has_key(''.join(l1)):
					x[''.join(l1)] = x[''.join(l1)] + 1
				else:
					x[''.join(l1)] = 1
			elif l[i+1].isupper():
				if x.has_key(''.join(l1)):
					x[''.join(l1)] = x[''.join(l1)] + 1
				else:
					x[''.join(l1)] = 1
		elif l[i].isdigit():
			l2.append(l[i])
			if i==len(l)-1:
				if x.has_key(''.join(l1)):
					x[''.join(l1)] = x[''.join(l1)] + int(''.join(l2))
				else:
					x[''.join(l1)] = int(''.join(l2))
			elif not l[i+1].isdigit():
				if x.has_key(''.join(l1)):
					x[''.join(l1)] = x[''.join(l1)] + int(''.join(l2))
				else:
					x[''.join(l1)] = int(''.join(l2))
	return x