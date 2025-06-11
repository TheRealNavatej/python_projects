print("Welcome to the Quiz Game!")

playing = input("Do you wanna play the game? (yes/No):")

if playing.strip().lower() != "yes":
    quit()
    
while True:
    player = input("Please enter your name: ").strip()
    if player != "":
        break
    print("You must enter a name to play the game.")

print(f"Hello {player}, let,s begin the game!")

score = 0
question = input("what does CPU stand for? (a) Central Processing Unit (b) Central Process Unit (c) Central Processor Unit: ")
if question == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is (a)")

question = input("what does RAM stand for? (a) Read Access Memory (b) Random Access Memory (c) Random Access Module: ")
if question == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is (b)")

question = input("what does GPU stand for? (a) Graphical Processing Unit (b) Graphics Processing Unit (c) Graphical Processor Unit: ")
if question == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is (b)")

question = input("what does SSD stand for? (a) Solid State Drive (b) Solid State Disk (c) Solid State Device: ")
if question == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is (a)")

print ("Now here comes a tough one!")

ask = input("ARE YOY READY!? (yes/no): ")

if ask.strip.lower() != "yes":
    print("Okay, maybe next time!")
    print("Your score is:", score)
    quit()
else:
    print("that's the sprit!, let's continue!")

question = input("what does HDD stand for? (a) Hard Disk Disk (b) Hard Disk Device (c) Hard Disk Drive: ")
if question == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is (c)")
print("Congratulations, you have completed the quiz!")
print(f"Your final score is: {score} out of 5")

