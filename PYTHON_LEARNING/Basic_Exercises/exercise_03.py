print('Hello!\n')

name = input('Please, type your full name: ')
age = input('Please, type your age: ')

name = name.strip()
age = age.strip()

check_name = name.replace(' ', '')
check_age = age.replace(' ', '')

if (check_name == '') or (check_age == ''):
    print('I am sorry, but you did not type your age or your name.')
else:
    print(f"\nSo, that's your full name: {name}")
    print(f"\nThat's the inverted of your full name: {name[::-1]}")

    if ' ' in name:
        print("There are space(s) in your name.")
    else:
        print("There are not space(s) in your name.")

    print(f'Your name has: {len(check_name)} letters.')
    print(f'The first letter of your name is: {name[0]}')
    print(f'The last letter of your name is: {name[-1]}')