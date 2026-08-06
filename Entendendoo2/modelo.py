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

class Playlist():
    def __init__(self, nomePl, elementos):
        self.nomePl = nomePl
        self._elementos = elementos

    @property
    def listar(self):
         return self._elementos

    @property
    def tamanho_lista(self):
        return len(self._elementos)

#Séries
supernatural = Series("Supernatural", 2005, 15)
Dd = Series("Demolidor", 2015, 3)

#Filmes
avatar = Filmes("Avatar", 2009, 177)
Stw = Filmes("Star Wars: Eisódio III - A Vingança dos Sith", 2005, 146)

#Curtidas
supernatural.curtida()
supernatural.curtida()
supernatural.curtida()
supernatural.curtida()
Dd.curtida()
Dd.curtida()
Dd.curtida()
avatar.curtida()
avatar.curtida()
avatar.curtida()
Stw.curtida()
Stw.curtida()
Stw.curtida()
Stw.curtida()
Stw.curtida()

filmes_series = [avatar, Stw, supernatural, Dd]
Pl_Aleatoria = Playlist("Aleatóriamente Aleatória", filmes_series )

print(f"Tamanho da Playlist: {len(Pl_Aleatoria)}")
print(f"Está na Playlist? {avatar in Pl_Aleatoria}")

for programas in Pl_Aleatoria:
    print(programas)

#nome, programas, tamanho()
#nomePl = nome da Playlist
