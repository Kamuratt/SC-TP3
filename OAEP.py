import os
from hashlib import sha3_256

# Função para converter um inteiro para bytes
def int_to_bytes(x, length):
    return x.to_bytes(length, byteorder="big")

# Função para converter bytes para um inteiro
def bytes_to_int(b):
    return int.from_bytes(b, byteorder="big")

# Função para aplicar OAEP
def oaep_encode(message_int, k, h_len=32):
    """
    Aplica o OAEP (Optimal Asymmetric Encryption Padding) a um número inteiro com SHA3-256.

    :param message_int: Mensagem a ser cifrada (como inteiro).
    :param k: Tamanho do bloco de dados (em bytes).
    :param h_len: Comprimento do hash (SHA3-256 tem 32 bytes).
    :return: Mensagem cifrada com OAEP (como inteiro).
    """
    # Converter o número inteiro para bytes
    message = int_to_bytes(message_int, (message_int.bit_length() + 7) // 8)

    m_len = len(message)
    padding_length = k - m_len - 2 * h_len - 2

    if padding_length < 0:
        raise ValueError("Mensagem muito longa para o tamanho do bloco especificado.")

    # 1. Gerar o padding necessário
    padding = b'\x00' * padding_length

    # 2. Construir a mensagem com o padding e delimitador
    data_block = b'\x00' + padding + b'\x01' + message

    # 3. Gerar o hash do label (normalmente uma string vazia)
    label_hash = sha3_256(b'').digest()

    # 4. Concatenar o hash do label com o bloco de dados
    data_block = label_hash + data_block

    # 5. Gerar o seed aleatório
    seed = os.urandom(h_len)

    # 6. Gerar a máscara para o bloco de dados usando SHA3-256
    db_mask = sha3_256(seed).digest() * (len(data_block) // h_len + 1)
    db_mask = db_mask[:len(data_block)]

    # 7. Aplicar o XOR para mascarar o bloco de dados
    masked_db = bytes([data_block[i] ^ db_mask[i] for i in range(len(data_block))])

    # 8. Gerar a máscara para o seed usando o bloco de dados mascarado
    seed_mask = sha3_256(masked_db).digest() * (len(seed) // h_len + 1)
    seed_mask = seed_mask[:len(seed)]

    # 9. Aplicar o XOR para mascarar o seed
    masked_seed = bytes([seed[i] ^ seed_mask[i] for i in range(len(seed))])

    # 10. Concatenar o seed mascarado e o bloco de dados mascarado
    encoded_message = masked_seed + masked_db

    # Converter o resultado para inteiro antes de retornar
    return bytes_to_int(encoded_message)

# Função para descriptografar OAEP
def oaep_decode(encoded_message_int, k, h_len=32):
    """
    Simula a descriptografia da mensagem cifrada com OAEP com SHA3-256.

    :param encoded_message_int: Mensagem cifrada com OAEP (como inteiro).
    :param k: Tamanho do bloco de dados (em bytes).
    :param h_len: Comprimento do hash (SHA3-256 tem 32 bytes).
    :return: Mensagem decodificada como inteiro.
    """
    # Converter o número inteiro para bytes
    encoded_message = int_to_bytes(encoded_message_int, k)

    # 1. Separar seed mascarado e bloco de dados mascarado
    masked_seed = encoded_message[:h_len]
    masked_db = encoded_message[h_len:]

    # 2. Gerar a máscara para o seed usando o bloco de dados mascarado
    seed_mask = sha3_256(masked_db).digest() * (len(masked_seed) // h_len + 1)
    seed_mask = seed_mask[:len(masked_seed)]

    # 3. Reverter o XOR para recuperar o seed original
    seed = bytes([masked_seed[i] ^ seed_mask[i] for i in range(len(masked_seed))])

    # 4. Gerar a máscara para o bloco de dados usando o seed original
    db_mask = sha3_256(seed).digest() * (len(masked_db) // h_len + 1)
    db_mask = db_mask[:len(masked_db)]

    # 5. Reverter o XOR para recuperar o bloco de dados original
    data_block = bytes([masked_db[i] ^ db_mask[i] for i in range(len(masked_db))])

    # 6. Separar o hash do label e a mensagem preenchida
    label_hash = data_block[:h_len]
    message_with_padding = data_block[h_len:]

    # 7. Verificar o hash do label (deve ser igual ao hash de uma string vazia)
    if label_hash != sha3_256(b'').digest():
        raise ValueError("Hash do label inválido.")

    # 8. Remover o padding
    if b'\x01' not in message_with_padding:
        raise ValueError("Delimitador de padding não encontrado.")

    _, message = message_with_padding.split(b'\x01', 1)

    # Converter a mensagem de volta para um inteiro
    return bytes_to_int(message)

# Testando OAEP com inteiros
message_int = 123456789012345678901234567890
k = 256  # Tamanho do bloco de dados (em bytes)

# Codificando a mensagem
encoded_message_int = oaep_encode(message_int, k)
print("Mensagem codificada (inteiro):", encoded_message_int)

# Decodificando a mensagem
decoded_message_int = oaep_decode(encoded_message_int, k)
print("Mensagem decodificada (inteiro):", decoded_message_int)

