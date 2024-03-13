
"""""

Eels and Escalators from Spongebob

Rules: Roll a dice to move on board eels take you down, 
escalators go up the positions of the eels and escalators are determined by the initial dictionary

3/20/2023
Justin Myshrall

"""""
import random

# define the board layout using a dictionary to indicate the eels and escalators
board = {
    2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94,
    16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80
}

# define the number of players and their starting positions
num_players = 2
# `num_players` can be assigned as any number > 1
positions = [1] * num_players


# define how die works
def roll_die():
    return random.randint(1, 6)


# define the main game loop
while True:
    # loop over the players and get their moves
    for i in range(num_players):
        print(f"Player {i + 1}'s turn")
        # `{i+1}` is determined by assigned `num_players`
        input("Press enter to roll the die...")
        roll = roll_die()
        print(f"You rolled a {roll}")
        positions[i] += roll
        # checks current position, then adds dice roll to that value

        # check if the player landed on escalators or eels by looping through dictionary
        if positions[i] in board:
            # constantly checks position indexed by loop variable
            new_position = board[positions[i]]
            if new_position > positions[i]:
                print("You climbed an escalator")
            else:
                print("You slid down an eel")
            positions[i] = new_position

        # check if the player won
        if positions[i] == 100:
            print(f"Player {i + 1} wins!")
            exit()
            # game ends

        # check if the player went past 100
        if positions[i] > 100:
            print("Oops, you went past 100, you lose your turn")
            positions[i] -= roll
            # undoes last dice roll by player

        print(f"You are now on square {positions[i]}")
        print()
        # constantly telling players current position
