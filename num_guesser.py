"""
Collaborator: Justin Myshrall
Date: 2/28/2024
Title: Random Number Guesser
"""
import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0                             # user will never be right by default
    while guess != random_num:
        guess = int(input (f'Guess a number between 1 and {x}: '))    # int() converts user input to type int for comparison operator
        if guess < random_num:
            print('Too low')
        elif guess > random_num:
            print('Too high')

    print(f'You guessed the number {random_num} correctly')


def comp_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low     # could also be high, low = high
        feedback = input(f'Is {guess} too high (H)?, too low (L)?, or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback  == "l":
            low = guess + 1 
    print(f'Computer guessed your number, {guess}, correctly!')

def main():
    max_num = int(input("Enter the maximum number for the guessing game: "))   # user defines x in terminal
    guess(max_num)
    comp_guess(max_num)

main()