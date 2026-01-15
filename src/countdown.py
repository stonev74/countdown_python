import time
import random
from countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels
def input_user_word(): #user inputs the word they have come up with after countdown is finished
    user_word = input("What is your word?")
    return user_word

def generate_letters():
    letters = []
    vowel_count = 0
    consonant_count = 0
    while True:
        while len(letters) < 9:
            user_choice = input("Vowel (V) or consonant (C)?")
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
def valid_word(word):
    pass

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
        print('Invalid word length!')
    return points

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time's up!")

#countdown(30)
#will need scraper to verify if word is valid
def main():
    print(generate_letters())
    countdown(30)
    print(award_points(input_user_word()))

main()