class Cliente:
    def __init__(self, nome, cpf, dataNascimento, saldo, credito):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento
        self.__saldo = saldo
        self.__credito = credito

    def extrato(self):
        print(f"Cliente: {self.__nome}")
        print(f"Saldo: R$ {self.__saldo:.2f}")
        print(f"Crédito: R$ {self.__credito:.2f}")

    def adicionar_credito(self, valor):
        if(valor <= 0):
            print("Valor inválido")
        else:
            self.__credito += valor

    def compra_permitida(self, valor):
        valor_disponivel = self.__saldo + self.__credito
        return valor <= valor_disponivel

    def comprar_carro(self, valor):
        if(self.compra_permitida(valor)):
            if(self.__credito >= valor):
                self.__credito -= valor
            else:
                restante = valor - self.__credito
                self.__credito = 0
                self.__saldo -= restante
                print("Compra realizada com sucesso!")
        else:
            print("Saldo e crédito insuficientes.")

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def credito(self):
        return self.__credito

    @property
    def cpf(self):
        return self.__cpf

class CarroVendido:
    def __init__(self, ano, modelo, quilometragem, valor_venda):
        self.__ano = ano
        self.__modelo = modelo
        self.__quilometragem = quilometragem
        self.__valor_venda = valor_venda

    def gerar_credito(self, cliente):
        cliente.adicionar_credito(self.__valor_venda)

        print(f"\nCarro vendido: {self.__modelo}")
        print(f"Crédito gerado: R$ {self.__valor_venda:.2f}")

    @property
    def valor_venda(self):
        return self.__valor_venda

class CarroNovo:
    def __init__(self, ano, modelo, quilometragem, valor_novo):
        self.__ano = ano
        self.__modelo = modelo
        self.__quilometragem = quilometragem
        self.__valor_novo = valor_novo

    def vender(self, cliente):
        print(f"\nCarro escolhido: {self.__modelo}")
        print(f"Valor: R$ {self.__valor_novo:.2f}")

        cliente.comprar_carro(self.__valor_novo)

    @property
    def valor_novo(self):
        return self.__valor_novo

    @staticmethod
    def nome_loja():
        return "Clovis-Car"