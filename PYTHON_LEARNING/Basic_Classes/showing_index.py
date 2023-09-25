lista = ['Gabriel', 'João', 'Maria']
counter = 0

#using while
while counter < len(lista):
    print(f'{counter} - {lista[counter]}')
    counter += 1

counter = 0

#using for
for element in lista:
    print(f'{counter} - {element}')
    counter += 1

#whithout counter

indexes = range(len(lista))

for index in indexes:
    print(index, ' ', lista[index])