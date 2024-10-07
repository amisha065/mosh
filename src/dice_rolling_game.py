import random

def dice_roll(iterations: any) -> None:

    result = ""
    for i in range(iterations):
         result += f"{random.randint(1, 6)} "
    print(f"{result}")

def play(choice: any):
    match choice:
            case 'y':
                iterations = int(input("How many times? "))
                dice_roll(iterations)
                return True
            case 'n':
                print("Thanks for playing!")
                return False
            case _:
                print("Invalid choice!")
                return True

if __name__ == "__main__":

    active=True
    while(active):
        choice = input("Roll the dice? (y/n): ").lower()
        active=play(choice)