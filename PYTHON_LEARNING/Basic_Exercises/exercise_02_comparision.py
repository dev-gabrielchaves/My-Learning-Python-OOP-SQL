first = input("Type a value: ")
second = input("Type another value: ")

if first > second:
    print(f'{first} has a higher value than {second}.')
elif first == second:
    print(f'{second} has the same value as {first}.')
else:
    print(f'{second} has a higher value than {first}.')