def master_list():
    import random
    kleuren = ["R", "B", "G", "Y"]
    master_lst = []
    random_code = []

    for R in range(len(kleuren)):
        for B in range(len(kleuren)):
            for G in range(len(kleuren)):
                for Y in range(len(kleuren)):
                    master_lst.append([kleuren[R], kleuren[B], kleuren[G], kleuren[Y]])
    random_code.append(random.choice(master_lst))
    return random_code


def random_guess():
    x = input("Geef hier uw random gok, keuze uit [R B G Y]: ")
    y = x.upper()
    z = [word for line in y for word in line.split()]
    if len(z) != 4:
        print("ERROR: lengte van opgegeven code is ongeldig.")
    return z


def beoordelingsfunctie(x, y):

    black_pin = 0
    white_pin = 0
    temporary_lst = []

    for i in range(len(x)):
        temporary_lst.append(x[i])

        if y[i] == x[i]:
            black_pin += 1
            temporary_lst.remove(x[i])

    for i in range(len(x)):
        if y[i] in temporary_lst:
            temporary_lst.remove(y[i])
            white_pin += 1

    return black_pin, white_pin


c = beoordelingsfunctie(x=["G", "G", "B", "R"], y=random_guess())
zwart_pin = c[0]
wit_pin = c[1]
print("Zwart is", zwart_pin, "Wit is", wit_pin)
