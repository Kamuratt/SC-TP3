from Assinatura import assinar_arquivo
from Verificaçao import verificar_assinatura
from genKeys import genKeys

mensagem = "./Mensagem.txt"

chaves_publicas, chaves_privadas = genKeys()

arquivo_assinado = assinar_arquivo(mensagem, chaves_privadas[0], chaves_privadas[1], "./Mensagem Assinada.txt")

verificacao = verificar_assinatura(arquivo_assinado, chaves_publicas[0], chaves_publicas[1])

if verificacao == True:
    # Abre o arquivo com a codificação correta (utf-8)
    with open(mensagem, 'r', encoding='utf-8') as file:
        mensagem_lida = file.read()  # Lê todo o conteúdo do arquivo
    
    print(f"Mensagem verificada e segura. Mensagem recebida: {mensagem_lida}")
else:
    print("Foi verificada uma alteração na mensagem.")

