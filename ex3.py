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

# print(count)

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
unique_numbers = list(set(repeated_numbers))

# unique_numbers.sort()

# print(sorted(unique_numbers))
# print(sorted(unique_numbers, reverse=True))

unique_numbers.sort()
# print(unique_numbers)
unique_numbers.sort(reverse=True)
# print(unique_numbers)

unique_numbers_asc = sorted(unique_numbers)
unique_numbers_desc = sorted(unique_numbers, reverse=True)

# print(sorted(["María", "Pedro", "Jaime", "Vito"]))



# unique_numbers_2 = []

# for num in repeated_numbers:
#     if not num in unique_numbers_2:
#         unique_numbers_2.append(num)
# print(unique_numbers_2)

repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
repeated_numbers_pow = []

# for num in repeated_numbers:
#     repeated_numbers_pow.append(num ** 2)
# print(repeated_numbers_pow)
'''
[lo que queramos hacer con el iterable for element_del_iterable in iterable]
[___ for ___ in ___]
[___ for ___ in ___ if ___]

'''
repeated_numbers_pow_2 = [num**2 for num in repeated_numbers if num]
# print(repeated_numbers_pow_2)


result = 0
for num in repeated_numbers:
    result += num/len(repeated_numbers)

# print(result == sum(repeated_numbers)/len(repeated_numbers))
# sum - max - min
max_num = 0
pos_max_num = None
for i, num in enumerate(repeated_numbers):
    if num > max_num:
        max_num = num
        pos_max_num = i
repeated_numbers[i] = 1000
# print(max_num)
# min(repeated_numbers)

# int
# in range

repeated_numbers[repeated_numbers.index(max(repeated_numbers))] = 1000
# repeated_numbers[22]
repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
# print(repeated_numbers[5: -4])
url = "http://www.unsplash.com/id230495sdflkj203.php"
img_name, img_extension = url.split(".")[-2:]

# if file_extension in ["svg", "jpg", "png"]:
#     print("allowed!")

# print(sum(repeated_numbers[4:10]))
# result = 0
# for num in repeated_numbers[4:10]:
#     result += num
# print(result)

# for n in range(1,10):
#     print(n)
# result = 0

fibo = [0,1]
limit = 15

for _ in range(1, limit):
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)
# i = 1
# while i < limit:
#     fibo.append(fibo[i] + fibo[i - 1])
#     i += 1

n = 10
