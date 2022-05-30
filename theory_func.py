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

def sumar():
    print( 1 + 1)

def sumar_2():
    return 1 + 1

# a = sumar()
# print(a)

a = sumar_2()
# print(a)
stock = ["intenso", "ristretto"]
def nespresso(cap_space):
    temp = 80
    return f"Café {cap_space} recién hecho a {temp} grados"

# print(nespresso("de la India"))
# print("Fin")

data = ["cosas"]

a = {"a": 2}
c = 3
def b(a):
    c
    return a

b(a)
# print(a)

def add(a,b):
    return a + b


def concatenar(a, b):
    return add(a,b)

print(concatenar("a","b"))