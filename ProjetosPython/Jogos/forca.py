def jogar_forca():

    print("-"*26)
    print("\nBem Vindo ao Jogo da Forca\n")
    print("-"*26)

    palavra_secreta = "Kalimba"
    letras_acertadas = ["_","_","_","_","_","_","_"]
    perdeu = False
    acertou = False
    #Enquanto o jogador não acertar a palavra secreta
    #O jogador pode jogar

    while(not perdeu and not acertou):
        chute = input("Escreva uma Letra: ")
        chute = chute.strip()
        #Index define a posição da letra
        index = 0
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)
           

    
if(__name__ == "__main__"):
    jogar_forca()