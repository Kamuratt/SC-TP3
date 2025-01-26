from Assinatura import assinar_mensagem
from Verificaçao import verificar_assinatura
from genKeys import genKeys

mensagem = "Eu sou linda, sou gostosa, mas eu sofro pra caralho. As bonitas também sofrem, tô sem grana pra gastar. Eu só pego cara duro, então tenho que trabalhar. Eu sou foda pra caralho e ainda vou ser popstar."

chaves_publicas, chaves_privadas = genKeys()

mensagem, mensagem_assinada = assinar_mensagem(mensagem, chaves_privadas[0], chaves_privadas[1])

mensagem, verificacao = verificar_assinatura(mensagem, mensagem_assinada, chaves_publicas[0], chaves_publicas[1])

if verificacao == True and mensagem:
    print(f"Mensagem verificada e segura. Mensagem recebida: {mensagem}")
else:
    print("Foi verificada uma alteração na mensagem.")  