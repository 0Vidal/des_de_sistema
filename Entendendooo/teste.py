from conta import Conta

conta1 = Conta(1, "Victor", 50.0)
conta2 = Conta(2, "Roberto", 45.5)
conta3 = Conta(3, "Carlos", 0.0, 1200.0)
print(conta1.limite)
print(conta2.limite)
print(conta3.limite)

class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views

video = Video("Tenet", 10.0, 50000)

class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

livro = Livro("O Hobbit", "J.R.R Tolkien", 1937)
