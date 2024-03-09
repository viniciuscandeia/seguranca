
# Biblioteca usada: Crypto (pycryptodome)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(message.encode(), AES.block_size))
    return iv + encrypted_data


def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(
        encrypted_message[AES.block_size:]), AES.block_size)
    return decrypted_data.decode()


# Exemplo de uso:
key = get_random_bytes(16)  # Chave de 128 bits (16 bytes)
message = "Mensagem secreta"
encrypted_message = encrypt_message(message, key)
print("Mensagem criptografada: \n", encrypted_message)
decrypted_message = decrypt_message(encrypted_message, key)
print("Mensagem descriptografada:", decrypted_message)


class Usuario:

    # Método para criptografar
    def criptografia(conteduo: str, chave: str):
        print("CRIPTO")

    # Método para descriptografar
    def descriptografia(conteduo: str, chave: str):
        print("DESCRIPTO")


pcVini = Usuario.criptografia("", "")
pcAna = Usuario.descriptografia
