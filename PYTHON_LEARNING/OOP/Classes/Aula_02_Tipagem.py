class Pessoa: #Nome de classes devem ser substantivos.

    def __init__(self, nome: str, idade: int) -> None: #A tipagem tem caráter mais de ilustrar para facilitar o entendiment do código.
        self.nome = nome #O mesmo para atributos, devem ser substantivos também.
        self.__idade = idade
    
    def dirigir(self, veiculo: str) -> None: #Métodos, ações, devem recebem verbos.
        print('Você está dirigindo um {}'.format(veiculo))
    
    def cantar(self) -> None:
        print('LaLaLa')
    
    def apresentar_idade(self) -> int:
        return self.__idade

gabriel = Pessoa('Gabriel', 24)

#print(gabriel.__idade) <-- Como dito na aula anterior, '__idade' só pode ser acessado dentro da classe.

print(gabriel.apresentar_idade()) #Jeito correto de mostrar a idade neste caso.