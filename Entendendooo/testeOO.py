#numero = 345
#titular = "Victor"
#saldo = 100.0
#limite = 2000.0

#conta = {"numero":345, "titular": "Victor",
#         "saldo": 100.0, "limite": 2000.0
#}

#print(conta["titular"])
#print(conta["limite"])

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular": titular,
        "saldo": saldo, "limite": limite
    }
    return conta

conta = criar_conta(123, "João", 200.0, 1000.0)
#print(conta["limite"])

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Seu saldo atual é {conta["saldo"]}")

depositar(conta, 450.0)
extrato(conta)
sacar(conta, 400.0)
extrato(conta)