#Vamos aplicar os conceitos da aula em outro caso prático para vermos outras funcionalidades.
class ControleRemoto:
    
    """Agora todo vez que eu criar um objeto da classe 'ControleRemoto'
    eu vou ter que passar dois argumentos: 'tv' e 'comodo'.
    Esses argumentos serão os atributos do objeto criado."""
    def __init__(self, tv, comodo):
        self.tv = tv
        self.comodo = comodo
    
    def avancar_canal(self):
        print("Próximo Canal!")
    
    def voltar_canal(self):
        print("Voltei Canal!")

    def alterar_canal(self, canal):
        print(f'Alterei para o canal: {canal}')
    
    def mostrar_atributos(self):
        print(f"Modelo da TV: {self.tv}")
        print(f"Cômodo: {self.comodo}")

"""Recapitulando...
Criei uma classe de nome 'ControleRemoto', essa classe tem 4 métodos:
1° - Método construtor(__init__): Local onde defino atributos para o 
objeto da classe, no caso acima temos dois atributos: 'tv' e 'comodo'.
2°, 3°, 4° e 5° - Métodos de ação: Realizarão uma ação."""
    
#Criando objeto 'controle_sala' e designando argumentos.    
controle_sala = ControleRemoto('Samsumg', 'Sala')

#Executando as ações.
controle_sala.mostrar_atributos()
controle_sala.avancar_canal()
controle_sala.voltar_canal()
controle_sala.alterar_canal(15)