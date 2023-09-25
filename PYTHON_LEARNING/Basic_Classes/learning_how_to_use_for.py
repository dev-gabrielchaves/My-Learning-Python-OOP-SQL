'''text = 'Python'

for letter in text:
    print(letter)

numbers = range(10)

for number in numbers:
    print(number) 
'''
"""
Iterable -> str, range, etc (__iter__)
Iterator -> someone who can deliver one value at a time
next -> give me the next value
iter -> give me your iterator
"""
# for letter in text

text = 'Luiz'  # iterable

# iterator = iter(text)  # iterator

# while True:
#     try:
#         letter = next(iterator)
#         print(letter)
#     except StopIteration:
#         break

for letter in text:
    print(letter)

print(letter)