from Assinatura import assinar_mensagem
from Verificaçao import verificar_assinatura
from genKeys import genKeys

m = "Como o dia está lindo!!"

chaves_publicas, chaves_privadas = genKeys()

mensagem, mensagem_assinada= assinar_mensagem(m, chaves_privadas[0], chaves_privadas[1])

mensagem, mensagem_segura = verificar_assinatura(mensagem, mensagem_assinada, chaves_publicas[0], chaves_publicas[1])

if mensagem_segura == True:
    print(f"Mensagem verificada e segura. Mensagem recebida: {mensagem}")
else:
    print("Foi verificada uma alteração na mensagem.")



