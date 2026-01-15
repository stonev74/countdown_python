countdown_tiles_consonants = []
countdown_tiles_vowels = []

countdown_weighting_consonants = {
    'B': 2,
    'C': 3,
    'D': 6,
    'F': 2,
    'G': 3,
    'H': 2,
    'J': 1,
    'K': 1,
    'L': 5,
    'M': 4,
    'N': 8,
    'P': 4,
    'Q': 1,
    'R': 9,
    'S': 9,
    'T': 9,
    'V': 1,
    'W': 1,
    'X': 1,
    'Y': 1,
    'Z': 1,
}
countdown_weighting_vowels = {
    'A': 15,
    'E': 21,
    'I': 13,
    'O': 13,
    'U': 5
}

for key, value in countdown_weighting_consonants.items():
    countdown_tiles_consonants.extend([key] * value)
for key, value in countdown_weighting_vowels.items():
    countdown_tiles_vowels.extend([key] * value)
