kleuren = ["R", "B", "G", "Y"]
random_gok = []

n = 0
while n < 11:
    x = input("Geef hier uw random gok, keuze uit [R B G Y]: ")
    y = x.upper()
    z = list(y)

    if len(z) != 4:
        print("ERROR: lengte van opgegeven code is ongeldig.")
        n += 1
    else:
        random_gok.append(z)
        n += 1
print("GAME OVER")