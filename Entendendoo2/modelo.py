#Filmes e séries tem as seguintes características: 

#Filme: Nome, Ano, Duração, Avaliação
#série: Nome, Ano, Temporadas, Avaliação

#Classe mãe/principal
#Super classe
class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtir = 0

    @property
    def valor_curtir(self):
        return self._curtir
    
    @property
    def valor_nome(self):
        return self._nome

    def curtida(self):
        self._curtir += 1

class Filme(Programas):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Series(Programas):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

print("Série:")
supernatural = Series("Supernatural", 2005, 15)
supernatural.curtida()

print(f"{supernatural.valor_nome} - {supernatural.ano} - {supernatural.temporadas} - {supernatural.curtida()}")

print("Filme:")
avatar = Filme("Avatar", 2009, 177)
print(avatar.ano)
