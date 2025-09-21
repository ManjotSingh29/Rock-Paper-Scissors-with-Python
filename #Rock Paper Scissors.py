#Rock Paper Scissors

from tracemalloc import start


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

start_Game()