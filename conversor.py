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

	def monta_dezena_2(self):
		dezenas = {'1':'onze', '2':'doze', '3':'treze', '4':'quatorze',\
		'5':'quinze', '6':'dezesseis', '7':'dezesete', '8':'dezoito', '9':'dezenove'}
		return dezenas[self.num[-1]]

	def monta_centena(self):
		centenas = {'1':'cento', '2':'duzentos', '3':'trezentos',
			'4':'quatrocentos', '5':'quinhentos', '6':'seiscentos',
			'7':'setecentos', '8':'oitocentos', '9':'novecentos'}
		return centenas[self.num[-3]]

	def escrever(self):
		# Caso específico num == 0
		if (self.num == '0'):
			return 'zero'
		# Monta unidades 	
		elif (self.n == 1):
			return self.monta_unidade()
		# Monta dezenas	
		elif (self.n == 2):
			# Dezenas COM unidades
			if (self.num[-1] != '0' and self.num[-2] != '1'):
				return self.monta_dezena() + ' e ' + self.monta_unidade()
			# Dezenas caso ONZE
			elif(self.num[-2] == '1'):
				return self.monta_dezena_2()
			# Dezenas SEM unidades 
			return self.monta_dezena()
			# Monta centenas
		elif (self.n == 3):
			# Centenas SEM dezenas e SEM unidade
			if(self.num[-1] == '0' and self.num[-2] == '0'):
				return 'cem'
			# Centena SEM dezena COM unidade
			elif(self.num[-2] == '0'):
				return self.monta_centena() + ' e ' + self.monta_unidade()	
			# Centena COM dezena SEM unidade
			elif(self.num[-1] == '0'):
				return self.monta_centena() + ' e ' + self.monta_dezena()
			# Centa COM dezena ONZE
			elif(self.num[-2] == '1'):
				return self.monta_centena() + ' e ' + self.monta_dezena_2()
			# Centana COM dezena e COM unidade
			return self.monta_centena() + ' e ' + \
				self.monta_dezena() + ' e ' + self.monta_unidade()