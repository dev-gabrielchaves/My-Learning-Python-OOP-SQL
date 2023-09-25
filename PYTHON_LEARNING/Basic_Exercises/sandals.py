#Question of the 'OBI 2023' called 'Chinelos', or in english: 'Sandals'

try:

    counter = 0

    number_of_sizes = int(input())
    sizes = []

    for i in range(number_of_sizes):

        how_many_of_a_size = int(input())
        sizes.append(how_many_of_a_size)

    number_of_orders = int(input())

    for i in range(number_of_orders):

        size_of_choice = int(input())

        if sizes[size_of_choice-1] > 0:
            
            sizes[size_of_choice-1] -= 1
            counter += 1
    
    print(counter)

except:
    ...