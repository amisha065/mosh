'''
Notes:
======================================================================
1) We learnt how to manage our database (question bank) using "list of dictionares approach" to in this assignment
2) We saw a how to randomize the questions we ask using random.shuffle() function
3) We saw a simple use of lambda fuction
4) We used cprint to color our text on screen

We can work on the following improvements:
======================================================================
Right now the order of our choices are hardcoded. Ex. 'B. Jupiter'. 
The reason is to simplify comparison of the expected response  with the selected response.
For example: user selects B.. and expected is B.. so the test is super simple..

Ideally, we need the following thing.. 

user selects A --> we should have a mechanism to map A to the displayed choice 'Jupiter' or whatver
And the expected response will also be the string.. 
and then we will compare the selected string to the expected syting

'''


# python3 -m pip install --upgrade termcolor
import sys
import random

from termcolor import cprint

# Helper lambdas to control the print colors
print_red = lambda x: cprint(x, "red")
print_green = lambda x: cprint(x, "green")

# APPROACH 1: List of dictionary approach
question_bank = [
       {'question': 'What is the capital of France?', 'options':['A. Paris','B. London','C. Rome'], 'correct': 'A'},
       {'question': 'What is the largest planet in our solar system?', 'options':['A. Earth', 'B. Jupiter', 'C. Mars'], 'correct': 'B'},
       {'question': 'What is the capital of France (fewer choices?', 'options':['A. Paris','B. London'], 'correct': 'A'},
]

def ask_question_give_options(question_number, question_answer):
    print(f'Question {question_number+1}: {question_answer['question']}')
    for option in question_answer['options']:
            print(f'{option}')



def play_game():

    # This will randomly shuffle the entries of question_bank. So, now when we iterate thru it they will be in random order
    random.shuffle(question_bank)

    score = 0
    for question_number, question_answer in enumerate(question_bank):
        ask_question_give_options(question_number, question_answer)
        
        selected_answer = input('Your answer: ').upper()
        expected_answer = question_answer['correct']

        if selected_answer == expected_answer:
            print_green("Correct!\n")
            score += 1
        else:
            print_red(f'Wrong! The correct answer is {expected_answer}\n')

    print(f'Quiz over! Your final score is {score} out of {len(question_bank)}')


if __name__ == "__main__":
    play_game()