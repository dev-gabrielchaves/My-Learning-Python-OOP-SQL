list1 = [1, 2, 3, 4, 5]

#using while
counter = 0
while counter < len(list1):
    print(list1[counter] ** 2)
    counter += 1

#using for
for square in list1:
    print(square ** 2)