import random

chad_wins = 0
bot_wins = 0

choices = ["rock", "paper", "scissors"]
choices[0]

while True:
    chad_input = input("ENTER YOUR CHOICE (rock, paper, scissors) OR Q TO QUIT").lower()
    if chad_input == "q":
        print("Thanks for playing!")
        print(f"final score - chad: {chad_wins}, bot: {bot_wins}")
        break
    if chad_input not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    random_choice = random.choice(choices)
    #random_choice = random.randint(0, 2) also works but not as readable but as numbers

    print(f"Bot chose: {random_choice}")
    if chad_input == random_choice:
        print("It's a tie!")
    elif (chad_input == "rock" and random_choice == "scissors"):
        print("yo boi WON, thats giga chad energy")
        chad_wins += 1
    elif (chad_input == "paper" and random_choice == "rock"):
        print("yo boi WON, thats ultra chad energy")
        chad_wins += 1
    elif( chad_wins == "scissors" and random_choice == "rock"):
        print("yo boi WON, thats mega chad energy")
        chad_wins += 1
    else:
        print("bot wins this time")
        print("but remember, chad always wins in the end")
        bot_wins =+ 1

print("GG CHAD, you played well!")

