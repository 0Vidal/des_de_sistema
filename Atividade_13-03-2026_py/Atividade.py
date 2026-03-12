tarefa = ["Estudar Engenharia","Ir no Mercado","Banhar o Cachorro"]

def Exibir_Menu():
    print("="*25)
    print("Menu das Lista de Tarefas")
    print("="*25)
    print("(1) Listar tarefas")
    print("(2) Adicionar tarefa")
    print("(3) Remover tarefa")
    print("(4) Sair")
    print("="*25)

while True:
    Exibir_Menu()
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 1:
        print("\nSua lista atual:")
        for num, trf in enumerate(tarefa, 1):
            print(num, "-", trf)

    elif opcao == 2:
        print("*Adicione uma tarefa por vez")
        nova_tarefa = input("\nAdicionar Tarefa: ")
        tarefa.append(nova_tarefa)

    elif opcao == 3:
        print("*Remova uma tarefa por vez")
        remove_tarefa = input("\nRemover Tarefa: ")
        tarefa.remove(remove_tarefa)

    elif opcao == 4:
        print("Fechando sua Lista de Tarefas...")
        break

    else:
        print("Opção inválida -_-")
        print("Inicie o código novamente!!")
        break
