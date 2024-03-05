"""
Collaborator: Justin Myshrall
Date: 2/29/2024
Title: Rock Paper Scissor Game 25 ways
RPS 25 rules were written by: https://www.umop.com/rps25.htm
RULES:
GUN: ROCK SUN FIRE SCISSORS AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF
DRAGON: DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS AXE SNAKE MONKEY
MOON: AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN
TREE: COCKROACH WOLF SPONGE PAPER MOON AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING
AXE: SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER MOON AIR BOWL
DYNAMITE: GUN ROCK SUN FIRE SCISSORS AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH
ALIEN: DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS AXE SNAKE
PAPER: MOON AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK
MAN: TREE COCKROACH WOLF SPONGE PAPER MOON AIR BOWL WATER ALIEN DRAGON DEVIL
SCISSORS: AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER MOON AIR
NUKE: DYNAMITE GUN ROCK SUN FIRE SCISSORS SNAKE AXE MONKEY WOMAN MAN TREE
WATER: ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS AXE
SPONGE: PAPER MOON AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN
WOMAN: MAN TREE COCKROACH WOLF SPONGE PAPER MOON AIR BOWL WATER ALIEN DRAGON
LIGHTNING: NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS AXE SNAKE MONKEY WOMAN MAN
BOWL: WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS
WOLF: SPONGE PAPER MOON AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE
MONKEY: WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER MOON AIR BOWL WATER ALIEN
SUN: FIRE SCISSORS AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER
DEVIL: LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE SCISSORS AXE SNAKE MONKEY WOMAN
AIR: BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE DYNAMITE GUN ROCK SUN FIRE
COCKROACH: WOLF SPONGE PAPER MOON AIR BOWL WATER ALIEN DRAGON DEVIL LIGHTNING NUKE
SNAKE: MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER MOON AIR BOWL WATER
ROCK: SUN FIRE SCISSORS AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE
FIRE: SCISSORS AXE SNAKE MONKEY WOMAN MAN TREE COCKROACH WOLF SPONGE PAPER MOON
"""
import random

def rps25():
 
    choices = ['gun', 'dynamite', 'nuke', 'lightning', 'devil', 'dragon', 'alien', 'water', 'bowl', 'air',\
               'moon', 'paper', 'sponge', 'wolf', 'cockroach','tree', 'man', 'woman', 'monkey', 'snake',\
                 'axe', 'scissors', 'fire', 'sun', 'rock' ]

    # define the winning conditions
    winning_conditions = {
        'rock': ['sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge'],
        'sun': ['fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper'],
        'fire': ['scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon'],
        'scissors': ['axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air'],
        'axe': ['snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl'],
        'snake': ['monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water'],
        'monkey': ['woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien'],
        'woman': ['man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon'],
        'man': ['tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil'],
        'tree': ['cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning'],
        'cockroach': ['wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke'],
        'wolf': ['sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite'],
        'sponge': ['paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun'],
        'paper': ['moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock'],
        'moon': ['air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun'],
        'air': ['bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire'],
        'bowl': ['water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors'],
        'water': ['alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe'],
        'alien': ['dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake'],
        'dragon': ['devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey'],
        'devil': ['dynamite', 'nuke', 'lightning', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman'],
        'lightning': ['nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man'],
        'nuke': ['dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'snake', 'axe', 'monkey', 'woman', 'man', 'tree'],
        'dynamite': ['gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach'],
        'gun': ['rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf']
    }
    prompt = """
    Choose from the following options:
    gun, dynamite, nuke, lightning, devil, dragon, alien, water, bowl, air,
    moon, paper, sponge, wolf, cockroach,
    tree, man, woman, monkey, snake, axe, scissors, fire, sun, rock
    """
    # ask the user to choose
    user_choice = input(prompt).lower()

    # all inputs are lower-cased `.lower()`

    # check if the user input is valid
    if user_choice not in choices:
        print("Invalid choice. Please choose again.")
        # makes error case
    else:
        # use random to choose the computer's choice
        computer_choice = random.choice(choices)

        # display the choices
        print(f"You chose {user_choice}.")
        # `f` makes f-string instead of concatenating the `print()` statement
        print(f"The computer chose {computer_choice}.")

        # check the result
        if user_choice == computer_choice:
            print("It's a tie")
        elif computer_choice in winning_conditions[user_choice]:
            # if `computer_choice` is in `winning_conditions` indexed by `user_choice` then you will win
            print("You win")
        else:
            print("You lose.")

def main():

    rps25()

main()