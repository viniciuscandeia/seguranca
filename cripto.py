
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


class Cripto:

    def criptografar(mensagem, chave):
        # Certifique-se de que a mensagem é um múltiplo de 16 bytes (bloco AES)
        padded_message = pad(mensagem.encode(), AES.block_size)

        # Inicialize o objeto AES com a chave fornecida
        cipher = AES.new(chave, AES.MODE_CBC)

        # Criptografe a mensagem
        ciphertext = cipher.encrypt(padded_message)

        # Retorna o texto cifrado e o vetor de inicialização (IV) para uso posterior durante a descriptografia
        return ciphertext, cipher.iv

    def descriptografar(ciphertext, key, iv):
        # Inicialize o objeto AES com a chave e o IV fornecidos
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Descriptografe a mensagem
        decrypted_message = cipher.decrypt(ciphertext)

        # Remova o preenchimento da mensagem
        unpadded_message = unpad(decrypted_message, AES.block_size)

        # Retorna a mensagem descriptografada
        return unpadded_message.decode()


# Exemplo de uso
mensagem = "Esta é uma mensagem secreta!"
# Sua chave secreta compartilhada, deve ter 16, 24 ou 32 bytes
chave = b"1234567890123456"

cifrado, iv = Cripto.criptografar(mensagem, chave)
print("Texto cifrado:", cifrado)
print("Vetor de inicialização (IV):", iv)

# Exemplo de uso
mensagem_descriptografada = Cripto.descriptografar(cifrado, chave, iv)
print("Mensagem descriptografada:", mensagem_descriptografada)
