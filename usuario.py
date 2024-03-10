
# * Classe para realizar a troca de mensagens com chave secreta compartilhada

from contas import Contas


class Usuario:

    def __init__(self, user: str, q: int, a: int):

        self.user: str = user
        self.x: int = Contas.valor_chave_privada(q)
        self.ya: int = Contas.valor_chave_publica(a, self.x, q)
        self.yb: int = 0
        self.k: int = 0

        self.q: int = q
        self.a: int = a

    # Mostrando as chavers

    def show_keys(self):
        print(f'{self.user} : X  : {self.x}')
        print(f'{self.user} : YA : {self.ya}')
        print(f'{self.user} : YB : {self.yb}')
        print(f'{self.user} : Y  : {self.k}')

    # Enviar a chave pública
    def send_public_key(self):
        return self.ya

    # Receber a chave pública do outro usuário
    def get_public_key(self, yb):
        self.yb = yb

    # Definir a chave secreta
    def set_secret_key(self):
        self.k = Contas.chave_secreta(self.yb, self.x, self.q)
