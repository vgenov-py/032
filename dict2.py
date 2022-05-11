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


print(best_grade_students)