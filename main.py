
from sympy import primitive_root
import random
import sympy

# * Classe para realizar as operações matemáticas necessárias para a criptografia


class Contas:

    # Gerar número primo (aleatório)
    def gerar_numero_primo(bits):

        while True:
            # Gerar um número aleatório com o número de bits especificado
            num = random.getrandbits(bits)

            # Garantir que o número gerado tenha o bit mais significativo e o bit menos significativo definidos
            num |= (1 << bits - 1) | 1

            # Verificar se o número é primo usando a função isprime da biblioteca sympy
            if sympy.isprime(num):
                return num

    # Encontrar raiz primitiva
    def raiz_primitiva(n):
        return primitive_root(n)

    # Definir X




class Usuario:

    # Método para criptografar
    def criptografia(conteduo: str, chave: str):
        print("CRIPTO")

    # Método para descriptografar
    def descriptografia(conteduo: str, chave: str):
        print("DESCRIPTO")


pcVini = Usuario.criptografia("", "")
pcAna = Usuario.descriptografia
