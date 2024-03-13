
# * Classe para realizar a troca de mensagens com chave secreta compartilhada

from rsa import RSA


class Usuario:

    def __init__(self, user: str):

        self.rsa = RSA()

        # Nome e chaves do usuário
        self.user: str = user
        self.privateKey = self.rsa.pegar_chave_privada()
        self.publicKey = self.rsa.pegar_chave_publica()

        # Nome e chave pública de outro usuário
        self.secUser: str = ""
        self.secPublicKey: list = []

        # Conectado com outro usuário?
        self.isConnected = False

    # Mostrando as chaves
    def show_keys(self):
        print(f'{self.user:>10} : PRI. KEY : {self.privateKey}')
        print(f'{self.user:>10} : PUB. KEY : {self.publicKey}')

    # Enviar a chave pública
    def send_public_key(self):
        return self.publicKey

    # Enviar o usuário
    def send_user(self):
        return self.user

    # Receber a chave pública do outro usuário
    def receiver_public_key(self, user, publicKey):
        self.secUser = user
        self.secPublicKey = publicKey
        self.isConnected = True

    def show_connection(self):
        if self.isConnected:
            print(f"{self.user:>10} <-> {self.secUser}")
        else:
            print(f"{self.user:>10} <-> X")

    def send_message(self, text):
        print(f'Sou o usuario \033[93m{
              self.user}\033[0m, estou enviando a mensagem ---- {text}')
        if self.isConnected:
            men = self.rsa.criptografar(self.secPublicKey, text)
            return men
        else:
            print('Usuario desconectado')

    def recive_message(self, text):
        print(f'Sou o usuario \033[94m{
              self.user}\033[0m, recebi a mensagem ---- {text}')
        if self.isConnected:
            men = self.rsa.descriptografar(self.privateKey, text)
            print('Mensagem Descriptografada: ---- ', men)
        else:
            print('Usuario desconectado')

