number = int(input())
price = 0

if number <= 10:
    price = 7
elif number <= 30 and number >= 11:
    price = (number - 10) + 7
elif number <= 100 and number >= 31:
    price = (number - 30) * 2 + 27
else:
    price =  (number - 100) * 5 + 167
 
print(price)