import base64
from hashlib import sha256
from rsa import rsaAlgorithm

def calcular_hash(mensagem):
    """
    Calcula o hash SHA-256 da mensagem.
    
    :param mensagem: Mensagem em texto.
    :return: Hash da mensagem em formato hexadecimal.
    """
    return sha256(mensagem.encode('utf-8')).hexdigest()

def assinar_arquivo(arquivo_mensagem, chave_privada, n, arquivo_assinado):
    """
    Cria uma assinatura digital da mensagem, lê a mensagem do arquivo,
    concatena o hash criptografado e salva no mesmo arquivo.
    
    :param arquivo_mensagem: Caminho do arquivo contendo a mensagem.
    :param chave_privada: Expoente da chave privada (d).
    :param n: Módulo da chave pública/privada (n).
    :return: Caminho do arquivo com a mensagem e a assinatura salvos.
    """
    # Lê o conteúdo do arquivo
    with open(arquivo_mensagem, 'r') as file:
        mensagem = file.read()
    
    # Calcula o hash da mensagem
    hash_mensagem = calcular_hash(mensagem)
    hash_int = int(hash_mensagem, 16)
    
    # Assina o hash (assinatura = (hash^d) mod n)
    assinatura = rsaAlgorithm(hash_int, chave_privada, n, "c")
    
    # Codifica a assinatura em Base64 para envio
    assinatura_bytes = assinatura.to_bytes((assinatura.bit_length() + 7) // 8, 'big')
    assinatura_base64 = base64.b64encode(assinatura_bytes).decode('utf-8')
    
    # Concatena a mensagem original com a assinatura criptografada
    mensagem_assinada = f"{mensagem}\n{assinatura_base64}"
    
    # Salva a mensagem assinada de volta no mesmo arquivo
    with open(arquivo_assinado, 'w') as file:
        file.write(mensagem_assinada)
    
    # Retorna o caminho do arquivo
    return arquivo_assinado
