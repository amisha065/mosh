'''
1. Read words in a text file, line by line, and save it to a list.
2. Pick a word at random from this list.
3. Once we have the word, now the user had 6 attempts to guess the word. 
4. At the start, the user sees _ _ _ 

'''
import random

def get_words_from_file():

    content = list()

    with open('words.txt', 'r') as file:
        content = file.read().splitlines()
    return content

def pick_secret_word(words): 
    return random.choice(words)

def get_user_attempt(guesses): # I am guessing mosh might have a cleaner way to do this. we'll check..
    while True:
        attempt = input('Enter a letter: ').strip().lower()
        if len(attempt) != 1:
            print('Enter only one letter.')
            continue
        if not (attempt >= 'a' and attempt <= 'z'):
            print('Enter only letters from a to z.')
            continue
        if attempt in guesses:
            print('You already guessed this letter')
            continue
        return attempt



def play_game():
   
    words = get_words_from_file()
    secret_word = pick_secret_word(words)

    print(secret_word)

    guesses = set()
    user_guess = ['_' for i in range(len(secret_word))]
   
    attempt = 6
    while attempt > 0:
      
        letter = get_user_attempt(guesses)
        guesses.add(letter)

        if letter not in secret_word:
            attempt -= 1
            print('Wrong guess')
        else:
            print('Good guess')

        user_guess = [letter if letter == l else user_guess[i] for i, l in enumerate(secret_word)]

        # Print guess
        print(''.join(user_guess))

        if (''.join(user_guess) == secret_word):
            print('You guessed the secret word!')
            return
    
    print('Better luck next time')








if __name__ == "__main__":
  play_game()
