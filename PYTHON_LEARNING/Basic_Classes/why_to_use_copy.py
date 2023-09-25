"""
Be careful with mutable data
= - value is copied (immutable)
= - points to the same value in memory (mutable)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #If not used, once i changed change list_a, list_b will change as well

lista_a[0] = 'Anything'

print(lista_a)
print(lista_b)