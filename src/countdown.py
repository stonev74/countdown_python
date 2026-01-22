# Support running both as a package (tests) and as a standalone script.
try:  # when executed from project root or another module
    from .letter_functions import *
    from .number_functions import *
except ImportError:  # when executed directly inside src/
    from letter_functions import *
    from number_functions import *

def game_menu():
    print("Welcome to Countdown!")
    while True:
        print("What would you like to do?")
        print("1. Play a game")
        print("2. Check Leaderboard")
        print("3. Exit")
        choice = input("Choose option:  ")
        match choice:
            case "1":
                choose_game()
            case '2':
                pass
            case '3':
                return
            case _:
                print("Invalid input. Please choose again.")
                continue

def choose_game():
    while True:
        print("What game would you like to play?")
        print("1. Letters")
        print("2. Numbers")
        print("3. Exit")
        choice = input("Choose your option: ")
        match choice:
            case "1":
                letters_game()
            case "2":
                numbers_game()
            case "3":
                return
            case _:
                print('Invalid input. Please choose again.')
                continue

def main():
    game_menu()

if __name__ == "__main__":
    main()
