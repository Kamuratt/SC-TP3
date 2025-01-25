<<<<<<< Updated upstream
from genKeys import genKeys
=======
from OAEP import oaep_encode, oaep_decode
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        
=======

        m = oaep_encode(m, 128)
        #Realiza o OEAP     
    
>>>>>>> Stashed changes
        C = modular_exponentiation(m, c1, c2)
        #Divide a exponenciação para otimizar os cálculos
        
        return C
    elif k == "d":
        #Verifica se está sendo feito o processo de decodificação
        
        MD = modular_exponentiation(m, c1, c2)
<<<<<<< Updated upstream
        
        #Divide a exponenciação para otimizar os cálculos
        
        print(f'Mensagem decodificada: {MD}')

        return MD

m = 754789874985498547985498549854784985954798549854985498598454989595498562554985498515652123564564231564532154798456415649844189848498478884698498468468478446846846846845346845684846846846846846846846846846845643515616879845619874984123549848

chaves_codificacao, chaves_decodificacao = genKeys()

mensagem_decodificada = rsaAlgorithm(rsaAlgorithm(m, chaves_codificacao[0], chaves_codificacao[1], "c"), chaves_decodificacao[0], chaves_decodificacao[1], "d")

if m == int(mensagem_decodificada):
    print("Mensagem em claro é igual a mensagem decodificada, o que é esperado.")
else:
    print("Mensagem em claro é diferente a mensagem decodificada, o que demonstra que há algum erro no RSA.")
=======
        #Divide a exponenciação para otimizar os cálculos

        MD = oaep_decode(MD, 128)
        #Realiza o OEAP
        
        return MD
>>>>>>> Stashed changes
