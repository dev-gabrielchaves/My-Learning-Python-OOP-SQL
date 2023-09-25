import random

try:
    value = int(input("How many CPF's you wanna generate: "))

    for i in range(value):
        generated_cpf = ''

        for i in range(9):
            generated_number_str = str(random.randint(0, 9))
            generated_cpf += generated_number_str

        #Calculating the first number of the CPF

        countdown = 10
        first_number = 0

        for i in range(9):
            first_number += int(generated_cpf[i]) * countdown
            countdown -= 1

        first_number *= 10

        if first_number % 11 > 9:
            first_number = 0
        else:
            first_number = first_number % 11

        #Including the first number into our generated CPF
        generated_cpf += str(first_number)

        #Calculating the second number of the CPF

        countdown = 11
        second_number = 0

        for i in range(10):
            second_number += int(generated_cpf[i]) * countdown
            countdown -= 1

        second_number *= 10

        if second_number % 11 > 9:
            second_number = 0
        else:
            second_number = second_number % 11

        generated_cpf += str(second_number)

        #Showing our generated CPF

        print(f'The generated CPF is: {generated_cpf[0:3]}.{generated_cpf[3:6]}.' \
            f'{generated_cpf[6:9]}-{generated_cpf[9:11]}')
except:
    print("Type a valid number!")