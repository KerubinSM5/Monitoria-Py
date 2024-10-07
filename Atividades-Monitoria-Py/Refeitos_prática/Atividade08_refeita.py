class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero, disponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponibilidade = disponibilidade
    def info(self):
        disponibilidade_str = "Disponível" if self.disponibilidade else "Indisponível"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Gênero: {self.genero}")
        print(f"Status: {disponibilidade_str}")
    def emprestar_livro(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"O livro '{self.titulo}' foi emprestado")
        else:
            print(f"O livro '{self.titulo}' está indisponivel para emprestimo.")
    def devolver_livro(self):
        if self.disponibilidade:
            self.disponibilidade = True
            print("O livro foi devolvido")
    def ver_disponibilidade(self):
        if self.disponibilidade:
            return f"O livro '{self.titulo}' está disponível."
        else:
            return f"O livro '{self.titulo}' está indisponível."
    def atualizar_ano(self, novo_ano):
        print(f"Ano de publicação do livro '{self.titulo}' atualizado para {novo_ano}.")

if __name__ == '__main__':
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
    livro2 = Livro("1984", "George Orwell", 1949, "Ficção Científica", False)

    livro1.info()
    print(livro1.ver_disponibilidade())
    livro1.emprestar_livro()
    livro1.info()
    livro1.devolver_livro()
    livro1.info()
    print("------------------------------------------------------")
    livro2.info()
    print("------------------------------------------------------")
    livro1.atualizar_ano(1955)