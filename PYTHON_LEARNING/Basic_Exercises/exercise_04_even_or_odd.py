number_str = input("Type an integer: ")

try: 
    number_int = int(number_str)
    if number_int % 2 == 0:
        print("\nThe number you typed is even.")
    else:
        print("\nThe number you typed is odd.")
except:
    print("\nYou did not type an integer.")