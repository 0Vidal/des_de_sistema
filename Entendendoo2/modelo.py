#Filmes e séries tem as seguintes características: 

#Filme: Nome, Ano, Duração, Avaliação
#série: Nome, Ano, Temporadas, Avaliação

#Classe mãe/principal
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
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._curtir = 0

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._curtir = 0

print("Série:")
supernatural = Series("Supernatural", 2005, 15)
supernatural.curtida()

print(f"Nome: {supernatural.valor_nome} - Ano: {supernatural.ano} - Temporada: {supernatural.temporadas} - Curtidas: {supernatural.curtida()}")

print("Filme:")
avatar = Filme("Avatar", 2009, 177)
print(avatar.ano)
