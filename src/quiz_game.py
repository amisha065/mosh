# python3 -m pip install --upgrade termcolor
import sys

from termcolor import cprint

print_red = lambda x: cprint(x, "red")
print_green = lambda x: cprint(x, "green")

counter = 0

print('Question 1: What is the capital of France?')
print('a) Paris')
print('b) London')
print('c) Rome')

user_input = input('Your answer: ').upper()
expected_answer = 'A'

if user_input == expected_answer:
    print_green("Correct!")
    counter += 1
else:
    print_red(f'Wrong! The correct answer is {expected_answer}')

print('Question 2: What is the capital of France?')
print('a) Paris')
print('b) London')
print('c) Rome')

user_input = input('Your answer: ').upper()
expected_answer = 'A'

if user_input == expected_answer:
    print_green("Correct!")
    counter += 1
else:
    print_red(f'Wrong! The correct answer is {expected_answer}')

print(f'Quiz over! Your final score is {counter} out of 2')

