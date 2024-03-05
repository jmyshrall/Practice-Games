"""
Collaborator: Justin Myshrall
Date: 2/29/2024
Title: Random Number Guesser
"""
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # tracks letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()        # what user has guessed 
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # takes `used_letters` and seperates each as a string seperate by comma and space
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter').upper()    # a != A
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives =  lives - 1
                print('Letter is not in the word')
        
        elif user_letter in used_letters:
            print('You already used that letter, try again')
        
        else:
            print('Invalid character')
    if lives  == 0:
        print('You lost the answer was', word)
    else:
        print('You guessed the word', word, '!')

hangman()
