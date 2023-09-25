print("Welcome to the Calculator!")

while True:
    
    first_number = input("\nType the first number: ")
    second_number = input("Type the second number: ")
    operator = input("Type the operator: ")

    try:
        float_first_number = float(first_number)
        float_second_number = float(second_number)
    except:
        print("\nYou did not write a valid number.")
        continue
    
    if operator == '+':
        print("The result is:", first_number + second_number)
    elif operator == '-':
        print("The result is:", first_number - second_number)
    elif operator == '*':
        print("The result is:", first_number * second_number)
    elif operator == '/':
        print("The result is:", first_number / second_number)
    else:            
        print("\nYou did not type the operator.")

    keep = input("\nDo you want to do another operation? (Yes or No)\n")

    if keep == 'Yes':
        continue
    else:
        break