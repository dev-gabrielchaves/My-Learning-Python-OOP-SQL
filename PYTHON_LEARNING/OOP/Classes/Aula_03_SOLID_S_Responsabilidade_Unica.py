"""
No código abaixo vamos de encontro com o conceito da responsabilidade única.

Esse conceito diz que: "Cada módulo deve ser responsável por um, e apenas um, ator."

Como exemplo podemos ver a função 'cadastar' abaixo, ela apresenta diversas funcionalidades:

- Verificação dos dados;
- Realização do cadastro;
- Apresentação de erro.

class SistemaCadastral:
    def cadastar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Realizando cadastro!")
            print(f"O cadastro de {nome} de {idade} anos foi realizado com sucesso!")
        else:
            print("Dados inválidos!")
"""

#O código abaixo apresenta uma maneira mais organizada e aplicando o conceito de SRP
class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        
        if self.__validacao(nome, idade) is True:

            self.__cadastro(nome, idade)

        else:
            
            self.__aviso_erro()
    
    def __validacao(self, nome: str, idade: int) -> bool:

        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
    
    def __cadastro(self, nome: str, idade: int) -> None:
        
        print("Realizando cadastro...")
        print(f"O cadastro de {nome} de {idade} anos foi realizado com sucesso!")

    def __aviso_erro(self) -> None:

        print("Dados inválidos!")

#Apenas testando 'SistemaCadastral'. :-)
usuarios = []
i = 0

while i < 3:
    ...
    usuario_nome = input("Digite o nome do usuário: ")
    usuario_idade = input("Digite a idade do usuário: ")

    usuarios.append(SistemaCadastral())
    usuarios[i].cadastrar(usuario_nome, int(usuario_idade))

    i += 1