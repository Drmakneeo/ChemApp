from math import log10

def ph_from_hydronium(a):
	return -1 * log10(a)

def ph_from_hydroxide(a):
	return 14 + log10(a)