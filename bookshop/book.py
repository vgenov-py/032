
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
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera",
    "ISBN": "978810392812"
},
]

genres = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]

def menu():
    print("Bienvenido a bookshop")
    print("1. Buscar por ID")
    print("2. Buscar por Autor")
    print("3. Buscar por Título")
    print("4. Buscar por Materia")
    print("5. Eliminar libro por ID")
    print("6. Actualizar libro por ID")

    print("q. para salir")

def get_by_id(book_id):
    for book in DB:
        if book["id"] == book_id:
            return book

    # un comentario
    # otro comentario
    # tercer comentario
# Búsqueda relativa
# Retornar lista
# insensitive /i


def pretty_book(book):
    for k,v in book.items():
        print(f"{k}: {v}")

def get_by_param(user_input, book_param): # author, title, genre LO QUE EL USUARIO DIGA
    result = []
    user_input = user_input.lower()
    for book in DB:
        if book[book_param].lower().find(user_input) >= 0:
            result.append(book)
    return result

def user_option(msg, book_param):
    user_input = input(msg)
    books = get_by_param(user_input, book_param)
    for book in books:
        pretty_book(book)
        
        input("\nSiguiente\n")

'''
1. usuario elige una opción
2. uso get_by_param con lo que el usuario me diga

# género

1. usuario elige una opción
2. listo los géneros
3. extraigo el género que el usuario haya indicado
4. uso get_by_param con lo que el usuario me diga 


CREATE
READ
UPDATE
DELETE


'''

# WET & DRY 
# Write Everythin Twice
# Don't Repeat Yourself



####### UI/UX:

while user != "q":
    menu()

    user = input(": ")
    if user == "1":
        book_id = input("id: ")
        book = get_by_id(book_id)
        if book:
            pretty_book(book)
        else:
            print(f"No hemos encontrado el libro por el ID: {book_id}")
        input(": ")

    elif user == "2":
        user_option("Author: ", "author")
    
    elif user == "3":
        user_option("Title: ", "title")
        
    elif user == "4":
        for i, genre in enumerate(genres): # 
            print(f"{i + 1}. {genre}")
        user = int(input(": ")) - 1
        books = get_by_param(genres[user], "genre")
        for book in books:
            pretty_book(book)         
            input("\nSiguiente\n")

    elif user == "5":
        book_id = input("ID: ")
        # book_to_delete = get_by_id(book_id)
        # if book_to_delete:
        #     DB.remove(book_to_delete)
        #     print(f"El libro '{book_to_delete['title']}' ha sido eliminado")
        # else:
        #     print(f"No hemos encontrado el libro por ID: {book_id}")
        # input(": ")
        '''
        ALTERNATIVA get_by_param():
        '''
        book_to_delete = get_by_param(book_id, "id")
        if len(book_to_delete) == 1:
            book_to_delete = book_to_delete[0]
            DB.remove(book_to_delete) # DB.pop(DB.index(book_to_delete))            
            print(f"El libro '{book_to_delete['title']}' ha sido eliminado")
        else:
            print(f"No hemos encontrado el libro por ID: {book_id}")
        input(": ")
        
    elif user == "6":
        book_id = input("ID: ")
        book_to_update = get_by_id(book_id)
        pretty_book(book_to_update)
        if book_to_update:
            for k,v in tuple(book_to_update.items())[1:]: # Big O notation O(6) == O(1)
                new_v = input(f"New {k} ({v}): ")
                if new_v:
                    book_to_update[k] = new_v                
