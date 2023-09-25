name = input("Type your name: ")
name_size = len(name)

counter = 0

while counter < name_size:
    print(f'*{name[counter]}', end='')
    counter += 1
