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
    elif player_Ready_Status =="n":
            print("Guess not...")
            exit()
    else:
        print("Invalid input. Please try answering in y/n.")
        start_Game()
    instrustions()

def instrustions():
    """
    Explaining Game rules to User
    """
    print("For Rock, input 0")
    print("For Paper, input 1")
    print("For Scissors, input 2")
    print("Rock beats Scissors, Paper beats Rock , Scissors beat paper.\n Rock and Rock, Paper and Paper along with Scissors and Scissors lead to a draw")

def bot():
    """
    Using random to generate a number between 0-2 inclusive for printing one of the moves.
    """
    global bot_Move
    bot_Move = random.randint[0,2]

def user():
    """
    Taking Input for Users move
    """
    global user_Move
    user_Move = input(int())
    while user_Move == (0,1,2):
         pass
    else:
         print("Invalid input. Please choose number from given options.")
         user()

def gameplay():
    """
    Starting the match
    """
    user()
    bot()
    print("Rock")
    time.sleep(0.75)
    print("Paper")
    time.sleep(0.75)
    print("Scissors")
    time.sleep(0.75)
    print("Go!!!")
    print(f"Player move: {moves(user_Move)}")
    print(f"Bot Move:{moves(bot_Move)}")
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
    elif rematch =="n":
            print("Guess not...")
            exit()
    else:
        print("Invalid input. Please try answering in y/n.")

start_Game()