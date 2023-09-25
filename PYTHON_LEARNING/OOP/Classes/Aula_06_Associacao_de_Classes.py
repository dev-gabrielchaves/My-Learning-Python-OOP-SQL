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

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    """Abaixo podemos ver uma associação de classes, pois estou chamando o método 
    'acender_luzes' que é da classe 'Casa' no método 'entrar_no_local' da classe
    'Pessoa', ou seja, toda vez que a pessoa entrar no local, as luzes serão acesas."""
    def entrar_no_local(self, local: any) -> None:
        print(f"\n{self.__nome} entrou no local!")
        local.acender_luzes()
    
    def sair_do_local(self, local: any) -> None:
        print(f"\n{self.__nome} saiu do local!")
        local.apagar_luzes()
    
    def apresentar_local(self, local: any) -> None:
        endereco = local.get_endereco()
        print(f"\n{self.__nome} está na {endereco}.")

casa_de_praia = Casa("Rua dos Coqueiros")
pessoa_1 = Pessoa('Adriano')

#Como podemos ver abaixo, o objeto 'casa_de_praia' é o parámetro do método 'entrar_no_local'.
pessoa_1.entrar_no_local(casa_de_praia)
pessoa_1.apresentar_local(casa_de_praia)
pessoa_1.sair_do_local(casa_de_praia)