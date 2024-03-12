from sympy import gcd, isprime
import random


class RSA:

	def __init__(self):
		self.bits = 32
		self.p, self.q = self.selecionar_primos()
		self.n = self.p * self.q
		self.phi = (self.p - 1) * (self.q - 1)  # Corrigido o cálculo de phi
		self.e = self.escolher_e(self.phi)
		self.d = self.modular_inverse(self.e, self.phi)

	def gerar_numero_primo(self):
		while True:
			num = random.getrandbits(self.bits)
			num |= (1 << self.bits - 1) | 1
			if isprime(num):
				return num

	# * Selecionar P e Q
	def selecionar_primos(self):
		num1, num2 = 0, 0
		while num1 == num2:
			num1 = self.gerar_numero_primo()
			num2 = self.gerar_numero_primo()
		return num1, num2

	# * Escolher E
	def escolher_e(self, phi: int):
		while True:
			e = random.randint(2, phi - 1)
			if gcd(phi, e) == 1:
				return e

	# * Calcular D (1/2)
	# # TRANSFORMAR EM ITERATIVO
	def extended_gcd(self, a: int, b: int):
		if b == 0:
			return a, 1, 0
		else:
			g, x, y = self.extended_gcd(b, a % b)
			return g, y, x - (a // b) * y

	# * Calcular D (2/2)
	def modular_inverse(self, e: int, phi: int):
		g, x, y = self.extended_gcd(e, phi)
		if g != 1:
			raise Exception('O inverso modular não existe')
		else:
			return x % phi

	def pegar_chave_publica(self):
		return [self.e, self.n]

	def pegar_chave_privada(self):
		return [self.d, self.n]

	def criptografar(self, chavePublica: list, mensagem):
		e: int = chavePublica[0]
		n: int = chavePublica[1]
		criptografado = [pow(ord(char), e, n) for char in mensagem]
		return criptografado

	def descriptografar(self, chavePrivada: list, mensagem):
		e: int = chavePrivada[0]
		d: int = chavePrivada[1]
		descriptografado = ''.join([chr(pow(char, d, n)) for char in mensagem])
		return descriptografado
