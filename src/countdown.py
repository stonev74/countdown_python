import time
import random
import requests

# Support running both as a package (tests) and as a standalone script.
try:  # when executed from project root or another module
    from .countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels
    from .countdown_numbers import small_numbers
except ImportError:  # when executed directly inside src/
    from countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels
    from countdown_numbers import small_numbers



def input_user_word(): #user inputs the word they have come up with after countdown is finished
    user_word = input("What is your word?\n ")
    return user_word

def generate_letters():
    letters = []
    vowel_count = 0
    consonant_count = 0
    while True:
        while len(letters) < 9:
            user_choice = input("Vowel (V) or consonant (C)?\n")
            if user_choice.isalpha() == False:
                print("You must input a letter!")
            else:
                if user_choice.lower() == 'v':
                    if vowel_count == 5:
                        print("You must choose at least four consonants!")
                    else:
                        choice = random.choice(vowels)
                        letters.append(choice)
                        vowel_count += 1
                        vowels.remove(choice)
                elif user_choice.lower() == 'c':
                    if consonant_count == 6:
                        print("you must choose at least three vowels!")
                    else:
                        choice = random.choice(consonants)
                        letters.append(choice)
                        consonant_count += 1
                        consonants.remove(choice)
                else:
                    print('Invalid input!')
        return letters

#print(generate_letters())
def valid_word(letters, word):
    for letter in word.upper():
        if letter in letters:
            letters.remove(letter)
        else:
            return False
    response = requests.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}")
    return response.status_code == 200

def award_points(word):
    #awarding points based on word length
    points = 0
    if len(word) < 9:
        points = len(word)
    elif len(word) == 9:
        #9 letter words count for double
        points = 18
    else:
        #word cannot be longer than 10 letters
        return ('Invalid word length!')
    return points

def countdown(t=30):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time's up!")

#countdown(30)
def letters_game():
    #run the letters game and associated functions
    while True:
        letters = generate_letters()
        print(f"Your letters are {letters}")
        countdown(30)
        word = input_user_word()
        if valid_word(letters, word) == True:
            points = award_points(word)
            print(f"Your word is worth {points} points!")
        else:
            print("Word is not valid!")
        user_choice = input("Would you like to play again? Enter yes or no.")
        if user_choice.lower() == 'yes':
            continue
        elif user_choice.lower() == 'no':
            False
        else:
            print('Error.')
    

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
