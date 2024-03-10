
from contas import Contas
from usuario import Usuario

# * 1 : Definir q e a
q = Contas.gerar_numero_primo(32)
a = Contas.raiz_primitiva(q)

# * 2 : Criar chaves dos usuários
user1 = Usuario("User1", q, a)
user2 = Usuario("User2", q, a)

# * 3 : Troca de chaves públicas entre os usuáris
user1.get_public_key(user2.send_public_key())
user2.get_public_key(user1.send_public_key())

# * 4 : Definir chave secreta
user1.set_secret_key()
user2.set_secret_key()

user1.show_keys()
user2.show_keys()
