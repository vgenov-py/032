

m_course = [
    {
	"name": "Patricia",
	"id" :  "001",
    "score": 8.1
    },
    {
	"name": "Nicole",
	"id" :  "002",
    "score": 8.1
    },
    {
	"name": "Javier",
	"id" :  "003",
    "score": 10
    },
    {
	"name": "Verónica",
	"id" :  "004",
    "score": 10
    },
    {
	"name": "Guillermo",
	"id" :  "005",
    "score": 4
    },
    {
	"name": "Pablo",
	"id" :  "006",
    "score": 9
    },
    {
	"name": "Patricia",
	"id" :  "007",
    "score": 2.3
    }
]

a_course = [
    {
        "name": "Germán",
        "id" :  "001",
    "score": 6.8
    },
    {
        "name": "Sara",
        "id" :  "002",
    "score": 8.8
    },
    {
        "name": "Jorge",
        "id" :  "003",
    "score": 3.3
    },
    {
        "name": "María",
        "id" :  "004",
    "score": 9.8
    },
    {
        "name": "Alicia",
        "id" :  "005",
    "score": 5.6
    },
    {
        "name": "Hernesto",
        "id" :  "006",
        "score": 10
    }
]

# print(a_course[-1]["score"])
name_to_find = "maría"
'''
author: vgenov-py
github: vgenov
license: MIT
'''

for student in a_course:
    if student["name"].lower() == name_to_find.lower():
        # print(f'''{student["name"]} - grade: {student['score']}''')
        pass

students = [*m_course, *a_course]
counter = 0
for student in students:
    # if student["name"][0] == "P":
    #     counter += 1
    if student["name"].upper().startswith("P"):
        counter += 1
# print(counter)
# counter= len([student for student in students if student["name"].startswith("P")])

# print(students)

grade = 0
best_grade_students = []
for student in students:
    if student["score"] >= grade:      
        if student["score"] > grade:    
            best_grade_students = [student]
        else:
            best_grade_students.append(student)
        grade = student["score"]

# print(best_grade_students)

to_change_grade = "Alicia"

# for student in m_course:
#     student["id"] = "M" + student["id"]

# for student in a_course:
#     student["id"] = "A" + student["id"]

# print(m_course)

approved = [student for student in students if student["score"]>=6]
# print(approved)
suspended = [student for student in students if student["score"]<6]
# print(suspended)
approved.clear()
suspended.clear()
for student in students:
    if student["score"] >= 6:
        approved.append(student)
    else:
        suspended.append(student)


to_keys = ["A", "B", "C", "D"]
to_values = [1,2,3,4]
new_dict = {}

for i,v in enumerate(to_values):
    new_dict[to_keys[i]] = v

# print(new_dict)

i = 0
for k in to_keys:
    # new_dict[k] = to_values[i]
    # i += 1
    new_dict[k] = to_values[to_keys.index(k)]

for k,v in zip(to_keys, to_values):
    new_dict[k] = v
# [__ for __ in __]
#   v      v    iterable
{}
# {k:v for (k,v) in dict.items()}
a = {"A": 2}
b = {k:v ** 2 for (k,v) in a.items()}
# print(a)
# print(b)

new_dict = {k:v for (k,v) in zip(to_keys, to_values)}
# print(new_dict)


# print(f"Íñtimo: {dict(zip(to_keys, to_values))}")
# print(list(new_dict))

# search_by_name(name), change_id(course, letter), create_dict(lista_keys, lista_values)

def search_by_name(name, course): # 
    for student in course: # 
        if student["name"].lower() == name:
            return student
    return False

# print(m_course) 
def change_id(course, letter):
    for student in course:
        student["id"] = letter.upper() + student["id"]

change_id(m_course, "M")
print(m_course)

def create_dict(lista_keys, lista_values):
    return dict(zip(lista_keys, lista_values))
    dict_to_return = {}
    for i,v in enumerate(lista_values):
        dict_to_return[lista_keys[i]] = v
    return dict_to_return


a = ["A", "B"]
b = ["I", "II"]

dict_ab = create_dict(a,b)
