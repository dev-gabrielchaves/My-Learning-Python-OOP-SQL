from random import randint

class Livro:

    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.num_id = randint(1, 1000)