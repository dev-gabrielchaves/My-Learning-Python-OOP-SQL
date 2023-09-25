name = 'Gabriel'
age = 24
height = 1.82
weight = 80

bmi = weight/height**2
reduced_bmi = round(bmi, 2)

first_line = f'Hello {name}!'
second_line = f'You\'re {age} years old, and your BMI is: {bmi:.2f}!'

#First way to do, just to exemplify how to format Strings
print(first_line)
print(second_line)

print('\nHello', name + '!')
print("You're", age, 'years old, and your BMI is:', str(reduced_bmi) + '!')