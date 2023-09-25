from random import choice
from typing import Type

class Jogador:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.placar = 0
        self.__escolha = ['Pedra', 'Papel', 'Tesoura']
    
    def escolher(self) -> str:
        return choice(self.__escolha)

class Jogo:

    def jogar(self, jogador_1: Type[Jogador], jogador_2: Type[Jogador]) -> int:
        
        escolha_jogador_1 = jogador_1.escolher()
        escolha_jogador_2 = jogador_2.escolher()

        if escolha_jogador_1 == escolha_jogador_2:
            return 0
        elif (
            (escolha_jogador_1 == 'Pedra' and escolha_jogador_2 == 'Tesoura')
            or (escolha_jogador_1 == 'Papel' and escolha_jogador_2 == 'Pedra')
            or (escolha_jogador_1 == 'Tesoura' and escolha_jogador_2 == 'Papel')
            ): return 1
        else:
            return 2

joao = Jogador('João')
gabriel = Jogador('Gabriel')

jogo_1 = Jogo()

while True:

    if jogo_1.jogar(joao, gabriel) == 0:
        pass
    elif jogo_1.jogar(joao, gabriel) == 1:
        gabriel.placar += 1
    else:
        joao.placar += 1

    print(f'{joao.nome}: {joao.placar} vitórias --- {gabriel.nome}: {gabriel.placar} vitórias.')