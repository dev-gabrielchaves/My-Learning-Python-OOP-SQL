class Vehicle:

    def __init__(self, name: str, power: int, weight: float) -> None:

        if power < 0 or power > 1000:
            raise ValueError("Power should be between 0 and 1000")
        if weight < 0 or weight > 10000:
            raise ValueError("Weight should be between 0 and 10000")

        self.name = name
        self.power = power
        self.weight = weight

    # Defining the Power/Weight relation...
    def power_weight(self) -> float:
        return self.power/self.weight