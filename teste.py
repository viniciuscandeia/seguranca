import sympy


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y


def modular_inverse(e, phi_n):
    g, x, y = extended_gcd(e, phi_n)
    if g != 1:
        raise Exception('O inverso modular não existe')
    else:
        return x % phi_n


# Exemplo de uso
e = 7  # Substitua pelo valor de e que você tem
phi_n = 160  # Substitua pelo valor de pi(n) que você tem

d = modular_inverse(e, phi_n)
print("d calculado:", d)
