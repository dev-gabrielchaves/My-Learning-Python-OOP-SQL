'''**********THAT IS HOW I DID**********
secret_word = 'feijao'
size_secret_word = len(secret_word)
main_counter = 0

while True:
    
    counter = 0
    if main_counter == size_secret_word:
        print("\n\nCongrats, you guessed all the letters!\n")
        break

    letter = input("\n\nType the letter: ")
    
    if len(letter) == 1:
        if letter in secret_word:
            while counter < size_secret_word:
                if letter == secret_word[counter]:
                    print(letter, end="")
                    main_counter += 1     
                else:
                    print("_", end="")
                counter += 1
        else:
            print("The letter you typed is not inside of the secret word.")
    else:
        print("You did not type just a letter.")
'''

"""*********THE GAME TAKEN IS IN PORTUGUESE***********
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0