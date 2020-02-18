kleuren = ["R", "B", "G", "Y"]
random_gok = []

n = 0
while n <= 10:
    x = input("Geef hier uw random gok, keuze uit [R B G Y]: ")
    y = x.upper()
    z = list(y)

    if len(z) == 4:
        if z in kleuren:
            for i in z:
                random_gok.append(i)
        else:
            print("Error: Letter komt niet voor in lijst.")

    else:
        print("Error: U mag alleen 4 letter combinaties gebruiken.")
    print(random_gok)