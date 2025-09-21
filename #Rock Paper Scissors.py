#Rock Paper Scissors

import random

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

def bot():
    """
    Using random to generate a number between 0-2 inclusive for printing one of the moves.
    """
    bot_move = random.randint[0,2]

def user():
    """
    Taking Input for Users move
    """
    user_Move = input(int())

start_Game()