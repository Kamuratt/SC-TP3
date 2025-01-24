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

def mdc(a, b):
    #Verifica o mdc entre dois números
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):

    #Verifica se dois números são coprimos.
    
    return mdc(a, b) == 1

def find_e(phi_n):
    #Encontra o menor 'e' coprimo com phi_n.

    # Começa com um valor comum (65537 é usado frequentemente na prática)
    e = 65537
    # Verifica se e é coprimo com phi_n
    while mdc(e, phi_n) != 1:
        e += 2  # Incrementa para o próximo número ímpar (para eficiência)
    return e

# Função para o Algoritmo Estendido de Euclides
def extended_euclid(a, b):
    #Algoritmo Estendido de Euclides para calcular os coeficientes x e y
    #que satisfazem a * x + b * y = mdc(a, b).
    if b == 0:
        return a, 1, 0  # Caso base: mdc(a, 0) = a
    else:
        mdc, x1, y1 = extended_euclid(b, a % b)  # Passo recursivo
        x = y1
        y = x1 - (a // b) * y1
        return mdc, x, y

# Função para calcular o inverso modular
def modular_inverse(e, phi_n):
    #Calcula o inverso modular de e em relação a phi_n usando o Algoritmo Estendido de Euclides.
    # Usando a função mdc para garantir coprimalidade
    if mdc(e, phi_n) != 1:
        raise ValueError("e e phi_n não são coprimos, inverso modular não existe.")
    
    # Calcula o inverso modular com o Algoritmo Estendido de Euclides
    _, x, _ = extended_euclid(e, phi_n)
    return x % phi_n  # Garante que o resultado seja positivo

def genKeys():
    # Gera os números primos de 1024 bits p e q, p != q
    p, q = genPrimes(1024)

    n = p * q
    sigma = (p-1) * (q-1)
    
    #Escolhe um valor para e(valor default = 65537)
    e = find_e(sigma)

    d = modular_inverse(e, sigma)

    return (e, n), (d, n)
