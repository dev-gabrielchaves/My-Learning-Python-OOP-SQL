class Empregado: #Substantivo.

    taxa_aumento = 1.05 #Variável de classe.
    
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        if self.validacao(nome, idade, salario) is True:
            self.nome = nome #Atributos ou estados recebem substantivos também.
            self.idade = idade
            self.__salario = salario #Definindo salário como privado.
        else:
            Empregado.aviso()
    
    def fazer_cafe(self) -> str: #Verbo em método.
        return f"Funcionário {self.nome} está fazendo o café!" #Estamos retornando 'str'.
    
    def apresentar_salario(self) -> None: #Método responsável por apresentar salário, visto que ele é apenas acessável pela classe.
        print(f"Funcionário {self.nome} recebe: {self.__salario:.2f} reais!")

    def aplicar_aumento(self) -> None:
        self.__salario *= self.taxa_aumento

    def validacao(self, nome: str, idade: int, salario: float) -> bool:
        if isinstance(nome, str) and isinstance(idade, int) and isinstance(salario, float):
            return True
        else:
            return False
    
    @classmethod
    def alterar_taxa(cls, nova_taxa):
        cls.taxa_aumento = nova_taxa
    
    @staticmethod
    def aviso():
        print("Inválido!")

funcionario_1 = Empregado('Gabriel', 24, 1200.00)

print(funcionario_1.fazer_cafe())
funcionario_1.apresentar_salario()

funcionario_1.aplicar_aumento()

funcionario_1.apresentar_salario()

Empregado.alterar_taxa(1.25)

funcionario_1.aplicar_aumento()

funcionario_1.apresentar_salario()