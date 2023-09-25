class Loja:
    
    tarifa = 1.03

    def __init__(self, endereco) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(f"O endereço da sua loja é: {self.__endereco}!")

    def vender(self, valor) -> None:
        print(f"Sua loja vendeu {valor*self.tarifa} reais!")
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa) -> None:
        cls.tarifa = nova_tarifa

loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

loja_praia.apresentar_endereco()
loja_praia.vender(10)

Loja.alterar_tarifa(1500)

loja_praia.apresentar_endereco()
loja_praia.vender(10)