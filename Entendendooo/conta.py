class  Conta:
    def __init__(self, numero, titular, saldo, limite):
       self.__numero = numero
       self.__titular = titular
       self.__saldo = saldo
       self.__limite_especial = limite

    #Declaração dos métodos (funções)
    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if(valor <= 0):
            print("\nValores negativos não podem ser depositados")
        else:
            self.__saldo += valor

    def saque_permitido(self, valor_saque):
        valor_disponivel_saque =  self.__saldo + self.__limite_especial
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if(self.saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")
    
    def transferir(self, valor, destino):
        if (self.__saldo < valor) or (valor < 0):
            print("Saldo insuficiente")
        else:
            self.sacar(valor)
            destino.depositar(valor)

    #Métodos para retornar apenas 
    #valores das propriedades

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite_especial
    
    @property
    def numero(self):
        return self.__numero
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    
    #Métodos para manipular os
    #valores das propriedades

    @limite.setter
    def limite(self, limite):
        self.__limite_especial = limite
