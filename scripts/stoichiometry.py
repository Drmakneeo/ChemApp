import pint
ureg = pint.UnitRegistry()

import json

def molmass(a):
	with open('../resources/element_data.json') as data_file:
		data = json.load(data_file)

	mm = 0
	keys = a.keys()
	for i in range(len(a)):
		for n in range(0,118):
			if data["elements"][n]["symbol"] == keys[i]:
				mm = mm + ( a[keys[i]] * data["elements"][n]["molar-mass"] )
				break
	mm = mm * ureg.gram / ureg.mol
	return mm