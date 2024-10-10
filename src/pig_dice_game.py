'''
Problem statement
======================
1. 2 players roll the dice one after the other. Keep asking the player after every move if they want to continue rolling. Also, keep adding the value of the dice. 
2. We move to the other player in one of the 2 cases -> 1) either the player chose not to, 2) they get a 1 and then the total for this attempt is zero.
3. who ever gets to 100 wins.

Plan
======================
1. Lets build a logic to roll the die and get a random response. roll_dice()
2. Now build logic to keep rolling the dice and adding the total for one turn. player_turn()



'''

import random

def roll_dice():
    return random.randint(1,6)


def player_turn(label):

    current_score = 0
    print(f'\nPlayer {label}\'s turn')

    while True:
        dice_value = roll_dice()
        print(f'You rolled a {dice_value}')

        current_score += dice_value
        if dice_value == 1:
            current_score = 0
            break
        play_more = input('Roll again?(y/n): ')
        if play_more == 'n':
            break

    print(f'You scored {current_score} points in this turn')
    return current_score

def print_scores(score_tally):
    print(f'Current scores: Player 1: {score_tally['1']}, Player 2: {score_tally['2']}')
    

def play_pig_dice_game():


    score_tally = {'1' : 0, '2' : 0} # Player : total score

    # Initialize
    player = '2'

    while score_tally[player] < 100:

        if player == '1':
            player = '2'
        else:
            player = '1'

        # Player turn
        score_tally[player] += player_turn(player)

        # Print scores
        print_scores(score_tally)

    print(f'Player {player} wins! ')




if __name__ == "__main__":
    play_pig_dice_game()


