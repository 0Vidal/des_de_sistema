tarefa = ["Estudar Engenharia","Ir no Mercado","Banhar o Cachorro"]

def Exibir_Menu():
    print("="*25)
    print("Menu das Lista de Tarefas")
    print("="*25)
    print("(1) Listar tarefas")
    print("(2) Adicionar tarefa")
    print("(3) Remover tarefa")
    print("(4) Sair")
    print("-"*25)

while True:
    Exibir_Menu()
    opcao = int(input("\nEscolha uma opção: "))
    

    if opcao == 1:
        print("\nSua lista atual:")
        print(tarefa)
    

    if opcao == 2:
        nova_tarefa = input("\n Adicione uma Nova Tarefa: ")
        tarefa.append(nova_tarefa)

    if opcao == 3:
        print("Lembre-se que a lista começa do número 0, ou seja, esta lista não se inicia por padrão com número 1")
        remove_tarefa = input("\n Digite o Número da Tarefa para Remover: ")
        tarefa.pop(remove_tarefa)