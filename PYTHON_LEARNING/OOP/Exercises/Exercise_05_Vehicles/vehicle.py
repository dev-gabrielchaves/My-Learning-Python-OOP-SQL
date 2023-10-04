class Vehicle:

    def __init__(self, name: str, power: int, weight: float) -> None:

        if power < 0 or power > 1000:
            raise ValueError("Power should be between 0 and 1000")
        if weight < 0 or weight > 10000:
            raise ValueError("Weight should be between 0 and 10000")

        self.__name = name
        self.__power = power
        self.__weight = weight

    # Defining sets...
    def set_name(self, name: str) -> None:
        self.__name = name
    
    def set_power(self, power: int) -> None:
        if power < 0 or power > 1000:
            raise ValueError("Power should be between 0 and 1000")
        self.__power = power

    def set_weight(self, weight: float) -> None:
        if weight < 0 or weight > 10000:
            raise ValueError("Weight should be between 0 and 10000")
        self.__weight = weight

    # Defining gets...
    def get_name(self) -> str:
        return self.__name
    
    def get_power(self) -> int:
        return self.__power
    
    def get_weight(self) -> float:
        return self.__weight
    
    # Defining the Power/Weight relation...
    def power_weight(self) -> float:
        return self.__power/self.__weight
    
    def __str__(self) -> str:
        return f'The name of the vehicle is: {self.__name}.\nThe weight of the vehicle is: {self.__weight}kg.\nThe power of the vehicle is: {self.__power}cv.'