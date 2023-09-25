#There you can see a list of numbers
sequence = [1, 2, 3, 4, 5]
#A list can contain different types, like str, int, float, etc.
whatever = [1, 2.5, 'Gabriel', True]
#A list can even contain another list
matrix = [1, 2, 3, [1, 2, 3]]
#Different than Strings, you can access the list and "mutate" it's data
sequence[2] = "I changed!"
print(sequence)
#You can also delete, add, and many more things...
sequence.append("I was added now!") #Adds the element to the end of the list
print(sequence)
del sequence[0] #Deletes the element I choose, and relocates every other...
print(sequence)
last_element = sequence.pop() #Deletes the last element
print(sequence, "Removed:", last_element)
whatever.clear() #Clear the list
print(whatever)
#The method 'insert' inserts an element inside the last, replacing the others
matrix.insert(0, "I am here now!")
print(matrix)
#We use the method 'extend' to extend a list, but we can also concatenate using '+'
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)
list_a.extend(list_b) #This adds the list_b to the list_a
print(list_a)