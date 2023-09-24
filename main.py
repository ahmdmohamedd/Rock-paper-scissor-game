import random

print("\nWelcome to Rock paper scissors game 1.0 \n \tDev. by Ahmed Kamal\n")

stop = False
while not stop:
    rounds = input("Enter the number of rounds: ")
    i = 1
    comp_score = 0
    user_score = 0
    while i <= int(rounds):
        print("\nRound ", i)
        a = False
        while not a:

            response = input("Select your choice (R,P,S): ")
            if response == 'R' or response == 'r':
                user_choice = 1
                a = True
            elif response == 'P' or response == 'p':
                user_choice = 2
                a = True
            elif response == 'S' or response == 's':
                user_choice = 3
                a = True
            else:
                print("\nInvalid choice, please choose a valid choice")

        comp_choice = random.randint(1, 3)
        if comp_choice == 1 and user_choice == 2:
            print("User: Paper\nComputer: Rock")
            user_score = user_score + 1
            i = i + 1
        elif comp_choice == 1 and user_choice == 3:
            print("User: Scissors\nComputer: Rock")
            comp_score = comp_score + 1
            i = i + 1
        elif comp_choice == 2 and user_choice == 1:
            print("User: Rock\nComputer: Paper")
            comp_score = comp_score + 1
            i = i + 1
        elif comp_choice == 2 and user_choice == 3:
            print("User: Scissors\nComputer: Paper")
            user_score = user_score + 1
            i = i + 1
        elif comp_choice == 3 and user_choice == 1:
            print("User: Rock\nComputer: Scissors")
            user_score = user_score + 1
            i = i + 1
        elif comp_choice == 3 and user_choice == 2:
            print("User: Paper\nComputer: Scissors")
            comp_score = comp_score + 1
            i = i + 1
        else:
            print("Draw")

        print("Computer:", comp_score, "\tUser:", user_score)

    if comp_score > user_score:
        print("\n************Computer WINS************")
    elif user_score > comp_score:
        print("\n************User WINS************\n")
    else:
        print("\n************DRAW************\n")

    choice = input("Would you like to go for another game? (Y/N): ")
    if choice == 'Y' or choice == 'y':
        stop = False
        print("\n")
    else:
        stop = True
        print("\n\t\t\t\tThank you!")
