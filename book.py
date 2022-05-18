user = ""

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
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
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
    "author": "Joseph Conrad",
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
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genre = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]

def menu():
    print("Bienvenido a bookshop")
    print("1. Buscar por ID")
    print("2. Buscar por Autor")
    print("3. Buscar por Título")
    print("4. Buscar por Materia")
    print("q. para salir")

def get_by_id(book_id):
    book_id = input("id: ")
    for book in DB:
        if book["id"] == book_id:
            return book
    else:
        print("No hemos encontrado nada")

def pretty_book(book):
    for k,v in book.items():
        print(f"{k}: {v}")

def not_found(element):
    if element:
        pretty_book(element)
    else:
        print(f"No hemos encontrado nada")

####### UI/UX:

while user != "q":
    menu()

    user = input(": ")
    if user == "1":
        book_id = input("id: ")
        book = get_by_id(book_id)
        not_found(book)
        
        input()

        
