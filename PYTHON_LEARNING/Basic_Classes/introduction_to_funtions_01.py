"""
Named and Unnamed Arguments in Python Functions
Named arguments have names with an equal sign.
Unnamed arguments only receive the argument (value).
"""

def sum_numbers(x, y, z):
    # Definition
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

sum_numbers(1, 2, 3) #Here for example, we have unnamed arguments
sum_numbers(1, z=2, y=5) #These are named arguments, i can change the order with them

print(1, 2, 3, sep='-')