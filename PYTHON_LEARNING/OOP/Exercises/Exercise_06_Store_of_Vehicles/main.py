from vehicle import Vehicle
from store import Store
import os

store = Store("California Vehicles")

while True:
    choice = input(
        "Choose an option:\n\n"
        "[0] - Leave\n" \
        "[1] - Add Vehicle\n" \
        "[2] - List Vehicles\n"
        "[3] - Delete Vehicle\n"
        "[4] - Change Vehicle Specs\n")

    if choice == "0":
        os.system("cls")
        print("Bye!")
        break
    
    elif choice == "1":
        os.system("cls")
        name = input("Type the vehicle name: ")
        power = int(input("Type the vehicle power: "))
        weight = float(input("Type the vehicle weight: "))
        os.system("cls")

        store.add_vehicle(name, power, weight)
    
    elif choice == "2":
        os.system("cls")
        store.list_vehicles()
    
    elif choice == "3":
        os.system("cls")
        store.list_vehicles()
        id = int(input("Type the ID of the vehicle you want to delete: "))
        os.system("cls")
        print(store.delete_vehicle(id))

    elif choice == "4":
        os.system("cls")
        store.list_vehicles()
        id = int(input("Type the ID of the vehicle you want to modify: "))
        choice_modify = input(
        "\nChoose an option:\n\n"
        "[1] - Change Name\n" \
        "[2] - Change Power\n" \
        "[3] - Change Weight\n")

        if choice_modify == "1":
            os.system("cls")
            new_name = input("Set the new name: ")
            store.list_of_vehicles[store.modify_vehicle(id)]['Name'] = new_name
            os.system("cls")
            
        elif choice_modify == "2":
            os.system("cls")
            new_power = int(input("Set the new power: "))
            store.list_of_vehicles[store.modify_vehicle(id)]['Power'] = new_power
            store.list_of_vehicles[store.modify_vehicle(id)]['Power/Weight'] = new_power/store.list_of_vehicles[store.modify_vehicle(id)]['Weight']
            os.system("cls")
            
        elif choice_modify == "3":
            os.system("cls")
            new_weight = int(input("Set the new weight: "))
            store.list_of_vehicles[store.modify_vehicle(id)]['Weight'] = new_weight
            store.list_of_vehicles[store.modify_vehicle(id)]['Power/Weight'] = store.list_of_vehicles[store.modify_vehicle(id)]['Power']/new_weight
            os.system("cls")
            
        else:
            os.system("cls")
            print("You did not type a valid option!\n")
    
    else:
        os.system("cls")
        print("Type a valid option!\n")