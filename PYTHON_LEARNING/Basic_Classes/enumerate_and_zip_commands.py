#Let's suppose that we have two lists
sellers = ['Maria', 'Gabriel', 'João', 'Roberto']
how_much_each_seller_sold = [15, 10, 25, 40]

#And let's suppose that that the second list represents how much each seller
#of the first list sold, respectivelly, how do we print that? Well there is some ways:

#First way is this one, using for and range
size_of_list = len(sellers)

for i in range(size_of_list):
    print(sellers[i])
    print(how_much_each_seller_sold[i])

#Second way is using the enumerate()
#The enumerate returns two values, the first a number, and the second the iterable 
#of each element of the list
for i, seller in enumerate(sellers):
    print(seller)
    print(how_much_each_seller_sold[i])

#The third way is using zip()
for selller, how_much in zip(sellers, how_much_each_seller_sold):
    print(seller)
    print(how_much)

print(zip(sellers, how_much_each_seller_sold))