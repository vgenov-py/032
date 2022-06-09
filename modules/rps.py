import random as rdm

choices = ["Piedra", "Papel", "Tijera"] # --> 3!
user = ""
choices[1] == choices[1]


while user != "q":
    pc_choice = choices.index(rdm.choice(choices))  # rdm.randint(0,2)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    user = input(": ")
    if not user.isdigit():
        break
    else:        
        user = int(user) - 1
        print("user: ", choices[user])
        print("pc: ", choices[pc_choice])
    if user != pc_choice: # comprobación empate
        if user == len(choices) -1:
            user = -1
        if user + 1 == pc_choice:
            print("PC GANA")
        else:
            print("USER GANA")
    else:
        print("Empate!")

















