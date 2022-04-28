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

counter = 0
while counter <= 20:
    print(counter)
    counter += 2

counter = 1
while counter <= 20:
    if counter % 2 == 0:
        print(counter)
    counter += 1