
# * Classe para realizar as operações matemáticas necessárias para as chaves

from sympy import primitive_root, isprime
import random
import sympy


class Contas:

    # Gerar número primo (aleatório) -> q
    @staticmethod
    def gerar_numero_primo(bits):
        while True:
            # Gerar um número aleatório com o número de bits especificado
            num = random.getrandbits(bits)

            # Garantir que o número gerado tenha o bit mais significativo e o bit menos significativo definidos
            num |= (1 << bits - 1) | 1

            # Verificar se o número é primo usando a função isprime da biblioteca sympy
            if isprime(num):
                return num

    # Encontrar raiz primitiva -> a
    @staticmethod
    def raiz_primitiva(q: int):
        return primitive_root(q)

    # Definir chave privada -> X
    @staticmethod
    def valor_chave_privada(numero_primo: int):
        return random.randint(1, numero_primo - 1)

    # Definir chave pública -> Y
    @staticmethod
    def valor_chave_publica(a: int, x: int, q: int):
        return pow(a, x, q)

    # Definir chave secreta -> K
    @staticmethod
    def chave_secreta(y: int, x: int, q: int):
        return pow(y, x, q)
