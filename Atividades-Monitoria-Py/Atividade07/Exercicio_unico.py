#Crie um programa em Python para gerenciar um catálogo de livros. O programa deve permitir as seguintes funcionalidades

import datetime

class Livro: #definições de um livro: inclui titulo, autor e publicação
    def __init__(self, titulo, autor, ano_pub): #__init__: usado para iniciar uma nova instância na classe / construtor da classe
        self.titulo = titulo #titulo, autor e ano_pub: parametros que devem ser fornecidos para que o livro seja criado
        self.autor = autor
        self.ano_pub = datetime.datetime.strptime(ano_pub, '%Y-%m-%d').date()

    def __str__(self): #Retorna os valores de "dados_livros" porém com os dados em string
        return f"Título: {self.titulo}\n" f"Autor: {self.autor}\n" f"Ano: {self.ano_pub}"

class Catalogo: #define o catálogo
    def __init__(self):
        self.livros = [] #define a lista de armazenamento dos livros

    def add_livro(self, livro): #Adicionar o livro
        self.livros.append(livro) #append adiciona o livro na lista
        print("Livro adicionado")

    def remove_livro(self, criterio, valor_esp): #remover
        for livro in self.livros: #lê todos os livros da lista até encontrar o selecionado
            if getattr(livro, criterio) == valor_esp: #getattr: retorna o valor do critério selecionado
                self.livros.remove(livro) #remove o livro da lista
                print("Livro removido")
            else:
                print("Livro não encontrado")

    def buscar_livro(self, criterio_gen, valor_esp): #buscar
        resultados = [livro for livro in self.livros if getattr(livro, criterio_gen) == valor_esp]
        if resultados:
            for livro in resultados:
                print("Livro encontrado")
        else:
            print("Nenhum livro encontrado")

    def ordenar_livro_autor(self): #ordenar
        self.livros.sort(key=lambda livro: livro.autor) #organiza os livros pela ordem alfabética dos autores
        print("Livros ordenados pelo autor")

    def exibir_acervo(self): #mostra os lívros do catálogo
        if not self.livros:
            print("Nenhum livro encontrado")
        else:
            for livro in self.livros:
                print(livro)
                print("_" * 30) #separação (igual meus pais :( )

def menu(): #responsável por interagir com o usuário, deverá ser chamado para funcionar
    catalogo = Catalogo()

    while True:
        print("\n--- Catálogo de Livros ---")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Buscar livro")
        print("4. Ordenar livros por autor")
        print("5. Exibir catálogo completo")
        print("6. Sair")

        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1: #adiciona livro
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            data_pub = input("Digite o data de publicacao do livro formato (aaaa-mm-dd)")
            livro = Livro(titulo, autor, data_pub) #seleciona todos os dados para tornar deles um livro
            catalogo.add_livro(livro) #adiciona um livro na lista

        elif opcao == 2: #remove livro
            criterio_gen = input("Remover por 'titulo' ou 'autor'?: ").lower() #seleciona remoção por titulo ou autor
            valor_esp = input(f"Digite o {criterio_gen} do livro: ").lower() #remove conforme a seleção do critério
            if criterio_gen in ['titulo','autor']:
                catalogo.remove_livro(criterio_gen, valor_esp)
            else:
                print("Critério inválido")

        elif opcao == 3: #busca livros
            criterio_gen = input("Buscar por titulo ou autor?: ").lower()
            valor_esp = input(f"Digite o {criterio_gen} do autor: ")
            if criterio_gen in ['titulo','autor']:
                catalogo.buscar_livro(criterio_gen, valor_esp)

        elif opcao == 4: #Ordena por autor
            catalogo.ordenar_livro_autor()

        elif opcao == 5: #Mostra catálogo
            print("\n === Catálogo completo ===")
            catalogo.exibir_acervo()
            input("\n Pressione <enter> para continuar")

        elif opcao == 6: #Sair
            print("Saindo do programa, obrigado por utilizar :D ")
            break
        else: print("Opção invalida")

menu()