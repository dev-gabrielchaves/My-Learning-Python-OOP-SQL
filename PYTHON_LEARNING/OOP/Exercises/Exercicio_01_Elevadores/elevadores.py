from time import sleep

class Elevador:

    #Recebendo apenas localização do andar atual do elevador no método construtor.
    def __init__(self, localizacao_andar: int) -> None:
        self.localizacao_andar = localizacao_andar

    #Método responsável por mostrar o andar atual onde o elevador se encontra.
    def mostrar_andar_atual(self) -> None:
        print(f"O elevador está no {self.localizacao_andar}° andar!")
    
    #Método responsável por locomover o elevador.
    def locomover(self, andar_desejado: int) -> None:
        
        if isinstance(andar_desejado, int): #Caso o andar desejado for inteiro faça.
            
            if (andar_desejado <= 15) and (andar_desejado >= 1): #Definindo limites de andares.
                
                if self.localizacao_andar == andar_desejado:
                    print(f"\nVocê ja se encontra no {self.localizacao_andar}° andar!")

                else:

                    if self.localizacao_andar < andar_desejado: #Caso a localização atual for menor, suba.
                        self.__subir_andar(andar_desejado)

                    else: #Caso contrário, desça.
                        self.__descer_andar(andar_desejado)
                    
                    sleep(1) #Chamando função 'sleep()' para apresentar delay de 1 segundo.
                    print(f"\nChegamos no {andar_desejado}° andar!")
            
            else:
                Elevador.error_andar_inexistente()
        
        else:
            Elevador.error_andar_inexistente()
    
    #Função responsável por subir o elevador.
    def __subir_andar(self, andar_desejado):
        
        #Contado criado apenas para mostrar a primeira mensagem de aviso.
        counter = 0

        while self.localizacao_andar != andar_desejado:

            if counter == 0:
                print(f"\nEstamos subindo para o {andar_desejado}° andar!\n")
            else:
                sleep(1)
                print(f"Andar atual: {self.localizacao_andar}")
                self.localizacao_andar +=1

            counter += 1

    #Função responsável por descer o elevador.
    def __descer_andar(self, andar_desejado):

        counter = 0

        while self.localizacao_andar != andar_desejado:

            if counter == 0:
                print(f"\nEstamos descendo para o {andar_desejado}° andar!\n")
            else:
                sleep(1)
                print(f"Andar atual: {self.localizacao_andar}")
                self.localizacao_andar -=1
                
            counter -= 1

    @staticmethod
    def error_andar_inexistente():
        print("\nAndar inexistente!")