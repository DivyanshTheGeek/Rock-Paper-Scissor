import random
import sys


def computerChoice():
    return random.randint(1, 3)


def check_who_has_won():
    computer_choice = computerChoice()
    if (computer_choice == 1):
        print("Computer chose Rock\n")
    if (computer_choice == 2):
        print("Computer chose Paper\n")
    if (computer_choice == 3):
        print("Computer chose Scissor\n")
    if (player_choice == computer_choice):
        print("Game draw")
    if (player_choice == 1 and computer_choice == 2):
        print("Computer Wins!!!")
    if (player_choice == 1 and computer_choice == 3):
        print(player_name+" Wins!!!")
    if (player_choice == 2 and computer_choice == 1):
        print(player_name+" Wins!!!")
    if (player_choice == 2 and computer_choice == 3):
        print("Computer Wins!!!")
    if (player_choice == 3 and computer_choice == 1):
        print("Computer Wins!!!")
    if (player_choice == 3 and computer_choice == 2):
        print(player_name+" Wins!!!")


player_name = input(
    "\nWelcome to Rock, Paper, Scissor game :\n\nEnter your name:\n")
print("~~~" + player_name+" vs Computer~~~\n")
while True:
    i = 0
    while i < 3:
        print("\n--Round "+str(i+1)+"--\n")
        player_choice = int(input(
            "Choose 1 for Rock, 2 for Paper, 3 for Scissor.\nChoose 0[Zero] to exit the game!\n"))
        if player_choice not in (0, 1, 2, 3):
            print("Invalid Choice!!\nPlease try again.")
            i = 0
            continue
        elif (player_choice == 0):
            sys.exit()
        else:
            i += 1
            check_who_has_won()