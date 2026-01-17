import time
import random
from src.countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels
import requests

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
        while True:
            if letter in letters:
                return True
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

def main():
    letters = generate_letters()
    print(f"Your letters are {letters}")
    countdown(30)
    word = input_user_word()
    if valid_word(letters, word) == True:
        points = award_points(word)
        print(f"Your word is worth {points} points!")
    else:
        print("Word is not valid!")

if __name__ == "__main__":
    main()
