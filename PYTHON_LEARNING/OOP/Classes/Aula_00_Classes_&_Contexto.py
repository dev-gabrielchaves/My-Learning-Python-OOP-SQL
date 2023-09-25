"""Definindo uma classe com o nome 'MinhaClasse', por convenção sempre colocar nome...
de classe em CamelCase."""
class MinhaClasse:

    """Dentro do método '__init__', que também pode ser chamado de método construtor,
    definimos os atributos da nossa classe."""
    def __init__(self):
        self.meu_atributo = 'Olá Mundo!'

    """Criando um método, ação da classe, com o nome 'meu_metodo',
    por definição, o método sempre deve receber 'self' como primeiro parámetro."""
    def meu_metodo(self):
        print('Estou no método!')

"""Instanciando um objeto de nome 'objeto'. Objetos são instancias de uma classe."""
objeto = MinhaClasse()

"""Chamando 'meu_metodo'."""
objeto.meu_metodo()

#Mostrando atributo do objeto 'objeto' que é uma instancia da nossa classe 'MinhaClasse'.
print(objeto.meu_atributo)