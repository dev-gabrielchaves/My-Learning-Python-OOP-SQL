user = {
    'gabriel': 'gtchaves',
    'joão': 'atelogo',
    'roberto': 'betinho',
    'carla': 'seila123'
}

#I can also create outside of the dictionary new keys with new values
user['rodolfo'] = 'bet355'

#Here you can see how to show both name and nickname using the for loop
for key in user:
    print(f'{key}: {user[key]}')

#Here you can see another way to do it!
#But better, because you have more 'control' over the variables
for user, nick in user.items():
    print(user.title() + ": " + nick)