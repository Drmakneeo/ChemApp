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
	print(stoichiometry.baleq(args.equation))

balance_parser = subparsers.add_parser('balance')
balance_parser.add_argument('equation')
balance_parser.set_defaults(func=balance)

if __name__ == '__main__':
	args = parser.parse_args()
	args.func(args)