# lista = ["Jose", "Pedro", "Raúl", "María"]

# i = 0
# while i < len(lista):
#     # print(lista[i])
#     i += 1

# # for name in lista: 
# #     print(f"Nombre: {name}") # Nombre: Jose
# #     print("Nombre: " + name)
# # print("Fin de la iteración")






# # lista_de_cuadrados = [None]
# # lista_de_cuadrados[0] = a[0] ** 2
# # print(lista_de_cuadrados)
# # for num in a:
# #     lista_de_cuadrados.append(num ** 2)
# # print(lista_de_cuadrados)
# # b = []
# # for num in a:
# #     b.append(num**2)
# # print(b)



# i = 0
# for num in a:
#     lista_de_cuadrados[i] = num ** 2
#     i += 1
# print(lista_de_cuadrados)

# utilizar la función enumerate y para esto tenemos que entender unpack

'''
1. Guardar en una nueva lista los cuadrados de a [25, 36, 49, 64]
2. Imprimir los valores de la nueva lista y sus respectivas posiciones (índices):
I: {i}, V: {v}

1. lista_de_cuadrados
 + for 
 + append
 + num ** 2
'''


from enum import unique
import re


a = [5,6,7,8]    
lista_de_cuadrados = [None, None, None, None]
for i, num in enumerate(a):
    lista_de_cuadrados[i] = num ** 2
# print(lista_de_cuadrados)
for i, num in enumerate(lista_de_cuadrados):
    # print(f"I: {i}, V: {num}")
    pass

# simular count 
fruits = ['apple', 'banana', 'cherry', "apple"]
fruits.count("apple") # --> 2

count = 0
search_term = "apple"
for element in fruits:
    if element == search_term:
        count += 1

print(count)

# simular index
# un elemento a buscar y debemos devolver su posición (int)
# debemos usar un for

fruits = ['apple', 'banana', 'cherry', "apple"]
search_term = "apple"
# print(list(enumerate(fruits)))

# enumerate_fruits = []
# i = 0
# for element in fruits:
#     enumerate_fruits.append((i, element))
#     i += 1

# print(enumerate_fruits)
'''
continue
break
pass
'''

if 1 == 1:
    pass

for i, element in enumerate(fruits):
    if element == search_term:
        pos = i
        break
 
        # continue

# print(f"La posición de {search_term} es {pos}")
# print(f"El método index dice que la posición de {search_term} es {fruits.index(search_term)}")

repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98, 891]
unique_numbers = set(repeated_numbers)
print(repeated_numbers)
print(unique_numbers)


unique_numbers_2 = []

for num in repeated_numbers:
    if not num in unique_numbers_2:
        unique_numbers_2.append(num)
# print(unique_numbers_2)