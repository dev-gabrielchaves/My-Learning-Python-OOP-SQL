def addTwoNumbers(l1, l2):
    
    inv_l1_number = ''
    inv_l2_number = ''

    len_l1 = len(l1)
    len_l2 = len(l2)

    for i in range(len_l1, 0, -1):
        inv_l1_number += str(l1[i-1])

    for i in range(len_l2, 0, -1):
        inv_l2_number += str(l2[i-1])

    inv_l3_number = int(inv_l1_number) + int(inv_l2_number)

    inv_l3 = list(str(inv_l3_number))

    inv_l3.reverse()

    l3 = []

    for i in inv_l3:
        l3.append(int(i))

    return l3

lista1 = [9,9,9,9,9,9,9]
lista2 = [9,9,9,9]

print(addTwoNumbers(lista1, lista2))