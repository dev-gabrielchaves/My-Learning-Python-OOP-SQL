from elevadores import Elevador
import os

elevador_1 = Elevador(1)
elevador_2 = Elevador(1)

elevadores = [elevador_1, elevador_2]

while True: 

    try:

        escolha_de_elevador = int(input("Escolha que elevador deseja entrar, 1 ou 2: "))

        if escolha_de_elevador == 1 or escolha_de_elevador == 2:
            
            while True:
        
                opcao = input("\nInforme o que você deseja:\n\n" \
                            "0 - Saber o andar atual;\n" \
                                "1 - Locomover o elevador.\n" \
                                    "2 - Sair\n")
                
                if opcao == '0':
                    os.system('cls')
                    elevadores[escolha_de_elevador-1].mostrar_andar_atual()

                elif opcao == '1':
                    os.system('cls')
                    try:
                        andar_desejado = int(input("\nInforme o andar desejado: "))
                        elevadores[escolha_de_elevador-1].locomover(andar_desejado)
                    except:
                        print("\nAndar inválido!")

                elif opcao == '2':
                    os.system('cls')
                    break

                else:
                    print("\nOpção inválida!")

        else:
            print("Elevador inexistente")
            break

    except:

        print("Elevador inexistente")
        break