"""
The exercise description:
A class that represents vehicles, as shown in the partially shown diagram below, keeping
information about the vehicle's name, engine power in horsepower, and vehicle weight in kilograms. The class should have:
• Encapsulated attributes, validating the values to be stored (define valid ranges for power
and weight);
• Constructor, receiving the initial values for all attributes;
• Access methods (getters and setters) for all attributes;
• Method to calculate the ratio between weight and power, given in hp/kg;
• ToString method or __str__ to return the vehicle's data in text format.
Write a program (Main) to test the Vehicle class, allowing the user to enter data for ten
different vehicles and showing, in the end, the data of the vehicle with the lowest ratio between weight and power.
"""

from vehicle import Vehicle
import os

# Defining an empty list called 'vehicles' that will receive all the vehicles that the user will describe...
vehicles = []
# Creating an empty list that will receive every vehicle relation...
vehicles_relations = []

for i in range(3):

    name = input("\nType the name of the vehicle: ")
    power = int(input("Type the amount of power of the vehicle: "))
    weight = float(input("How much does the vehicle weight: "))

#   Creating object 'new_vehicle'...
    new_vehicle = Vehicle(name, power, weight)

#   Adding every relation inside of the list...
    vehicles_relations.append(new_vehicle.power_weight())

    vehicles.append(new_vehicle)

# Getting the minimum value of the list...
min_relation = min(vehicles_relations)
# Getting the index of the element that has the lower relation...
min_relation_index = vehicles_relations.index(min_relation)

os.system('cls')

# Showing the vehicle with the lowest relation... 
print("\nYou can see bellow the attributes of the vehicle with the lower Power/Weight relation:")
print(str(vehicles[min_relation_index]))