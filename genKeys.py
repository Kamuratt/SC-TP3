import random

# Checa se n é primo a partir de teorema, chegando a resultado probabilístico
def millerRabinTest(n):

    # exp = parte exponencial do teorema
    # Pega (n-1) e divide por 2 até que chegue a um número ímpar
    exp = n - 1
    while not exp & 1:
        exp >>= 1 # divide por 2
    
    # Gera número inteiro aleatório (testemunha de primalidade)
    a = random.randrange(2, n-1)
    # Testa primeira opção do teorema
    if pow(a, exp, n) == 1:
        return True

    # Testa segunda opção do teorema
    while exp < (n-1):
        # Equivalente a checar se é igual a -1
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1 # multiplica por 2 até (n-1)
    
    # Não satisfez o teorema, portanto a é testemunha contra a primalidade de n
    return False



# Seleciona um número primo aleatório com n bits, verificando sua primalidade; Se não for primo, recomeça
def getPrime(n):
    # Primos pequenos podem diminuir a segurança do RSA, logo o range é escolhido com números maiores
    # Como todos os números primos > 2 são ímpares, o número escolhido deve ser ímpar
    prime = random.randrange(2**(n-1)+1, 2**n-1)
    if (prime % 2 == 0): prime -= 1

    # Número de rodadas de Miller Rabin
    for i in range(20):
        # Se número não passa no teste, recomeça
        if not millerRabinTest(prime): return

    return prime


# Gera dupla de primos p e q contendo n bits
def genPrimes(n):
    p = None
    q = None
    while (p == None): p = getPrime(n)
    while (q == None): q = getPrime(n)
    # Garante que p != q
    while (p == q): 
        while (q == None): q = getPrime(n)

    return p, q


def mdcEquals(integer, value):

    return 1


def genKeys():
    # Gera os números primos de 1024 bits p e q, p != q
    p, q = genPrimes(1024)

    n = p * q
    sigma = (p-1) * (q-1)
    e = mdcEquals(sigma, 1)
    d = e**(-1) % sigma

    return (e, n), (d, n)
