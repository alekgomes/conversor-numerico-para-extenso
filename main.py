#!/usr/bin/env python3

import argparse
import sys
import unittest
from conversor import Numero

def main():
	parser = argparse.ArgumentParser(description='Converte números para sua forma extensa em português')
	parser.add_argument('numero', type=int, nargs='?', help='Número a ser convertido (0-999)')
	parser.add_argument('--test', action='store_true', help='Executa os testes')
	
	args = parser.parse_args()
	
	if args.test:
		unittest.main(module='test_conversor', argv=[''], exit=False)
	elif args.numero is not None:
		if 0 <= args.numero <= 999:
			conversor = Numero(args.numero)
			print(conversor.escrever())
		else:
			print("Erro: O número deve estar entre 0 e 999", file=sys.stderr)
			sys.exit(1)
	else:
		parser.print_help()

if __name__ == '__main__':
	main()