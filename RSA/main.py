
from usuario import Usuario
import time

# * Criando usuários
user1 = Usuario("Vinicius")
user2 = Usuario("Arthur")

# * Mostrando as chaves
# user1.show_keys()
# user2.show_keys()

# * Mostrando as conexões
# user1.show_connection()
# user2.show_connection()

# * Trocanndo as chaves
#   & User1 envia para User2
user2.receiver_public_key(user1.send_user(), user1.send_public_key())
user1.receiver_public_key(user2.send_user(), user2.send_public_key())

mensagens = ['Ola', 'Como voce vai?', 'Vou bem e voce?', 'Vou bem tambem',
             'Que bom!', 'Gostou da prova hoje?', 'Prefiro nao falar sobre kkkk']

flag = False

print("=" * 100)
for i in mensagens:

    if (flag):

        men = user1.send_message(i)
        time.sleep(1)
        user2.recive_message(men)

        flag = False

    else:
        men = user2.send_message(i)
        time.sleep(1)
        user1.recive_message(men)

        flag = True

    print("=" * 100)
