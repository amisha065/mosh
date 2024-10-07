import random
from enum import Enum
import emoji

class ChoicesEnum(Enum):
    ROCK = 'r'
    PAPER = 'p'
    SCISSOR = 's'

    @classmethod
    def from_value(cls, value):
        """Reverse lookup to get enum member from its value."""
        for choice in cls:
            if choice.value == value:
                return choice
        return None  # Return None if no match is found


emojis = {ChoicesEnum.ROCK : emoji.emojize(':rock:'), ChoicesEnum.PAPER : emoji.emojize(':page_facing_up:'), ChoicesEnum.SCISSOR : emoji.emojize(':scissors:')}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = ChoicesEnum.from_value((input("Rock/paper/scissor? (r/p/s): ")))
        if user_choice in choices:
            return user_choice  # Return the enum memberr
        print("Invalid choice")



def print_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')



def print_winner(user_choice, computer_choice):
    if ((user_choice == ChoicesEnum.PAPER and computer_choice == ChoicesEnum.ROCK) or 
        (user_choice == ChoicesEnum.ROCK and computer_choice == ChoicesEnum.SCISSOR) or
        (user_choice == ChoicesEnum.SCISSOR and computer_choice == ChoicesEnum.PAPER)):
        print('You win!')
    elif ((user_choice == ChoicesEnum.PAPER and computer_choice == ChoicesEnum.SCISSOR) or 
        (user_choice == ChoicesEnum.ROCK and computer_choice == ChoicesEnum.PAPER) or
        (user_choice == ChoicesEnum.SCISSOR and computer_choice == ChoicesEnum.ROCK)):
        print('You lose!')
    else:
        print("Draw!")


def play_game():
    while True:         
        # Get choices
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        # Print choices 
        print_choices(user_choice, computer_choice)
        
        # Compute and print winner
        print_winner(user_choice, computer_choice)

        c = input("Continue? (y/n): ").lower()
        if c == 'n':
            break

if __name__ == "__main__":
    play_game()