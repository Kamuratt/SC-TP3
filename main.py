from Assinatura import assinar_mensagem
from Verificaçao import verificar_assinatura
from genKeys import genKeys

m = "Amigos, o código está pronto!! Colocarei tudo no GitHub agora. Testem caso queiram. Beijos S2"

chaves_publicas, chaves_privadas = genKeys()

mensagem, mensagem_assinada = assinar_mensagem(m, chaves_privadas[0], chaves_privadas[1])

mensagem, verificacao = verificar_assinatura(m, mensagem_assinada, chaves_publicas[0], chaves_publicas[1])

if verificacao == True and mensagem:
    print(f"Mensagem verificada e segura. Mensagem recebida: {mensagem}")
else:
    print("Foi verificada uma alteração na mensagem.")  