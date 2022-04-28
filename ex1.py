pwd = " " # Debe ser str, contraseña válida

# ENTENDER, RESOLVER, PROGRAMAR
if len(pwd) >= 8:
    print("Length OK")

if pwd.find(" ") == -1:
    print("Spaces OK")

if not pwd.isdigit() and not pwd.isalpha() and pwd.isalnum():
    print("Numbers OK")
    print("Letters OK")

a = "murcielago"

# Cómo con un bucle
# DRY - WET

a = a.replace("a", "2")
a = a.replace("e", "4")
a = a.replace("i", "8")
a = a.replace("o", "16")
a = a.replace("u", "32")

# print(a)

a += "kwargs" * len(a)
a += "1"


if len(a) % 2 != 0:
    print("")
    len_a = len(a)
    position = len_a / 2
    # position = round(position) # Incierto
    position = int(position)
    print(a[position])
    # iterable[position: int]
else:
    b = "75"
    a += b

print(a)
    