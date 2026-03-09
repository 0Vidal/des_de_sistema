tarefas = ["Estudar Python", "Lavar a louça", "Pagar conta URGENTE"]

def exibir_menu():
    print("\n" + "="*20)
    print("  GESTOR DE TAREFAS")
    print("="*20)
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa (por ID)")
    print("4. Filtrar por palavra-chave")
    print("5. Sair")

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        
        print("\nSua lista atual:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"[{idx}] - {tarefa}")
        
        if any("URGENTE" in t.upper() for t in tarefas):
            print("\n Nota: Você tem itens urgentes na lista!")

    elif opcao == "2":
        nova = input("Digite a nova tarefa: ")
        
        if len(nova.strip()) > 0:
            tarefas.append(nova)
            print("Tarefa adicionada!")
        else:
            print("Erro: A tarefa não pode ser vazia.")

    elif opcao == "3":
        try:
           
            id_remover = int(input("Digite o ID da tarefa para remover: "))
           
            removida = tarefas.pop(id_remover - 1)
            print(f"Tarefa '{removida}' removida com sucesso!")
        except (ValueError, IndexError):
            print("Erro: ID inválido. Veja a lista novamente.")

    elif opcao == "4":
        termo = input("Digite o que deseja buscar: ").lower()
        
        resultado = list(filter(lambda t: termo in t.lower(), tarefas))
        
        if resultado:
            print(f"\nResultados encontrados: {resultado}")
        else:
            print("\nNenhuma tarefa corresponde à busca.")

    elif opcao == "5":
        print("Até logo!")
        break

    else:
        print("Opção inválida!")