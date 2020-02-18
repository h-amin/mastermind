import random

mastermind_secret_code = 'G G B R'
kleuren = ["R", "B", "G", "Y"]
master_lst = []
random_code = []

for R in range(len(kleuren)):
    for B in range(len(kleuren)):
        for G in range(len(kleuren)):
            for Y in range(len(kleuren)):
                master_lst.append([kleuren[R], kleuren[B], kleuren[G], kleuren[Y]])
random_code.append(random.choice(master_lst))
print(random_code)


def beoordelingsfunctie():  # Functie dat feedback weergeeft op de random_gok uit kleuren lijst.
    random_gok = input("geef hier uw gok: ")
    feedback = []  # Feedback is 1. zwart, 2. wit of 3. null
    for i in range(len(master_lst)):
        if kleuren[i] == random_gok[i]:
            feedback.append("zwart")
        elif random_gok[i] in kleuren:
            feedback.append("wit")
        else:
            feedback.append("null")
    for j in feedback:
        print(j)


beoordelingsfunctie()

