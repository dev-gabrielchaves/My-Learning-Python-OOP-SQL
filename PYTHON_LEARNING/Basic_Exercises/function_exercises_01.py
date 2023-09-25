"""On this code i am going to use some things that are very import to make it easy
'programming', like 'Closure', for example, functions that returns another functions"""
"""So on this code i basically need to create functions that multiply
the given number by '2', '3' and '4', and returns the multiplied number"""

def multiplicator(multiplicator):
    def multiply(number):
        return number * multiplicator
    return multiply

multiply_by_2 = multiplicator(2)
multiply_by_3 = multiplicator(3)
multiply_by_4 = multiplicator(4)


print(multiply_by_2(10), multiply_by_3(10), multiply_by_4(10))