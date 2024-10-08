class Livro:
    def __init__(self, titulo, autor, ano_pub, genero, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_pub = ano_pub
        self.genero = genero
        self.disponibilidade = disponibilidade

    def info(self):
        disponibilidade_str = "Disponível" if self.disponibilidade else "Indisponível"
        print(f"Título: {self.titulo} \nAutor: {self.autor}\nPublicação: {self.ano_pub}\nGênero: {self.genero}\nDisponibilidade: {str(disponibilidade_str)}")

    def emprestimo(self):
        if self.disponibilidade == False:
            print(f"O livro {self.titulo} foi emprestado")
        else:
            print(f"O livro {self.titulo} está disponivel para ser emprestado")

    def devolucao(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f"O livro {self.titulo} foi devolvido")
        else: print(f"O livro {self.titulo} está disponível")

    def verificar_disp(self):
        return "Disponível" if self.disponibilidade else "indisponivel"

livro1 = Livro("O Hobbit", "JRR Tolkien", 1950, "Fantasia", True)
Livro.info(livro1)
Livro.verificar_disp(livro1)
Livro.devolucao(livro1)
Livro.emprestimo(livro1)