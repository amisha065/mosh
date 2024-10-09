import numpy as np
from termcolor import colored

# Constants
SIZE = 3

# This function inputs row/col from user 
# - bound checks
# - invalid input checks
def enter(label):
    while True:
        point = input(f'Enter {label} (0-{SIZE-1}): ').strip()
        try:
            point = int(point)
            if (point >=0 and point <= SIZE-1):            
                return point
            else:
                raise ValueError()
        except ValueError:
            print('Invalid input! Retry')

# This functions gets player to choose a spot on the grid
def player_turn(grid, icon):
    print(f'Player {icon}\'s turn')
   
    while True:
        # Input row/col from user
        row = enter('row')
        col = enter('col')
   
        # Check spot is free or not
        if grid[row][col] == ' ':
            grid[row][col] = icon
            return True
        print('This spot is already taken! Retry')





# the purpose of this function is to check if someone win
# A big limitation of this is the dimensions are hard coded
# I need a better way so we can play for bigger boards..
def game_status(grid, icon):

    # Check rows
    for row in grid:
        if row[0] == row[1] == row[2] == icon:
            return True
    
    # Check columns
    for col in range(SIZE):
        if (grid[0][col] == grid[1][col] == grid[2][col] == icon):
            return True
    
    # Check diagnol
    if (grid[0][0] == grid[1][1] == grid[2][2] == icon) or (grid[2][0] == grid[1][1] == grid[0][2] == icon):
        return True
    
    return False

def cell(mark):
    
    color = "red" if mark == 'X' else "green"
    return colored(mark,color)

# This function prints the board

# I need a better way so we can play for bigger boards..
def print_board(grid):
    line = '---+---+---'

    print(f'{line}')
    for row in grid:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ')              
        print(f'{line}')



def play_game():
    grid = np.full((SIZE, SIZE), ' ')

    move_counter = 0
    player_icons = ('X','O')

    print_board(grid)

    for move_counter in range(SIZE*SIZE):

        icon = player_icons[move_counter%2]


        
        player_turn(grid, icon)

        print_board(grid)


        status = game_status(grid, icon)
        if status:
            print(f'{icon} won!')
            return icon
    
    # If we get here, then it means no move legal moves are remaining as the board is full
    print('Board is full. It\'s a draw!')
    return 'Draw'

    
def tic_tac_toe_app():

    o_win_counter = x_win_counter = draw_counter = 0

    result = play_game()

    if result == 'O':
        o_win_counter +=1
    elif  result == 'X':
        x_win_counter +=1
    else:
        draw_counter += 1

if __name__ == "__main__":
  tic_tac_toe_app()
