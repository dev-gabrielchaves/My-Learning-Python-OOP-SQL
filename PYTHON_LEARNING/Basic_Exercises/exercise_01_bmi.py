print("Hello, welcome to the BMI program!\n")

name = input("What's your name: ")
height = input("Type your height: ")
weight = input("Type your weight: ")

float_height = float(height)
float_weight = float(weight)

bmi = float_weight/float_height**2

print(f"\nHey {name}, your BMI is: {bmi:.2f}!")
