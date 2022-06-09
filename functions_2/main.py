# funciones anónimas/lambda
# built in functions map - filter - reduce
# generators
# iterable - iterator
# operadores ternarios / ternary operators
# args & kwargs

def greeting(name):
    return f"hola {name}"

lambda name: f"hola {name}"
[num for num in [1,2,3,4]]

maths = {
    "double": lambda num: num ** 2,
    "triple": lambda num: num ** 3,
    "sqrt": lambda num: num ** 0.5
}

def double(num):
    return num ** 2

def triple(num):
    return num ** 3

def f_sqrt(num):
    return num ** 0.5

maths_2 = {
    "double": double,
    "triple": triple,
    "sqrt": f_sqrt
}
def f_add(num_1, num_2):
    return num_1 + num_2
# print(type(f_add))
# f_add = lambda num_1,num_2: num_1 + num_2
# print("------------------------------")
# print(type(f_add))

f_add(1,2) 

# una función lambda:
#   reciba una str
#   return str multiplicada por dos y en mayus upper
# "hola" --> "HOLAHOLA"

lambda word: (word*2).upper()
# una función lambda elevadora:
#   reciba dos int (int_1, int_2)
#   return int_1 ** int_2
#   2, 8 --> 256  
lambda num1,num2: num1 ** num2

# map
a = [1,2,3,4]
b = map(lambda num: num**2,a)
'''
1. un bucle: todo elemento de a es pasado como argumento al parámetro num / for
2. se ejecuta la función / ()
3. se retornan los valores / return
4. se guardan en un iterable / append
'''
def double_list(array):
    result = []
    for num in array:
        result.append(num ** 2)
    return result

c = double_list(a)
# print(b)
# print(zip(a,a))
# print(enumerate(a))
# print(list(b) == c)

DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "genre": "Divulgación científica",
    "author": "Antonio Damasio"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora", # El Poder Del Ahora .title()
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
}
]

# result = list(map(lambda book: book.update({"title": book["title"].title()}), DB))
def book_title(book):
    new_book = book.copy()
    new_book["title"] = new_book["title"].title()
    return new_book

result_2 = list(map(book_title, DB))
# print(DB[0])
# print(result_2)

def title_books(data):
    result = []
    for book in data:
        book["title"] = book["title"].title()
        result.append(book)
    return result

# a = [1,2,3,4]
# b = list(map(lambda num: num ** 2,a))
def double(num):
    return num ** 2
a = [1,2,3,4]
b = list(map(double,a))
# print(b)

'''
1. un bucle: todo elemento de a es pasado como argumento al parámetro num / for
2. se ejecuta la función / ()
3. se retornan los valores / return
4. if statement
5. se guardan en un iterable / append
'''

values = [1,2,3,4]

result = list(filter(lambda num: num %2 == 0, values))
# print(result)

def a(data):
    result = []
    for num in data:
        if num %2 == 0:
            result.append(num)
    return result

values = [1,2,3,4]

def b(num):
    return num %2 == 0
result = list(filter(b, values))
# print(result)

genre_dc = filter(lambda book: book["genre"] == "Divulgación científica",DB)
# print(list(genre_dc))

result = []
for book in genre_dc:
    result.append(book)

values = [1,2,3,4,5,6,7,9]

# Comprobación de Rubén:

filter_values = filter(lambda num: num %2 != 0, values)
# [1,3]
# print(list(filter_values))
# [3]

# print(tuple(zip((1,2,3,4), ("a", "b", "c", "d", "e"))))
a = (1,2,3,4)
b = ("a", "b", "c", "d", "e")
# print(list(map(lambda num1, num2: (num1, num2),a,b)))


values = [1,2,3,4,5,6,7,9]
# elevar al cuadrado los números pares map + filter
# print(list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, values))))

[num ** 2 for num in filter(lambda num: num % 2 == 0, values)]
[num ** 2 for num in values if num % 2 == 0]

# <=
values = [1,2,3,4,5,6,7,9]

# print(sorted(values, reverse=True))

values = {k:k ** 2 for k in values}

values_dict = [{"name": "Vito", "antiguedad": 2}, {"name": "Alvaro", "antiguedad": 1}, {"name": "Candela", "antiguedad": 3}]

print(sorted(values_dict, key=lambda partner: partner["name"]))

map(lambda partner: partner["antiguedad"] ,values_dict)