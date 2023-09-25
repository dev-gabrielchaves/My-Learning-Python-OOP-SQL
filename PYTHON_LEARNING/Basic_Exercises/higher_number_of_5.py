higher_number = 0
counter = 0

while counter < 5:

    number = int(input("Type a number: "))

    if counter == 0:
        higher_number = number
    if number > higher_number:
        higher_number = number
    
    counter = counter + 1
    
print(f'\nThe higher number you typed is: {higher_number}!')