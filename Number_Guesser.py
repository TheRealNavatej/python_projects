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
guesses = 0

while True:
    user_guess = input("make a lucky or calculative guess:")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number again")
        continue

    if user_guess == random_number:
        print("you got it!!!")
        print("you have made", guesses, "guesses so far")
        break
    else:
        if user_guess < random_number:
            print("u below bro")
        else:
            print("u above boi")
