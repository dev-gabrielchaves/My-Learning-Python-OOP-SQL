from elevador import Elevador
import os

elevador = Elevador() #Criei um objeto 'elevador_1' e defini que ele está no 1° andar!


while True:
    
    opcao = input("\nInforme o que você deseja:\n\n" \
                  "0 - Saber o andar atual;\n" \
                    "1 - Locomover o elevador.\n" \
                        "2 - Sair\n")
    
    if opcao == '0':
        os.system('cls')
        elevador.mostrar_andar_atual()

    elif opcao == '1':
        os.system('cls')
        try:
            andar_desejado = int(input("\nInforme o andar desejado: "))
            elevador.locomover(andar_desejado)
        except:
            print("\nAndar inválido!")

    elif opcao == '2':
        os.system('cls')
        break

    else:
        print("\nOpção inválida!")