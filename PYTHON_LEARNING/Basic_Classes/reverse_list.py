list1 = [1, 2, 3, 4, 5]

#using while
counter = len(list1)
while counter > 0:
    print(list1[counter-1])
    counter -= 1

#using the function reverse
list1.reverse()
print(list1)

#using slicing
list1 = list1[::-1]
print(list1)#reverse of the reverse