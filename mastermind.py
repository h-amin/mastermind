def beoordelingsfunctie():
    kleuren = ["rood", "blauw", "groen", "groen"]  # V.B.
    random_gok = ["rood", "paars", "groen", "geel"]
    feedback = []
    for i in range(len(kleuren)):
        if kleuren[i] == random_gok[i]:
            feedback.append("zwart")
        elif random_gok[i] in kleuren:
            feedback.append("wit")
        else:
            feedback.append("null")
    print(feedback)


beoordelingsfunctie()