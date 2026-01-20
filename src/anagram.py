from itertools import permutations
from spellchecker import SpellChecker

spell = SpellChecker()

trial_set = list('shogunate')

def find_longest_word(letter_set):
    #gets permutations of letters and finds longest valid word
    #need to add functionality so that it goes from longest to shortest
    print("Finding letter combinations")
    valid_combs = []
    while valid_combs == []:
        combs = [''.join(comb) for comb in permutations(letter_set, len(letter_set))]
        valid_combs = []
        for word in combs:
            if word in spell:
                valid_combs.append(word)
    print("Returning valid words...")
    return valid_combs

print(find_longest_word(trial_set))


