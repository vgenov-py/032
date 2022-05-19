### Bookshop

1. Código legible
2. Utilizar **o** una función para cada tipo de búsqueda o 2 funciones una para id y otra para autor, título y género
3. La búsqueda salvo por el parámetro id debe ser relativa y case-insensitive:
* "Jack lo" debería entregar **todos** los libros de Jack London

#### Búsqueda por género
1. Lista los géneros disponibles
```python
"1. Narrativa extranjera"
"2. Narrativa policíaca"
```
2. Buscar en base al género selecionado por el usuario

#### Eliminar y Actualizar libros DELETE & UPDATE

1. Deben aparecer las opciones en el menú principal
```python
"Bienvenido a bookshop"
"1. Buscar por ID"
"2. Buscar por Autor"
"3. Buscar por Título"
"4. Buscar por Materia"
"5. Eliminar libro por ID"
"6. Actualizar libro por ID"
"q. para salir"
```
2. Para eliminar un libro, introducimos el **ID** y el libro será eliminado
* El libro {title} ha sido eliminado
3. Para actualizar un libro, introducimos el **ID** y mostraremos todas los campos del diccionario
```python
"title: El ingenio de los pájaros"
input("nuevo título: ")
```
* Si el input se deja en blanco no se actualizará el campo