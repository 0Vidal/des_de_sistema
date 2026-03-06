
import random as rd

def jogar_adivinhacao():

    print("-------------------------------")
    print("\nBem vindo ao jogo de adivinhação!\n")
    print("-------------------------------")

    #Definição das variáveis#
    n_secreto = rd.randrange(1, 101)
    n_tentativas = 0
    rodada = 1

    print(n_secreto)

    pontuacao = 1000
    print(f"\nPontuação Atual: {pontuacao}\n")

    print("Níveis de dificuldade")
    print("\n(1) Fácil (2) Médio (3) Difícil (4) Aleatório\n")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        n_tentativas = 12
    elif(nivel == 2):
        n_tentativas = 8
    elif(nivel == 3):
        n_tentativas = 4
    else:
        n_tentativas = rd.randrange(1,13)


    for rodada in range(1,n_tentativas + 1):
        print(f"Rodada {rodada} de {n_tentativas}")
        entrada = int(input("Digite um  número entre 1 e 100: "))
        acertou = entrada == n_secreto
        entrada_maior = entrada > n_secreto
        entrada_menor = entrada < n_secreto

        if(entrada > 100 or entrada < 1):
            print(f"\nO valor {entrada} não é permitido")
            continue

        print(f"\nVocê digitou o número: {entrada}")

        #Verificação de acerto/erro#
        if(acertou):
            print("Parabéns, você acertou o número secreto")
            print(f"Parabéns (ou não hahha)! Você fez {pontuacao} pontos.")
            break
        else:
            if(entrada_maior):
                print("Você errou! O número digitado foi maior que o secreto")
            if(entrada_menor):
                print("Você errou! O número digitado foi menor que o secreto")

        pontos_perdidos = abs(n_secreto - entrada)
        pontuacao = pontuacao - pontos_perdidos
        rodada = rodada + 1    
    print("\nFim de jogo")