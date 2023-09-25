"""Variáveis de classe também são conhecidas como variáveis estáticas.
Variáveis estáticas: Quando uma variável estática é declarada, então uma única cópia dessa variavel é criada e
compartilhada com os objetos a nivel de classe. Então variáveis de classe são uma espécie de variáveis globais."""

class MinhaClasse:
    
    estatico = 'Programador' #'estatico' é uma variável da classe 'MinhaClasse'

    def __init__(self, estado) -> None:
        self.estado = estado

objeto_1 = MinhaClasse(True)
objeto_2 = MinhaClasse(False)

"""A variável 'estatico' está no contexto da classe, na qual o 'objeto_1' e 'objeto_2' estão inseridos, ou seja,
ao chamar: 'objeto_1.estatico' ele vai mostrar o valor da variável da classe 'estático'.'"""
print(objeto_1.estatico) 
print(objeto_2.estatico)
print(MinhaClasse.estatico)

"""Ao alterar o valor de 'estatico' no contexto da classe, todos os objetos passam a ter esse valor também."""
MinhaClasse.estatico = 'Médico'

print(objeto_1.estatico)
print(objeto_2.estatico)
print(MinhaClasse.estatico)

objeto_1.estatico = 'Desenvolvedor'

"""Ao alterar o valor de 'estatico' apenas no 'objeto_1', apenas ele apresentará esse valor diferente."""
print(objeto_1.estatico)
print(objeto_2.estatico)
print(MinhaClasse.estatico)