class  Conta:
    def __init__(self, numero, titular, saldo, limite):
       self.numero = numero
       self.titular = titular
       self.saldo = saldo
       self.limite = limite

    #Declaração dos métodos (função)
    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if(self.saldo < valor):
            print(f"Não é possível sacar o valor desejado")
        
        else:
            self.saldo -= valor 