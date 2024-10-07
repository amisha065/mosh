import random


def play(choice, computer_number, lo,hi):
    active = True

    try:
        choice = int(choice)
        if choice > computer_number and choice <= hi:
            print("Too high!")
        elif choice < computer_number and choice >= lo:
            print("Too low!")
        elif choice == computer_number:
            print("Congratulations, you guessed it!")
            active = False
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please enter a valid number")

    return active


if __name__ == "__main__":

    lo = 1
    hi = 100
    computer_number = random.randint(lo,hi)
    print(f"{computer_number}")

    active=True
    while(active):
        choice = input(f"Guess the number between {lo} and {hi}: ")
        active=play(choice, computer_number, lo, hi)