"""
Collaborator: Justin Myshrall
Date: 2/29/2024
Title: Rock Paper Scissor Game
"""
import random

def play():
    user = input ("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's']) 

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    # returns True if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def main():

    print(play())

main()