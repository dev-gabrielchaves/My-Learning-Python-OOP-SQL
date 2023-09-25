import random

print('Hello, welcome to the "GUESS WHICH NUMBER" game!\n')

random_number = random.randint(0,100)
#print(random_number)

contador = 0

while contador == 0:
 
    number_int = int(input('Try a number: '))

    if number_int < random_number:
        print('The number you typed is lower than the generated number, try it again!\n')
    elif number_int > random_number:
        print('The number you typed is higher than the generated number, try it again!\n')
    else:
        print("Congrats, you made it!\n")
        contador = 1