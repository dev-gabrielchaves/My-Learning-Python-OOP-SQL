#If we want a list immutable we can use a 'tuple'

names = 'Gabriel', 'João', 'Carla'
# names[0] = 'Hey' ---> You can't do that
print(names)
#But you can convert a tuple into a list
names_list = list(names)
print(names_list)
#You can do the oposite as well
names_tuple_again = tuple(names)
print(names_tuple_again) 