from itertools import permutations
from spellchecker import SpellChecker
from countdown_timer import countdown
import random
import requests
spell = SpellChecker()

try:  # when executed from project root or another module
    from .countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels
except ImportError:  # when executed directly inside src/
    from countdown_letters import countdown_tiles_consonants as consonants, countdown_tiles_vowels as vowels

spell = SpellChecker()

trial_set = list('shogunate')

def find_longest_word(letter_set):
    #gets permutations of letters and finds longest valid word
    #checks for longest words first then works down to 1
    for length in range(len(letter_set), 0, -1):  
        print(f"Finding {length} letter words...")
        #creates permutations of current length
        combs = [''.join(comb) for comb in permutations(letter_set, length)]
        #checks if they are valid words
        valid_combs = []
        for word in combs:
            if word in spell:
                valid_combs.append(word)
        #returns valid words if found
        if valid_combs:
            print(f"{len(valid_combs)} valid {length} letter word(s).")
            return valid_combs
    print("No valid words found.")


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

def valid_word(letters, word):
    for letter in word.lower():
        if letter in letters:
            letters.remove(letter)
        else:
            return False
    if word in spell:
        return True

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
        find_longest_word(letters)

