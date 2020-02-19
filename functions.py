def master_list():
    kleuren = ["R", "B", "G", "Y"]
    master_lst = []

    for R in range(len(kleuren)):
        for B in range(len(kleuren)):
            for G in range(len(kleuren)):
                for Y in range(len(kleuren)):
                    master_lst.append([kleuren[R], kleuren[B], kleuren[G], kleuren[Y]])
    return master_lst


def secret_code_generator():
    import random
    kleuren = ["R", "B", "G", "Y"]
    random_secret = []
    for i in kleuren:
        random_secret.append(random.choice(kleuren))
    return random_secret


def random_guess():
    x = input("Please give your combination of the following -> [R B G Y]: ")
    y = x.upper()
    z = [word for line in y for word in line.split()]
    if len(z) != 4:
        print("ERROR: Length of code is not valid. Please try again.")
    return z


def user_secret_code():
    x = input("What will the secret code be? Use the following characters in a random order. [R B G Y]: ")
    y = x.upper()
    z = [word for line in y for word in line.split()]
    if len(z) != 4:
        print("ERROR: Length of code is not valid. Please try again.")
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


def simple_algorithm():
    secret_code = user_secret_code()

    while len(master_list()) > 1:
        random_code = secret_code_generator()

        first_assessment = (beoordelingsfunctie(x=secret_code, y=random_code))

        if first_assessment == (4, 0):
            print("Congratulations! The secret code:", random_code, "has been found!")
            break

        for i in range(len(master_list())):
            random_code_2 = secret_code_generator()

            second_assessment = (beoordelingsfunctie(x=random_code, y=random_code_2))

            if first_assessment != second_assessment:
                master_list().remove(random_code_2)
    return


def finding_index(x):

    for i in range(len(master_list())):
        if master_list()[i] == x:
            return i


def worst_case_guess():  # Have to find all 'AABB' combinations, cause these questions have the smallest partition
    # element size.
    import random
    worst_case_lst = []
    for i in master_list():
        if i[0] == i[1] and i[2] == i[3]:
            worst_case_lst.append(i)
    for i in worst_case_lst:
        if i[0] == i[1] and i[1] == i[2] and i[2] == i[3]:
            worst_case_lst.remove(i)

    worst_case_attempt = random.choice(worst_case_lst)
    return worst_case_attempt


def worst_case_algorithm():
    master_list().insert(0, worst_case_guess())
    secret_code = user_secret_code()

    while len(master_list()) > 1:
        random_code = secret_code_generator()

        first_assessment = (beoordelingsfunctie(x=secret_code, y=random_code))

        if first_assessment == (4, 0):
            print("Congratulations! The secret code:", random_code, "has been found!")
            break

        for i in range(len(master_list())):
            random_code_2 = secret_code_generator()

            second_assessment = (beoordelingsfunctie(x=random_code, y=random_code_2))

            if first_assessment != second_assessment:
                master_list().remove(random_code_2)
    return
