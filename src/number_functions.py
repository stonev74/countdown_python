from countdown_numbers import big_numbers, small_numbers
import random
from countdown import countdown
import re
from itertools import permutations, combinations_with_replacement, combinations

trial_set = [100, 25, 6, 3, 2, 5]

def generate_numbers():
    while True:
        try:
            user_choice = int(input("You must pick 6 numbers. You can have up a max of 4 big numbers, and a max of 6 small numbers. How many big numbers would you like?\n"))
            if user_choice not in range(0,5):
                print("You can choose between 0 and 4 big numbers.")
                continue
            yes_no = input(f"You have chosen {user_choice} big numbers and {6-user_choice} small numbers. Is this correct? Enter yes or no.\n")
            if yes_no.lower() == 'yes':
                break
        except ValueError:
            print("Must enter a valid amount.")
    generated_numbers = random.sample(big_numbers, user_choice) + random.sample(small_numbers, (6-user_choice))
    print("Your numbers are:", *generated_numbers)
    return generated_numbers

trial_set = random.sample(big_numbers, 2) + random.sample(small_numbers, 4)
target_num = random.randint(100, 999)

def validate_calculation(final_num=500, numbers=trial_set):
    #evulates the input calculation, checks numbers are in generated set, and checks if declared num matches the calculation
    allowed_chars = set('0123456789+-*/() ')
    while True:
        user_method = input("Enter your full calculation for your final number.\n")
        if not all(char in allowed_chars for char in user_method):
            print("Invalid characters, please use only numbers, operators and brackets.")
            continue
        else:
            break
    cleaned_method = user_method.replace(" ", "")
    used_numbers = [int(x) for x in re.split(r'[+-/*=()]+', cleaned_method) if x.isdigit()]
    #print(used_numbers)
    available_numbers = numbers.copy()
    for num in used_numbers:
        if num in available_numbers:
            available_numbers.remove(num)
        else:
            print(f"Error: {num} is not in allowed numbers or has already been used.")
            return 0
    try:
        calculation = eval(cleaned_method)
        if calculation != final_num:
            print(f"You declared {final_num} but {calculation} was calculated. Zero points.")
            return False
        elif calculation == final_num:
            print("Calculation verified.")
            return True
    except:
        print('Invalid syntax.')
    #print(cleaned_method)

def award_points(target, final_num):
    points = 0
    if target == final_num:
        print("You managed to get the target number! 10 points!")
        points = 10
        return points
    elif 5 >= (target - final_num) >= -5:
        print(f"You were {abs(target-final_num)} away. 7 points!")
    elif 10 >= (target - final_num) >= -10:
            print(f"You were {abs(target-final_num)} away. 5 points!")

def find_valid_calculation(number_set, target):
    #find if there is a valid way to calculate the target number using the given numbers
    print(f"Find valid calculation for {target} with {number_set}...")
    operators = ["+","-","*","/"]
    #starts with smallest amount of numbers and works up to using 6 numbers to solve calculation
    for r in range(1, len(number_set) + 1):
        print(f"Calculating with  formulas with {r} numbers...")
        for number_combo in combinations(number_set, r):
            for values in permutations(number_combo):
                for operCombo in combinations_with_replacement(operators, r-1):
                    for oper in permutations(operCombo):
                        formula = "".join(o+str(v) for o, v in zip([""]+list(oper), values))
                        try:
                            if eval(formula) == target:
                                print(formula, '=', target)
                                return formula
                        except (ZeroDivisionError, ValueError):
                            pass
    print("No valid calculation found.")
    return None

def numbers_game():
    #run numbers game and associated functions
    numbers = generate_numbers()
    target_num = random.randint(100, 999)
    print(f"Your target is {target_num}. You have 30 seconds.")
    countdown()
    user_final_num = int(input("What is your final number?"))
    if validate_calculation(target_num, user_final_num, numbers):
        award_points()
    find_valid_calculation(numbers, target_num)



