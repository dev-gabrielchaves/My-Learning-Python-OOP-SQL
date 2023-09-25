#Adicionar funcionalidade do ID exclusivo...
from biblioteca import Biblioteca
from livros import Livro
import os

print("Bem vindo a Biblioteca!\n")

biblioteca_central = Biblioteca()

while True:
    
    try: 
        opcao = int(input("[1] - Cadastrar livro\n" \
                          "[2] - Listar livros cadastrados\n" \
                            "[3] - Remover livro cadastrado\n" \
                                "[4] - Checar se livro está cadastrado\n" \
                                    "[0] - Sair\n"))
        
        os.system('cls')

        if opcao == 1:
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano do livro: "))

            biblioteca_central.adicionar_livro(titulo, autor, ano)

            os.system('cls')

            print("Livro cadastrado com sucesso!\n")

        elif opcao == 2:
            biblioteca_central.listar_livros()
    
        elif opcao == 3:
            identificador = int(input("Digite o ID do livro que deseja remover: "))
            biblioteca_central.remover_livro(identificador)
        
        elif opcao == 4:
            identificador = int(input("Digite o ID do livro que deseja verificar: "))
            biblioteca_central.verificar_livro(identificador)

        elif opcao == 0:
            print("Até a próxima!")
            break

        else: 
            print("Opção inexistente!\n")
    
    except:
        os.system('cls')
        print("Digite um número válido!\n")