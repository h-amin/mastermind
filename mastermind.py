import random

mastermind_secret_code = ["G", "G", "B", "R"]
print(mastermind_secret_code)
kleuren = ["R", "B", "G", "Y"]
master_lst = []
random_code = []

for R in range(len(kleuren)):
    for B in range(len(kleuren)):
        for G in range(len(kleuren)):
            for Y in range(len(kleuren)):
                master_lst.append([kleuren[R], kleuren[B], kleuren[G], kleuren[Y]])
random_code.append(random.choice(master_lst))

def beoordelingsfunctie():  # Systeem vs gebruiker
    random_gok = input("geef hier uw gok: ")
    n = list(random_gok)
    print(n)
    zwart_pin = 0
    wit_pin = 0
    feedback = []  # Feedback is zwart = 2, wit = 1, null = 0
    for i in range(len(mastermind_secret_code)):
        if mastermind_secret_code[i] == n[i]:
            zwart_pin += 1
        elif n[i] in mastermind_secret_code:
            wit_pin += 1
    return zwart_pin, wit_pin


c = beoordelingsfunctie()
zwart_pin = c[0]
wit_pin = c[1]
print("Zwart is", zwart_pin, "Wit is", wit_pin)