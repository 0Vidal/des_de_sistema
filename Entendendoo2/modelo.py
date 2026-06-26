#Filmes e séries tem as seguintes características: 

#Filme: Nome, Ano, Duração, Avaliação
#série: Nome, Ano, Temporadas, Avaliação

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1

class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1

print("Série:")
supernatural = Series("Supernatual", 2005, 15)
supernatural.curtida()
print(f"Nome: {supernatural.__nome} - Ano: {supernatural.ano} - Temporada: {supernatural.temporadas} - Curtidas: {supernatural.curtir}")

print("Filme:")
avatar = Filme("Avatar", 2009, 177)
print(avatar.ano)
