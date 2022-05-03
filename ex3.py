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


a = [5,6,7,8]    
lista_de_cuadrados = [None, None, None, None]
for i, num in enumerate(a):
    lista_de_cuadrados[i] = num ** 2
# print(lista_de_cuadrados)
for i, num in enumerate(lista_de_cuadrados):
    print(f"I: {i}, V: {num}")

# simular count 
fruits = ['apple', 'banana', 'cherry', "apple"]

count = 0
search_term = "apple"
for element in fruits:
    if element == search_term:
        count += 1

print(count)