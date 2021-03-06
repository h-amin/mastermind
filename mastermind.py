import functions

print("Hello! welcome to a game of Mastermind code breakers.")
secret_code = functions.secret_code_generator()

while True:
    x = input("Please select a game mode: (1, 2 or help) ")  # 1 = Speler raad, 2 = Systeem raad, help = information
    # about the game

    if x == "1":
        print("You will be required to guess. Try and figure out what secret code is!")
        n = 0
        while n < 11:
            random_guess = functions.random_guess()
            assessment = functions.beoordelingsfunctie(x=secret_code, y=random_guess)
            black_pin = assessment[0]
            white_pin = assessment[1]
            if black_pin != 4:
                n += 1
            elif black_pin == 4:
                print("Congratulations! you have won the game.")
                break
            print("Black =", black_pin, 'White =', white_pin)
        break

    elif x == "2":
        alg_pref = input("The system will be guessing. Please choose your preferred algorithm (1, 2 or 3): ")
        if alg_pref == "1":
            print("You have chosen to go with the first (simple strategy) algorithm.")
            n = functions.simple_algorithm()

            break
        elif alg_pref == "2":
            print("You have chosen to go with the second (worst case strategy) algorithm.")
            n = functions.worst_case_algorithm()
            break

        elif alg_pref == "3":
            print("You have chosen to go with the third unique (strategy) algorithm")
            n = functions.unique_algorithm()
            break

    elif x == "help":
        print("Game mode number 1: Player will have to guess the secret code made by the system.")
        print("Game mode number 2: System will have to guess the secret code generated by the player.")
        continue

    else:
        print("Thank you for playing and goodbye!")
        break
