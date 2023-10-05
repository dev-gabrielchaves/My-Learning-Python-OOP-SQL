from vehicle import Vehicle
# from typing import Type
from random import randint

class Store:

    def __init__(self, name: str) -> None:
        self.name = name
        self.list_of_vehicles = []
        self.__list_of_ids = []

    def __generate_id(self) -> int:
        
        while True:
            id = randint(1,1000)
            if id not in self.__list_of_ids:
                self.__list_of_ids.append(id)
                break
            else:
                continue
        
        return id

    
    def add_vehicle(self, name: str, power: int, weight: float) -> None:
        new_vehicle = Vehicle(name, power, weight)
        vehicle_id = self.__generate_id()
        dict_new_vehicle = {
            'ID' : vehicle_id,
            'Name' : new_vehicle.name,
            'Power' : new_vehicle.power,
            'Weight' : new_vehicle.weight, 
            'Power/Weight' : new_vehicle.power_weight()
        }
        self.list_of_vehicles.append(dict_new_vehicle)
    
    def list_vehicles(self) -> None:
        if self.list_of_vehicles == []:
            print("There are no vehicles registered yet!\n")
        else:
            for vehicle in self.list_of_vehicles:
                for key in vehicle:
                    print(f'{key} : {vehicle[key]}')
                print()

    def delete_vehicle(self, id: int) -> str:
        for vehicle in self.list_of_vehicles:
            if vehicle['ID'] == id:
                self.list_of_vehicles.remove(vehicle)
                return "Vehicle deleted!\n"
        return "ID not found!\n"

    def modify_vehicle(self, id: int) -> None:
        for i, vehicle in enumerate(self.list_of_vehicles):
            if vehicle['ID'] == id:
                return i