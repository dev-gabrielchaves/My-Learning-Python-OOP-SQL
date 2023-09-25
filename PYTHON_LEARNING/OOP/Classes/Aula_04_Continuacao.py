"""Na sessão anterior, vimos que é possível alterar o valor de uma variável de classe a partir de um
objeto da classe, pois ambos estão no mesmo contexto, e essa alteração estaria atribuída apenas ao objeto
em questão.
Porém o mais interesse é alterar valores de variáveis de classe com a classe, para utilizamos o decorador
'@classmethod' e criamos então um método de classe."""

class MinhaClasse:
    
    estatico = 'Programador' #'estatico' é uma variável da classe 'MinhaClasse'

    def __init__(self, estado) -> None:
        self.estado = estado

    @classmethod
    def alterar_estatico(cls, valor: str) -> None:
        cls.estatico = valor

objeto_1 = MinhaClasse(True)

print(objeto_1.estatico)
print(MinhaClasse.estatico)

objeto_1.alterar_estatico('Médico') #Mesmo se tratando do objeto, ao chamar o método eu altero o valor de 'estatico' para toda a classe.

print(objeto_1.estatico)
print(MinhaClasse.estatico)