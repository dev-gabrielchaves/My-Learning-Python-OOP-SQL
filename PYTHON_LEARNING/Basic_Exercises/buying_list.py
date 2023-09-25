import os

buying_list = []

while True:

    option = input("\nChoose an option:\n[i]nsert | d[elete] | [l]ist | [o]ut\n").lower()

    if option == 'i':
        os.system('cls')
        add_element = input("\nWrite what you want to insert" \
                            " in your list: ")
        buying_list.append(add_element)
    elif option == 'd':
        os.system('cls')
        try:
            del_element = int(input("\nWrite the index of the element" \
                                " you want to delete: "))
            del buying_list[del_element]
        except:
            print("\nYou did not write a valid index.")
            continue
    elif option == 'l':
        os.system('cls')
        indexes = range(len(buying_list))
        if len(buying_list) == 0:
            print("The list has 0 elements!")
            continue
        for index in indexes:
            print(index, "-", buying_list[index])
    elif option == 'o':
        break
    else:
        os.system('cls')
        print("\nType a valid option!")
print("\nBye!")