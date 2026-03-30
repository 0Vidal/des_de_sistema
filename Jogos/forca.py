def jogar_forca():

    print("-"*26)
    print("\nBem Vindo ao Jogo da Forca\n")
    print("-"*26)

    arquivo = open("Jogos/palavras.txt", "r")
    palavras = []

    for linha in palavras:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    palavra_secreta = "Kalimba".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    #for letra in palavra_secreta:
        #letras_acertadas.append("_")
    
    perdeu = False
    acertou = False
    erros = 0

    #Enquanto o jogador não acertar a palavra secreta
    #o jogador pode jogar

    while(not perdeu and not acertou):
        chute = input("Escreva uma Letra: ")
        chute = chute.strip().upper()

        #Index define a posição da letra
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1  
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        print(erros)
        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar_forca()