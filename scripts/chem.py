import pint
ureg = pint.UnitRegistry()

import json
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

import input_chemical
import stoichiometry

def molar_mass(args):
	print(stoichiometry.molmass(input_chemical.convert(args.chemical)))

molar_mass_parser = subparsers.add_parser('molar_mass')
molar_mass_parser.add_argument('chemical')
molar_mass_parser.set_defaults(func=molar_mass)

def balance(args):
	r = []
	p = []
	for i in range(len(args.reactants)):
		print(input_chemical.convert(args.reactants[i]))
		r.append(input_chemical.convert(args.reactants[i]))
	for i in range(len(args.products)):
		print(input_chemical.convert(args.products[i]))
		p.append(input_chemical.convert(args.products[i]))
	
	c = stoichiometry.baleq(r,p)
	out = []
	for i in range(len(args.reactants)):
		out.append(c[i])
		out.append('*')
		out.append(args.reactants[i])
		if not i == len(args.reactants):
			out.append(' + ')
	out.append(' --> ')
	for i in range(len(args.products)):
		out.append(c[i+len(args.reactants)])
		out.append('*')
		out.append(args.products[i])
		if not i == len(args.products):
			out.append(' + ')
	print(''.join(out))

balance_parser = subparsers.add_parser('balance')
balance_parser.add_argument('--r', dest='reactants', action='append')
balance_parser.add_argument('--p', dest='products', action='append')
balance_parser.set_defaults(func=balance)

if __name__ == '__main__':
	args = parser.parse_args()
	args.func(args)