import hashlib
import base64
from rsa import rsaAlgorithm

def calcular_hash(mensagem):
    """
    Calcula o hash da mensagem usando SHA-3 (256 bits).
    
    :param mensagem: Mensagem em texto.
    :return: Hash da mensagem como string hexadecimal.
    """
    sha3 = hashlib.sha3_256()
    sha3.update(mensagem.encode('utf-8'))
    return sha3.hexdigest()

def assinar_mensagem(mensagem, chave_privada, n):
    """
    Assina a mensagem cifrando o hash com a chave privada.
    
    :param mensagem: Mensagem em texto.
    :param chave_privada: Expoente da chave privada (d).
    :param n: Módulo da chave pública/privada (n).
    :return: Assinatura codificada em Base64.
    """
    # Calcula o hash da mensagem
    hash_mensagem = calcular_hash(mensagem)
    # Converte o hash para inteiro
    hash_int = int(hash_mensagem, 16)
    # Cifra o hash com a chave privada: assinatura = (hash^d) mod n
    assinatura = rsaAlgorithm(hash_int, chave_privada, n, "c")
    # Converte a assinatura para Base64
    assinatura_base64 = base64.b64encode(assinatura.to_bytes((assinatura.bit_length() + 7) // 8, 'big')).decode('utf-8')
    return mensagem, assinatura_base64