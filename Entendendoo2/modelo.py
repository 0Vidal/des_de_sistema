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

    def __str__(self):
            return f"{self._nome} - {self.ano} - {self._curtir} Curtidas"

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
            return f"{self._nome} - {self.ano} - {self.duracao} - {self._curtir} Curtidas"

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
            return f"{self._nome} - {self.ano} - {self.temporadas} - {self._curtir} Curtidas"

#Instanciar é salvar em uma variável

supernatural = Series("Supernatural", 2005, 15)
supernatural.curtida()
#print(f"{supernatural.valor_nome} - {supernatural.ano} - {supernatural.temporadas} - {supernatural.curtida()}")

avatar = Filmes("Avatar", 2009, 177)
#print(avatar.ano)

filmes_series = [supernatural, avatar]

for programas in filmes_series:
    print(programas)
