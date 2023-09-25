"""Using '*args' as the function parameter, the function can receive infinite
arguments. These arguments will be saved in a tuple, but you can change that,
as you will see"""

"""First exercise"""
def multiply(*args):
    args = list(args)#Here i am converting the tuple into a list, even tough it was not necessary in this case
    total = 1
    for number in args:
        total *= number
    return total

value = multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(value)

"""Second exercise"""
def even(number):
    if number % 2 == 0:
        return 'even'
    return 'odd'

number = even(5)
print(number)