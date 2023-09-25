from user import User

class Repository:
    
    def __init__(self) -> None:
        self.list_of_users = []
    
    def add_user(self, first_name: str, last_name: str, age: int) -> None:
        new_user = User(first_name, last_name, age)
        dict_new_user = {
            'First Name' : new_user.first_name,
            'Last Name' : new_user.last_name,
            'Age' : new_user.age
        }
        self.list_of_users.append(dict_new_user)
    
    def users_registered(self) -> None:
        if self.list_of_users == []:
            print("No user registered!\n")
        else:
            for user in self.list_of_users:
                for key in user:
                    print(f'{key}: {user[key]}')
                print()