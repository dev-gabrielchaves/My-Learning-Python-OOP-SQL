"""Métodos getters e setters servem mais para tratarmos os nossos então atributos como estados."""
class Alarme:

    #Alarme vai receber um estado, sendo 'True' para armado ou 'False' para desligado.
    def __init__(self, estado: bool) -> None:
        self.__estado = estado #Estado, ou atributo, 'estado' é privado.
    
    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        self.__estado = valor

alarme_1 = Alarme(True) #Criando objeto 'alarme_1' e fornecendo estado 'True'.

print(alarme_1.get_estado()) #Mostrando o estado.

alarme_1.set_estado(False)

print(alarme_1.get_estado())