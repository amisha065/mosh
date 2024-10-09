tasks = list()

def display_main_menu():
    print('\nTodo list Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_user_input(limit):
    while True:
        user_input = input("Enter your choice: ").strip()
        try:
            user_input = int(user_input)
            if (user_input <0 or user_input > limit):
                raise ValueError()
            return user_input
        except ValueError:
            print('Invalid input! Retry')

def display_tasks():    
    if len(tasks) == 0:
        print("No tasks added yet!")
    
    for index,task in enumerate(tasks):
        print(f'{index+1}. {task}')

def add_task():
    new_task = input("Enter task: ").strip()
    tasks.append(new_task)

def remove_task():
    index = get_user_input(len(tasks)) - 1
    tasks.pop(index)



def todo_app():

    while True:
        display_main_menu()

        user_choice = get_user_input(4)

        if user_choice == 1: 
            display_tasks()
        elif user_choice == 2: 
            add_task()
        elif user_choice == 3: 
            remove_task()
        else:
            return

if __name__ == "__main__":
    todo_app()

