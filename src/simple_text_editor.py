'''
1 Problem statement:
------------------------
1.1 Ask user to open/create a text file. Check validity. In file doesn't exist, create one.
    -  I'll have to learn how to open and work with a file
1.2 Ask user to some texts. to save and exit. USer must enter SAVE in a new line
    - I guess I will have to do some basic pattern matching and perform operatiosn based on that.

2 Optional enhancement
-----------------------
2.1 Add append functionality
2.2 Enable search and replace functionality

3. Plan
--------------------------
3.1 To tackle 1.1 lets ask ChatGPT how to open/create a file - DONE. now i know how to open a file and write into it
3.2 To tackle 1.2,
    - we will get user to type the content inside a loop. we will keep appending each line as an entry in a list.. we will check if at any point he enters SAVE. When it does, then we terminate the loop
    - now we use the write() functionality and write to the file line by line. here also we will do it inside of a loop
'''

import os

def get_filename_and_print_content():
 
    file_name = input('Enter the filename to open or create: ')

    # If file exists, then print content 
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            content = file.read()    
    print(content)

    return file_name


# This function is responsible to get the data from the user. When user enters SAVE, then it means user is done entering the data
def get_user_content():
    # return ['line 1', 'line 2', 'line 3']                                                # This is a stub. Remove after testing
    user_content = list()
    print("Enter your text(type SAVE on a line new to save and exit):")
    while True:
        data = input()
        if data == 'SAVE':
            return user_content
        user_content.append(data)
    return user_content

# This function will open the file and write to it line by line
def write_to_file(file_name, user_content):

    with open(file_name,'w') as file:
        for line in user_content:
            file.write(line + '\n')
          

def texteditor_app():

    # Get the name of the file from user to open and print content. 
    file_name = get_filename_and_print_content()
        
    # Get the content from the user that they want to write to the file
    user_content = get_user_content()

    # Write the user content to the file
    write_to_file(file_name, user_content)    
    

if __name__ == "__main__":
    texteditor_app()


