import unittest
from conversor import Numero

class test_conversor(unittest.TestCase):	

	def test_unidades(self):
		z = Numero(0)
		t = Numero(4)
		self.assertEqual(z.escrever(), 'zero')
		self.assertEqual(t.escrever(), 'quatro')

	def test_dezenas(self):
		z = Numero(20)
		t = Numero(43)
		o = Numero(18)
		self.assertEqual(z.escrever(), 'vinte')
		self.assertEqual(t.escrever(), 'quarenta e tres')
		self.assertEqual(o.escrever(), 'dezoito')

	def test_centenas(self):
		z = Numero(100)
		t = Numero(205)
		o = Numero(330)
		q = Numero(555)
		a = Numero(418)
		self.assertEqual(z.escrever(), 'cem')
		self.assertEqual(t.escrever(), 'duzentos e cinco')
		self.assertEqual(o.escrever(), 'trezentos e trinta')
		self.assertEqual(q.escrever(), 'quinhentos e cinquenta e cinco')
		self.assertEqual(a.escrever(), 'quatrocentos e dezoito')

if __name__ == '__main__':
	unittest.main()