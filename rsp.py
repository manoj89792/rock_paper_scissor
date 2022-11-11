import random
print("WELCOME TO ROCK PAPER SCISSOR GAME")
print("Here (0) means ROCK (1) means PAPER (2) means SCISSOR")


def rps():
    computer = random.randint(0, 2)
    user = int(input("enter a number from (0,1,2) :"))
    if user == 0 and computer == 2:
        print("user won")
    elif user == 0 and computer == 1:
        print("computer won")
    elif user == 1 and computer == 0:
        print("user won")
    elif user == 1 and computer == 2:
        print("computer won")
    elif user == 2 and computer == 1:
        print("user won")
    else:
        print("computer won")


rps()
