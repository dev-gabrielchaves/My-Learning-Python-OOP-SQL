"""
Vamos utilizar do mesmo códido da 'Aula_06' para demonstrar 
o princípio de 'Injeção de Dependência'.
"""
from typing import Type

class Casa:

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco
    
    def acender_luzes(self) -> None:
        print("Luzes acesas!")
    
    def apagar_luzes(self) -> None:
        print("Luzes apagadas!")

    def get_endereco(self) -> str:
        return self.__endereco

class Pessoa:

    """Agora podemos ver que diferente do código da aula anterior, 'local'
    é um atributo da nossa classe 'Pessoa', ou seja, o nosso método construtor,
    que tem como parámetro 'local' recebera um objeto da classe 'Casa' como parámetro."""
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__nome = nome
        self.__local = local

    def entrar_no_local(self) -> None:
        print(f"\n{self.__nome} entrou no local!")
        #self.__local = objeto da classe 'Casa'.
        self.__local.acender_luzes()
    
    def sair_do_local(self) -> None:
        print(f"\n{self.__nome} saiu do local!")
        self.__local.apagar_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(f"\n{self.__nome} está na {endereco}.")

#Criando objeto 'casa_de_praia' da classe 'Casa'.
casa_de_praia = Casa("Rua dos Artistas")
"""Criando objeto 'pessoa_1' da classe 'Pessoa' que recebe como parametro o nome e
o local, que é objeto da classe 'Casa'.""" 
pessoa_1 = Pessoa("Gabriel", casa_de_praia)

pessoa_1.entrar_no_local()
pessoa_1.apresentar_local()
pessoa_1.sair_do_local()