import random

top_of_range = input("Type a number: ")

if top_of_range .isdigit():
    top_of_range =int(top_of_range)

    if top_of_range <=0:
        print("please enter a number greater than 0")
        quit()
        
else:
    print("please enter a number next time")
    quit()

random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("make a lucky or calculative guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("You got it right!")
            print("want to play again? (yes/no)")
            play_again = input().lower()
            if play_again == "yes":
                print("Restarting the game...")
                top_of_range = input("Type a number: ")
                if top_of_range.isdigit():
                    top_of_range = int(top_of_range)
                    random_number = random.randint(0, top_of_range)
                else:
                    print("Please enter a valid number next time.")
                    quit()
            else:
                print("Thanks for playing!")
                break
        elif user_guess < random_number:
            print("You were below the number")
        elif user_guess > random_number:
            print("You were above the number")
    else:
        print("Please enter a valid number next time")
        continue
    if user_guess == "":
        quit()

    
