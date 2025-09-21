#Rock Paper Scissors

import random
import time

moves = ("Rock","Paper","Scissors")

def start_Game():
    """
    Game start intro and ask user if they are ready
    """
    print("Ready to play? y/n")
    player_Ready_Status = input(str())

    if player_Ready_Status == "y":
            print("Lets get started.")
            instrustions()
            gameplay()
    elif player_Ready_Status =="n":
            print("Guess not...")
            exit()
    else:
        print("Invalid input. Please try answering in y/n.")
        start_Game()
    

def instrustions():
    """
    Explaining Game rules to User
    """
    print("Rock beats Scissors, Paper beats Rock , Scissors beat paper.\nRock and Rock, Paper and Paper along with Scissors and Scissors lead to a draw")
    return 

def bot():
    """
    Using random to generate a number between 0-2 inclusive for printing one of the moves.
    """
    global bot_Move
    bot_Move = random.randint(0,2)

def user():
    """
    Taking Input for Users move
    """
    global user_Move
    user_Move = int(input("Enter your move 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_Move in (0,1,2):
        print(f"Player move: {moves[user_Move]}")
    else:
        print("Invalid input. Please choose number from given options.")
        user()

def gameplay():
    """
    Starting the match
    """
    print("Enter your move:")
    bot()
    user()
   

    #Buildup


    print("Rock")
    time.sleep(0.75)
    print("Paper")
    time.sleep(0.75)
    print("Scissors")
    time.sleep(0.75)
    print("Go!!!")

    #Match


    print(f"Bot Move: {moves[bot_Move]}")
    if user_Move == 0:
        if bot_Move == 0:
            print("Its a draw.")
        elif bot_Move == 1:
            print("You lose.")
        else:
            print("You win.")
    if user_Move == 1:
        if bot_Move == 0:
            print("You win.")
        elif bot_Move == 1:
            print("Its a draw.")
        else:
            print("You lose.")
    if user_Move == 2:
        if bot_Move == 0:
            print("You lose.")
        elif bot_Move == 1:
            print("You win.")
        else:
            print("Its a draw.")
    print("Wanna go again? y/n")
    rematch = input(str())
    if rematch == "y":
            print("Lets get started.")
            gameplay()
    elif rematch =="n":
            print("Guess not...")
            exit()
    else:
        print("Invalid input. Please try answering in y/n.")

start_Game()