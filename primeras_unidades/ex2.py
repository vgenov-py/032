super_list = ["patata", "platano", "manzana"]

super_list[1] == super_list[-2]

# kwargs --> Key With Arguments

numbers = [2,1,3,4]
# print(numbers)
# numbers.sort(reverse=False)
# print("POS SORT")
# print(numbers)
# print("SORTED:")
# numbers_2 = [5,3,2,4]
# numbers_2 = sorted(numbers_2, reverse=True)
# print(numbers_2)
numbers.append(5)

# print(sum(numbers)/len(numbers))
# print(sum(numbers)/4)
super_list.sort()
# print(super_list)
# print(sorted("palabra"))

# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1 # == counter = counter - 1
#     #goto(24)
# print("Fin")

'''
1. De los números del 1:20 imprimir solo los pares - LEVANTAR MANO
2. De la lista names, imprimir sólo los nombres que empiecen por "c"
names = ["paula", "maría", "andrea", "carla", "carlos"]
3. Hacer el ejercicio anterior case-insensitive
4. Ejercicio strings vowels

while + condición que no supere el indice de la lista + método string + condicional
'''

# counter = 0
# while counter <= 20:
#     print(counter)
#     counter += 2

# counter = 1
# while counter <= 20:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1


names = ["paula", "maría", "andrea", "Carla", "carlos"]
# count = 0
# while count < len(names):
#     name = names[count]
#     if name[0] == "c":
#         print(name)
#     name.startswith("c")
#     name.find("c", 0, 1) == 0
#     count += 1

# counter = 0
# while counter < len(names):
#     name = names[counter]
#     f_letter = name[0]
#     if f_letter == "c" or f_letter == "C":
#         print(name)
#     counter += 1
#     '''
#     if names[counter].startswith("c"):
#         print(names[counter])
#     '''

# counter = 0
# while counter < len(names):
#     if names[counter][0].upper() == "C":
#         print(names[counter])
#     counter += 1

a = "murcielago"
i = 0
vowels = ["a", "e", "i", "o", "u"]

'''
a: 2
e: 4
...32
'''

# while i < len(vowels):
#     po = i + 1
#     a = a.replace(vowels[i], str(2**(po))) # ^
#     i += 1
    
# print(a)

