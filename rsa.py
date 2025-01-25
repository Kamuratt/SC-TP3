from genKeys import genKeys
from OAEP import oaep_encode, oaep_decode

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod  # Garantir que a base não seja maior que mod
    while exp > 0:
        # Se a expoente for ímpar, multiplicamos o resultado pela base
        if exp % 2 == 1:
            result = (result * base) % mod
        # Expõe a base ao quadrado e reduz a exp pela metade
        exp = exp // 2
        base = (base * base) % mod
    return result

def rsaAlgorithm(m, c1, c2, k):
    if k == "c":
        #Verifica se está sendo feito o processo de codificação

        m = oaep_encode(m, 128)

        print(m)

        C = modular_exponentiation(m, c1, c2)
        
        #Divide a exponenciação para otimizar os cálculos
        
        print(f'Mensagem codificada: {C}')

        return C
    elif k == "d":
        #Verifica se está sendo feito o processo de decodificação

        MD = modular_exponentiation(m, c1, c2)

        print(MD)

        MD = oaep_decode(MD, 128)

        print(MD)
        
        #Divide a exponenciação para otimizar os cálculos
        
        print(f'Mensagem decodificada: {MD}')

        return MD