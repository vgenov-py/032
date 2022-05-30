persona_lista = ["Vito", 28]

persona = {
    "SS": "23443ld903",
    "name": "Vito",
    "id": "asdjk443345sd",
    "dni":"20349234Q",
    "nacionalidad": "Argentina",
    "age": 28,
    "courses": ["Python", "OpenRefine", "R"]
}
persona["age"] += 1
persona.update({"Courses": 1})
persona.update({"couRses": 1})

persona.update({"antique": 1})
persona["email"] = "genovese@email.com"
print(persona)

#keys
# for k in list(persona.keys()):
#     print(k)
#values
# print(persona.values()[4])
# for v in persona.values():
#     print(v)
#items
# a, b, c  = [1,2,3]
# for i, v in enumerate(persona_lista):
#     print(i, v)

# for k,v in persona.items():
#     if k == "age":
#         persona["age"] += 1
#     elif k == "courses":
#         persona["courses"] = []

# print(persona["age"])
# print(persona["courses"])
