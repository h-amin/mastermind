import random

mastermind_secret_code = "GGBR"
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


def beoordelingsfunctie():  # Systeem vs gebruiker
    random_gok = input("geef hier uw gok: ")
    feedback = []  # Feedback is zwart = 2, wit = 1, null = 0
    for i in range(len(master_lst)):
        if mastermind_secret_code[i] == random_gok[i]:
            feedback.append(2)
        elif random_gok[i] in mastermind_secret_code:
            feedback.append(1)
        else:
            feedback.append(0)
    for j in feedback:
        print(j, end="")


beoordelingsfunctie()

