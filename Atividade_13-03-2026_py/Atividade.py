tarefa = ["Estudar Engenharia","Ir no Mercado","Banhar o Cachorro"]

def Exibir_Menu():
    print("-"*30)
    print("Menu das Lista de Tarefas")
    print("-"*30)
    print("(1) Listar tarefas")
    print("(2) Adicionar tarefa")
    print("(3) Remover tarefa")
    print("(4) Sair")
    print("-"*30)

while True:
    Exibir_Menu()
    opcao = input("\nEscolha uma opção: ")

