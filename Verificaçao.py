import base64
from Assinatura import calcular_hash
from rsa import rsaAlgorithm

def verificar_assinatura(arquivo_mensagem_assinada, chave_publica, n):
    """
    Verifica a assinatura digital da mensagem, lendo o conteúdo do arquivo com a mensagem e assinatura.
    
    :param arquivo_mensagem_assinada: Caminho do arquivo com a mensagem e a assinatura concatenada.
    :param chave_publica: Expoente da chave pública (e).
    :param n: Módulo da chave pública/privada (n).
    :return: True se a assinatura for válida, False caso contrário.
    """
    # Lê o conteúdo do arquivo
    with open(arquivo_mensagem_assinada, 'r') as file:
        mensagem_com_assinatura = file.read()
    
    # Separa a mensagem da assinatura (espera-se que a assinatura esteja na última linha)
    mensagem, assinatura_base64 = mensagem_com_assinatura.rsplit('\n', 1)
    
    # Decodifica a assinatura de Base64 para inteiro
    assinatura_bytes = base64.b64decode(assinatura_base64.encode('utf-8'))
    assinatura = int.from_bytes(assinatura_bytes, 'big')
    
    # Decifra o hash da assinatura: hash_decifrado = (assinatura^e) mod n
    hash_decifrado = rsaAlgorithm(assinatura, chave_publica, n, "d")
    
    # Recalcula o hash da mensagem original
    hash_mensagem = calcular_hash(mensagem)
    hash_mensagem_int = int(hash_mensagem, 16)
    
    # Compara os hashes
    if hash_decifrado == hash_mensagem_int:
        return True  # A assinatura é válida
    else:
        return False  # A assinatura é inválida
