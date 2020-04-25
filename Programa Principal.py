import bibSenha, time

print("Olá Campeã(o), Bom... Espero que seja 😂")
print("Este é um jogo de cores, cuja finalidade é acertar as senhas geradas pela máquina e para isso você contará com 8 chances.")
print("Vamos às regras: \n 😎")
print(" → Você pode escolher 4 cores em um total de 6 cores (seja criativo e não as repita 😉). ")
print(" → Você pode fazer pontos de duas maneiras: Acertando as cores e posições (Acertos Totais) ou apenas acertando as cores (Acertos Parciais).")
print(" → Dito isto, cada Acerto Total concede 7 pontos e cada Acerto Parcial concede 3 pontos.")
print(" → Vamos começar !!!")

cores_totais = ["Vermelho", "Verde", "Branco", "Amarelo", "Azul", "Preto"]
cores_na_senha = 4
chances = 8

senha = bibSenha.GerarSenha()

pontuacao = 0
senha_jogador = []
chance_atual = 1

print()

#While utilizado em cada rodada enquanto o jogador não ganhar e não acabar suas chances

while( chance_atual <= chances ) and ( bibSenha.TestarVitoria(senha, senha_jogador) == False ):
    print(f"Rodada: {chance_atual} / {chances}")
    contador = 1

#While para pedir o palpite do jogador
    while( contador <= cores_na_senha ):
        print("Cores Disponíveis:")
        bibSenha.Tabela(cores_totais, 3, senha_jogador)
        print(f"Escolha sua {contador}ª cor.")
        escolha = input("-> ").capitalize()
        if( escolha in cores_totais ):
            if(escolha not in senha_jogador):
                senha_jogador.append(escolha)
                contador += 1

            else:
                print("Você já escolheu essa cor!\n Tente outra vez.")
        else:
            print("Você não pode escolher essa cor!\nTente outra vez.")
        time.sleep(0.5)

#if para mostrar a pontuação caso o jogador não tenha ganho

    if( bibSenha.TestarVitoria(senha, senha_jogador) == False ):
        time.sleep(0.5)

        ordem_certa = bibSenha.TestarAcertosTotais(senha, senha_jogador)
        cores_certas = bibSenha.TestarAcertosParciais(senha, senha_jogador)
        pontuacao += ordem_certa * 7 + cores_certas * 3

        senha_jogador = str(senha_jogador)[1:-1].replace("'", "")

        print(f"Sua senha nesta rodada: {senha_jogador}")
        print(f"Você está com {pontuacao} pontos.")
        if(ordem_certa == 1):
            print(f"Você teve {ordem_certa} acerto total nesta rodada.")
        else:
            print(f"Você teve {ordem_certa} acertos totais nesta rodada.")
        if(cores_certas == 1):
            print(f"Você teve {cores_certas} acerto parcial nesta rodada.")
        else:
            print(f"Você teve {cores_certas} acertos parciais nesta rodada.")

        print()
        chance_atual += 1

        senha_jogador = []


#if para mostrar que ele ganhou
#else para mostrar que ele não ganhou
if(bibSenha.TestarVitoria(senha, senha_jogador) == True):
    print("Parabéns! Você ganhou o jogo! 💣💣💣")
else:
    bibSenha.DefineMensagem(pontuacao)