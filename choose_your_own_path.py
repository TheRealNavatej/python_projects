while True:
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
    ).lower()

    if answer == "left":
        answer = input(
            "You come to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: "
        ).lower()

        if answer == "swim":
            print("You swam across and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water, and lost the game.")
        else:
            print("Not a valid option. You lose.")

    elif answer == "right":
        answer = input(
            "You come to a bridge. It looks wobbly. Do you want to cross it or head back (cross/back/do nothing)? "
        ).lower()

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
            if answer == "yes":
                print("You talk to the stranger and they give you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger and they are offended. You lose.")
            else:
                print("Not a valid option. You lose.")
        elif answer == "do nothing":
            answer = input(
                "You stood around for too long. Do you still want to do nothing? (yes/no/eat 5stars): "
            ).lower()
            if answer == "yes":
                print("You stood there until you starved. You lose.")
            elif answer == "no":
                print("You decided to make a move and got lost. You lose.")
            elif answer == "eat 5stars":
                print("You ate 5 stars and gained superpowers. You WIN!")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")

    elif answer == "do nothing":
        answer = input("You stood around for too long. Do you still want to do nothing? (yes/no/eat 5stars): ").lower()
        if answer == "yes":
            print("You stood there until you starved. You lose.")
        elif answer == "no":
            print("You decided to make a move and got lost. You lose.")
        elif answer == "eat 5stars":
            print("You ate 5 stars and gained superpowers. You WIN!")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

    retry = input("Do you want to try again? (yes/no): ").lower()
    if retry != "yes":
        print("Thanks for playing! Goodbye.")
        break
