class Vehicle:

    def __init__(self, name: str, power: int, weight: float) -> None:

        if power < 0 or power > 1000:
            raise ValueError("Power should be between 0 and 1000")
        if weight < 0 or weight > 10000:
            raise ValueError("Weight should be between 0 and 10000")

        self.name = name
        self.power = power
        self.weight = weight

    # Defining sets...
    def set_name(self, name: str) -> None:
        self.name = name
    
    def set_power(self, power: int) -> None:
        if power < 0 or power > 1000:
            raise ValueError("Power should be between 0 and 1000")
        self.power = power

    def set_weight(self, weight: float) -> None:
        if weight < 0 or weight > 10000:
            raise ValueError("Weight should be between 0 and 10000")
        self.weight = weight

    # Defining gets...
    def get_name(self) -> str:
        return self.name
    
    def get_power(self) -> int:
        return self.power
    
    def get_weight(self) -> float:
        return self.weight
    
    # Defining the Power/Weight relation...
    def power_weight(self) -> float:
        return self.power/self.weight
    
    def __str__(self) -> str:
        return f'The name of the vehicle is: {self.name}.\nThe weight of the vehicle is: {self.weight}kg.\nThe power of the vehicle is: {self.power}cv.'