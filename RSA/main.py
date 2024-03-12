
from usuario import Usuario


# * Criando usuários
user1 = Usuario("Vinicius")
user2 = Usuario("Arthur")
user3 = Usuario("Analaura")

# * Mostrando as chaves
user1.show_keys()
user2.show_keys()
user3.show_keys()

# * Mostrando as conexões
user1.show_connection()
user2.show_connection()
user3.show_connection()

# * Trocanndo as chaves
#   & User1 envia para User2
user2.receiver_public_key(user1.send_user(), user1.send_public_key())
user1.receiver_public_key(user2.send_user(), user2.send_public_key())

# * Mostrando as conexões
user1.show_connection()
user2.show_connection()
user3.show_connection()
