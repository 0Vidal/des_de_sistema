def jogar_forca():

    print("------------------------------")
    print("\nBem Vindo ao Jogo da Forca\n")
    print("------------------------------")

    lista = ["_ _ _ _ _ _ _ _ _ _"]

    palavra_secreta = "Carro"
    perdeu = False
    acertou = False

    while not perdeu and not acertou:
        chute = input("Escreva uma letra: ")
        chute = chute.strip()

        #index define a posição da letra
        index = 0

        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f"A letra {chute} está na posição {index}")
            index = index + 1

