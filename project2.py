#Author: Zach Naymik
#Assignment: Project 2 Part 2
#Course and Prof.: ET2100-Section 107, Dusan Sormaz

def get_num_of_non_WS_characters(c): #defines getting number of whitespace function
    num_whitespace = c.count(' ')
    len_string = len(c)
    string_no_whitespace = len_string - num_whitespace
    return string_no_whitespace  #returns number of whitespace characters

def get_num_of_words(w):   #defines getting number of words function
    list_words = []     #list to store words
    list_words = w.split(' ')
    len_words = len(list_words)
    for i in list_words:          #iterates through words and removes characters that are not words
            if i == '':
                list_words.remove(i)
    for i in list_words:
            if i == '':
                list_words.remove(i)
    num_words = len(list_words)
    return num_words  #returns number of words

def fix_capitalization(f):  #function to define fixing capitalization
    count = 0
    beginning = True
    result = ''  #creates new string for edited text to be stored
    for i in f:  #iterates through the entire string
        if beginning and i.isalpha():
            if i.islower():
                i = i.upper()
                count += 1
                result += i
                beginning = False
        elif i in '?.!':         #defines where characters need to be capitalized
            beginning = True
            result += i
        else:
            result += i
    print('Number of letters capitalized: {}'.format(count))
    print('Edited text: {}'.format(result))
    return result, count   #returns number of letters capitalized and edited text

def replace_punctuation(r, exclamation_count = 0, semicolon_count = 0): #defines replacing punctuation function
    user_string = r
    new_str = '' #creates new string for edited string to be stored
    for i in user_string:  #iterates through characters in string
        if i == '!':
            i = '.'
            exclamation_count += 1   #adds to count of exclamation marks
        elif i == ';':
            i = ','
            semicolon_count += 1    #adds to count of semicolons
        new_str += i
    print('Punctuation Replaced')
    print('exclamation_count: {}'.format(exclamation_count))
    print('semicolon_count: {}'.format(semicolon_count))
    print('Edited text: {}'.format(new_str))
    return new_str  #returns edited string

def shorten_space(s):  #defines function to shorten elongated spaces
    list_words = []   #creates list for split words
    new_str = '' #creates new list for edited text to be stored
    list_words = s.split(' ')
    for i in list_words:  #iterates through list and removes space characters
        if i == '':
            list_words.remove(i)
    for i in list_words:
            if i == '':
                list_words.remove(i)
    for i in list_words:
            if i == '':
                list_words.remove(i)
    for i in list_words:
            if i == '':
                list_words.remove(i)
    for i in list_words:
            if i == '':
                list_words.remove(i)
    new_str = ' '.join(list_words)
    print('Edited text: {}'.format(new_str))
    return new_str #returns edited text

def open_and_read(file_name): #defines a function to open, read and edit a file
    with open(file_name, 'r') as o:  #opens file and will automatically close due to with statement
        lines = o.readlines()
        print(lines)   #prints lines in file
        while True:   #creates a loop in which the user can edit the text in their file until they wish to quit
            print('\nMENU')
            print('f - Fix capitalization')
            print('r - Replace punctuation')
            print('s - Shorten spaces')
            print('q - Quit\n')
            user_option = input('Choose an option:\n')
            if user_option == 'q':   #depending on user option, runs function to edit text in file
                break
            elif user_option == 'f':
                for i in lines:
                    fix_capitalization(i)
            elif user_option == 'r':
                for i in lines:
                    replace_punctuation(i)
            elif user_option == 's':
                new_str = ' '.join(lines)
                shorten_space(new_str)
            else:
                print('Please enter valid option')

def save_file(text, file_name):    #defines function for user to save the edited text to a new file
    file_split = file_name.split('.')
    new_file = file_split[0] + '-new.' + file_split[1]
    file_open = open(new_file, 'w')
    file_open.write(text)
    file_open.close()
    return new_file               #returns new file

            

def print_menu(string): #defines menu for user to edit their input text
    while True:  #allows user to edit text as many times as they want until they wish to quit
        print('\nMENU')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('f - Fix capitalization')
        print('r - Replace punctuation')
        print('s - Shorten spaces')
        print('o - open and read text from file')
        print('S - save final modified text into new file')
        print('q - Quit\n')
        user_option = input('Choose an option:\n')
        if user_option == 'q':  #breaks the loop if user wishes to quit
            break
        elif user_option == 'c':  #runs function corresponding to which option user selects
            print('\nNumber of non-whitespace characters: {}'.format(get_num_of_non_WS_characters(user_text)))
        elif user_option == 'w':
            print('\nNumber of words: {}'.format(get_num_of_words(user_text)))
        elif user_option == 'f':
            fix_capitalization(user_text)
        elif user_option == 'r':
            replace_punctuation(user_text)
        elif user_option == 's':
            shorten_space(user_text)
        elif user_option == 'o':
            file_name = input('Please enter file name: ')
            print(open_and_read(file_name))
        elif user_option == 'S':
            text = input('Please enter text to save:')
            file_name = input('Please enter file name: ')
            save_file(text, file_name)
        else:
            print('Please enter valid option.')
            
if __name__ == '__main__':   #makes sure that the print menu loop runs only if called in this file

    user_text = input('Enter a sample text:\n')  #prompts for user text input
    print('\nYou entered: {}'.format(user_text))
    print_menu(user_text)  #runs the print menu function to prompt the user for editing choices
