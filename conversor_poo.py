# Código que converte número dado da forma numérica
# para a forma extensa; input = 32 output = trinta e dois;

class Numero(object):
	def __init__(self, num):
		self.num = str(num)	
		self.n = len(self.num)

	def monta_unidade(self):
		unidades = {'1':'um', '2':'dois', '3':'tres', '4':'quatro', '5':'cinco',\
		'6':'seis', '7':'sete', '8':'oito', '9':'nove', '0':''}
		return unidades[self.num[-1]]

	def monta_dezena(self):		
		dezenas = {'0':'', '2':'vinte', '3':'trinta', '4':'quarenta',\
		 '5':'cinquenta','6':'sessenta', '7':'setenta', \
		 '8':'oitenta', '9':'noventa'}
		return dezenas[self.num[-2]] 

	def monta_centena(self):
		pass

	def escrever(self):
		if (self.num == '0'):
			return 'zero'
		elif (self.n == 1):
			return self.monta_unidade()
		elif (self.n == 2):
			if (self.num[-1] != '0'):
				return self.monta_dezena() + ' e ' + self.monta_unidade()	
			return self.monta_dezena()


t = Numero(21)
y = Numero(50)
z = Numero(4)
o = Numero(0)

assert t.escrever() == 'vinte e um'
assert y.escrever() == 'cinquenta'	
assert z.escrever() == 'quatro'
assert o.escrever() == 'zero'
