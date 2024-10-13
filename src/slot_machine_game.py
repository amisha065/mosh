
import random, emoji
from collections import Counter


def get_starting_balance():
    while True:
        money = input('Enter your starting balance: $')
        try:
            money = int(money)
            if money > 0:
                return money
            print('Please enter a positive number')    
        except ValueError:
            print('Please enter a valid number.')

def get_bet_amount(balance):
    while True:
        bet = input('Enter your bet amount: $')
        try:
            bet = int(bet)
            if bet > 0 and bet <= balance:
                return bet
            print(f'Invalid bet amount. You can bet between $1 and ${balance}')    
        except ValueError:
            print('Please enter a valid number for the bet amount.')

def display_wheel(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')



# This function randomly picks 3 out of 10 choices and prints them. returns reward.
def spin_wheel(symbols, bet):

    # List of emojis
    emoji_list = [
        emoji.emojize(':cherries:'),
        emoji.emojize(':strawberry:'),
        emoji.emojize(':watermelon:'),
        emoji.emojize(':sun_with_face:'),
        emoji.emojize(':star:'),
        emoji.emojize(':tangerine:'),
        emoji.emojize(':mango:'),
        emoji.emojize(':crescent_moon:')
    ]

    # Pick random emojis from the list. random.choices allows duplicates!!
    return random.choices(emoji_list, k=symbols)

def payout_factor(reels):
  if reels[0] == reels[1] == reels[2]:
    return 10
  if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
    return 2
  return 0

def play_game():

    balance = get_starting_balance()
    balance = 100

    print('\nWelcome to the Slot machine game!')
    print(f'You start with a balance of ${balance}')

    while balance > 0:
        print(f'Current balance: ${balance}')
        bet = get_bet_amount(balance)

        reels = spin_wheel(3, bet)
        display_wheel(reels)
        
        payout = bet*payout_factor(reels)
        if payout > 0:
            print(f'You won ${payout}!')
        else:
            print('You lost!')
        
        balance += payout - bet 

        if balance <= 0:
            print('You are out of money! Game over.')
            break
        
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print(f'You walk away with ${balance}.')
            break
        
def main():
    play_game()

if __name__ == "__main__":
    main()