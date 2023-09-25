"""
Definimos Polimorfismo como um princípio a partir do qual as classes derivadas de uma única 
classe base são capazes de invocar os métodos que, embora apresentem a mesma assinatura, 
comportam-se de maneira diferente para cada uma das classes derivadas.
"""

class Mae:

    def se_apresentar(self) -> None:
        print("Estou me apresentando!")

class Filha(Mae):

    def se_apresentar(self) -> None:
        print("Estou alterando este método na classe Filha")

class Neta(Filha):

    pass

mae = Mae()
filha = Filha()
neta = Neta()

mae.se_apresentar()
filha.se_apresentar()
neta.se_apresentar()