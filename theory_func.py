def name_func():
    return "Soy una función"

a = [2, 1, 3,4]
# sorted() - list.sort()
b = sorted(a)
# print(b)

def sort():
    "ordeno la lista"

a.sort()
# print(a)

def vito_sorted():
    return "Lista ordenada"

b = vito_sorted()
# print(b)

def vito_sort():
    "Ordenar la lista"

b = vito_sort()
# print(b)

def greeting(name):
    return f"Hola {name}!"

# print(greeting("Roberto"))


# crear una función que eleve al cuadrado un número 
# crear una función que reciba una lista y que devuelva los cubos de sus números [num]

def square(num):
    return num ** 2
    return "otra cosa"

def cube_list(lista):
    if type(lista) == list or type(lista) == tuple:
        return [num ** 3 for num in lista]
    return "Debe introducir una lista"


a = [1,2,3,4]
b = cube_list("(1,2,3,4)")
# print(b)

### Función con dos parámetros

def add(x, y):
    result =  x + y
    return result

