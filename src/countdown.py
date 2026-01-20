# Support running both as a package (tests) and as a standalone script.
try:  # when executed from project root or another module

    from .letter_functions import *
except ImportError:  # when executed directly inside src/

    from letter_functions import *

def choose_game():
    while True:
        user_choice = input("What game would you like to play? Letters or numbers? (Enter exit to end program.)")
        if user_choice.lower() not in ['letters', 'numbers', 'exit']:
            print('Invalid input. Please choose letters or numbers.')
            continue
        elif user_choice.lower() == 'letters':
            letters_game()
        elif user_choice.lower() == 'numbers':
            pass
        elif user_choice.lower() == 'exit':
            False
        else:
            print('Error.')

def main():
    choose_game()

if __name__ == "__main__":
    main()
