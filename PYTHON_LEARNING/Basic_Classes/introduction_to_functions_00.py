"""
Introduction to Functions (def) in Python
Functions are code blocks used to
replicate a specific action throughout your code.
They can receive values as parameters (arguments)
and return a specific value.
By default, Python functions return None.
"""

# def Print(a, b, c):
#     print('Multiple1')
#     print('Multiple2')
#     print('Multiple3')
#     print('Multiple4')

# def print_values(a, b, c):
#     print(a, b, c)


# print_values(1, 2, 3)
# print_values(4, 5, 6)

def greeting(name='Unnamed'): #In this case, 'name' is a parameter
    print(f'Hello, {name}!')


greeting('Luiz Otávio') #Here 'Luiz Otávio' is the argument
greeting('Maria')
greeting('Helena')
greeting()