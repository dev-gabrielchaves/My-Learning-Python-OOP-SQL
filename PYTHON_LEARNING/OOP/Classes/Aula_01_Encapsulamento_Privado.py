class Calculadora:

    #O método calcular() é público, ou seja, pode ser acessado por fora da classe.
    def calcular(self, op, num1, num2):

        if op == '+':
            return self.__somar(num1, num2)

        elif op == '-':
            return self.__subtrair(num1, num2)

        else:
            print("Operação Inválida!")
    
    #Ao colocar '__' antes do nome do método, ele se torna privado, podendo apenas ser acessado pela classe.
    def __somar(self, numero_1, numero_2): 
        return numero_1 + numero_2
    
    def __subtrair(self, numero_1, numero_2):
        return numero_1 - numero_2
    
soma_1 = Calculadora()

#soma_1.__somar(1, 3) <-- Não posso fazer isso, pois o método '__soma' só pode ser acessado pela classe 'Calculadora'

resultado_1 = soma_1.calcular('+', 3, 5)

print(resultado_1)