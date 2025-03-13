# Associação -> O escritor usa caneta (Setinha)
# Agregação -> Um escritor tem muitas canetas (Diamante)

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []  

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} de {livro.autor}")

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.mostrar_livros()