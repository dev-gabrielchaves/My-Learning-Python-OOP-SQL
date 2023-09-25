from user import User
from repository import Repository
import os

print("Welcome to the user registration program!\n")

repository = Repository()

while True:
    
    try: 
        option = int(input("[1] - Register new user\n" \
                    "[2] - Show list of users\n" \
                        "[0] - Leave\n"))
        os.system('cls')
        
        if option == 1:
            
            try:
                first_name = input("\nWrite the first name: ").replace(" ", "")
                last_name = input("Write the last name: ").replace(" ", "")
                age = int(input("Write the age: "))

                repository.add_user(first_name, last_name, age)

                os.system('cls')

                print("User Registered!\n")

            except:
                print("\nWrite a valid age!\n")

        elif option == 2:
            os.system('cls')
            repository.users_registered()

        elif option == 0:
            os.system('cls')
            print('Bye!')
            break

        else:
            os.system('cls')
            print("Invalid option!\n")
    except:
        os.system('cls')
        print("Invalid option!\n")