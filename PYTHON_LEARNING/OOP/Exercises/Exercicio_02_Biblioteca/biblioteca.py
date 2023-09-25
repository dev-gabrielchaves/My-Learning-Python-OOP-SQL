from livros import Livro

class Biblioteca:

    def __init__(self) -> None:
        self.__livros = []

    def adicionar_livro(self, titulo: str, autor: str, ano: int) -> None:
        #Criando objeto 'novo_livro' instância da classe 'Livro' e entregando parâmetros. 
        novo_livro = Livro(titulo, autor, ano)
        #Criando uma versão dicionário desse 'novo_livro' para eu ter controle das chaves e valores.
        dict_novo_livro = {'Titulo' : f'{novo_livro.titulo}',
                           'Autor' : f'{novo_livro.autor}',
                           'Ano' : f'{novo_livro.ano}',
                           'ID' : novo_livro.num_id
                           }
        #Adicionando esse novo dicionário com todas as informações do novo livro em nossa lista de livros.
        self.__livros.append(dict_novo_livro)
    
    def listar_livros(self) -> None:
        #Pecorrendo cada livro na nossa lista de livros.
        for livro in self.__livros:
            #Mostrando informações de cada livro.
            for key in livro:
                print(f'{key}: {livro[key]}')
            print()
    
    def remover_livro(self, id: int) -> None:
        contador = 0
        #Pecorrendo cada livro na nossa lista de livros.
        for livro in self.__livros:
            #Checando se nosso 'id' está no nosso livro, caso sim, delete-o.
            if id == livro['ID']:
                contador += 1
                self.__livros.remove(livro)
                print("Livro removido!\n")
        if contador == 0:
            print("Livro não se encontra cadastrado!\n")
    
    def verificar_livro(self, id: int) -> None:
        contador = 0
        #Pecorrendo cada livro na nossa lista de livros.
        for livro in self.__livros:
            #Checando se nosso 'id' está no nosso livro.
            if id == livro['ID']:
                contador += 1
                print("O livro se encontra registrado!\n")
                #Caso ele esteja registrado mostre-o.
                for key in livro:
                    print(f'{key}: {livro[key]}')
                print()
        
        if contador == 0:
            print("Livro não se encontra cadastrado!\n")