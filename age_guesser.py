import random

def guesser():
    print("Hello! I'm going to try to guess your age!\n")
    name = input("What is your name?\n")
    guess = False
    while guess == False:
        age = random.randint(15,40)
        user = input(f"Are you {age} years old? (y/n)\n")
        if user == "n":
            print("\nRats!\n")
        else:
            print(f"\n{name} is {age} years old")
            guess = True
    
guesser()