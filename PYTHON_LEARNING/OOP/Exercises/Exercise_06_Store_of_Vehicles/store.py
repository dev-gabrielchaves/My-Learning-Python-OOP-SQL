from vehicle import Vehicle
# from typing import Type
from random import randint

class Store:

    def __init__(self) -> None:
        self.__list_of_vehicles = []
    
    def add_vehicle(self, name: str, power: int, weight: float) -> None:
        new_vehicle = Vehicle(name, power, weight)
        id = randint(1,1000)
        dict_new_vehicle = {
            'ID' : id,
            'Name' : new_vehicle.name,
            'Power' : new_vehicle.power,
            'Weight' : new_vehicle.weight, 
            'Power/Weight' : new_vehicle.power_weight()
        }
        self.__list_of_vehicles.append(dict_new_vehicle)
    
    def list_of_vehicles(self) -> None:
        for vehicle in self.__list_of_vehicles:
            for key in vehicle:
                print(f'{key} : {vehicle[key]}')
            print()

store_1 = Store()

store_1.add_vehicle('Car 1', 750, 1400)
store_1.add_vehicle('Car 2', 550, 3000)
store_1.add_vehicle('Car 3', 700, 2300)

store_1.list_of_vehicles()