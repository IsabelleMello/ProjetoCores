import random

#Organizar as escolhas disponíveis para o usuário

def Tabela(cores, colunas, palpite_atual):
    largura = 0
    for cor in cores:
        if (len(cor) > largura) and (cor not in palpite_atual):
            largura = len(cor)
    cor_atual = 0
    linha = 1
    print("|", end = "")
    while( cor_atual < len(cores) ):
        if(cores[cor_atual] not in palpite_atual):
            print(f" {cores[cor_atual].center(largura)} ", end = "")
            print("|", end = "")
        cor_atual += 1
        if (linha % colunas == 0):
            print()
            linha += 1
    print()

def GerarSenha():
    cores = ["Vermelho", "Verde", "Branco", "Amarelo", "Azul", "Preto"]
    quantidade = 4
    senha = []
    for cor_atual in range(quantidade):
        cor_aleatoria = random.choice(cores)
        while(cor_aleatoria in senha):
            cor_aleatoria = random.choice(cores)
        senha.append(cor_aleatoria)
    return senha

def ValidarPalpite(palpite):
    cores = ["Vermelho", "Verde", "Branco", "Amarelo", "Azul", "Preto"]
    if len(palpite) == 4:
        for cor_atual in range(len(palpite)):
            palpite[cor_atual] = palpite[cor_atual].lower()

        for cor_atual in palpite:
            if palpite.count(cor_atual) > 1:
                return False
            if(cor_atual not in cores):
                return False
        return True
    else:
        return False

def TestarVitoria(senha, palpite):
    if(senha == palpite):
        return True
    else:
        return False

def TestarAcertosTotais(senha, palpite):
    acertosTotais = 0
    for cor_atual in range(len(senha)):
        if senha[cor_atual].lower() == palpite[cor_atual].lower():
            acertosTotais += 1
    return acertosTotais

def TestarAcertosParciais(senha, palpite):
    quantidade = 0
    for i in range(len(senha)):
        if palpite[i] in senha:
            quantidade += 1
    quantidade -= TestarAcertosTotais(senha, palpite)
    return quantidade

def CalcularPontosGanhos(senha, palpite):
    pontuacao  = TestarAcertosTotais  (senha, palpite) * 7
    pontuacao += TestarAcertosParciais(senha, palpite) * 3
    return pontuacao

def DefineMensagem(pontos):
    print(f"Você marcou {pontos} pontos.")
    if(pontos < 20):
        print("Hum, você precisa melhorar seus palpites! Jogue mais um pouco e você com certeza irá ganhar!")
    elif(pontos < 30):
        print("Seus palpites foram bons, continue assim e você vai ganhar rapidinho!")
    else:
        print("Muito bom, você quase acertou! Talvez na próxima!")