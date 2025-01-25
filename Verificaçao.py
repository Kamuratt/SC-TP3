import base64
from Assinatura import calcular_hash
from rsa import rsaAlgorithm
def verificar_assinatura(mensagem, assinatura_base64, chave_publica, n):
    """
    Verifica a assinatura da mensagem.
    
    :param mensagem: Mensagem em texto.
    :param assinatura_base64: Assinatura codificada em Base64.
    :param chave_publica: Expoente da chave pública (e).
    :param n: Módulo da chave pública/privada (n).
    :return: True se a assinatura for válida, False caso contrário.
    """
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
        return mensagem, True
    else:
        return "", False
