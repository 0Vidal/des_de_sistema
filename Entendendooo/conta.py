class  Conta:
    def __init__(self, numero, titular, saldo, limite):
       self.__numero = numero
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite

    #Declaração dos métodos (função)
    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if(self.__saldo < valor):
            print(f"Não é possível sacar o valor desejado")
        
        else:
            self.__saldo -= valor
    
    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)