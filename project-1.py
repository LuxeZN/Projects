#Author: Zach Naymik - ET2100 - Section 107
#Date: October 4, 2021
#Assignment - Project 1

import math                             #import the math module in order to allow for mathematical functions to take place
operations = []                        #create empty list for the history function and operations to be stored
arguments = []                          #create empty list for the history function and arguments to be stored
while True:
    print('\nEnter number of operation you wish to execute (type exit or quit to end program):\n', '1 sin(x)\n', '2 cos(x)\n', '3 tan(x)\n', '4 asin(x)\n', '5 acos(x)\n', '6 atan(x)\n','7 ln(x)\n', '8 sqrt(x)\n', '9 factorial (x)\n', '10 history')
    user_input = input('Select:')                                               #this block prompts the user to enter their desired operation
    print(f'\nUser input is {user_input}\n')                                    #the operation that is chosen is then printed back to them
    if user_input == 'quit' or user_input == 'exit':                            #allows the user to exit the program by typing either of the strings defined
        print('Goodbye.')                                                       #prints goodbye after the user wishes to quit the program
        break                                                                   #stops the loop from repeating itself as the user wanted to quit the program with the strings inputted
    elif user_input == '1':
        user_argument_input_1 = input('Enter the argument for operation:')      #after the user has selected input 1, they are then prompted to input the argument they want
        user_argument_1 = float(user_argument_input_1)                          #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        sin_result = math.sin(math.radians(user_argument_1))                    #the sin calculation is completed
        print(f'\nsin({user_argument_1}) = {sin_result}')                       #the result of the calculation is printed
        user_input = 'sin'                                                      #the input is changed to sin so when the history lists are called sin is what shows up in the operations column
        operations.append(user_input)                                           #adds the sin function to the operations list
        arguments.append(user_argument_1)                                       #adds the argument entered to the arguments list
    elif user_input == '2':
        user_argument_input_2 = input('Enter the argument for operation:')      #after the user has selected input 2, they are then prompted to input the argument they want
        user_argument_2 = float(user_argument_input_2)                          #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        cos_result = math.cos(math.radians(user_argument_2))                    #the cos calculation is completed
        print(f'\ncos({user_argument_2}) = {cos_result}')                       #the result of the calculation is printed
        user_input = 'cos'                                                      #the input is changed to cos so when the history lists are called cos is what shows up in the operations column
        operations.append(user_input)                                           #adds the cos function to the operations list
        arguments.append(user_argument_2)                                       #adds the argument entered to the arguments list
    elif user_input == '3':
        user_argument_input_3 = input('Enter the argument for operation:')      #after the user has selected input 3, they are then prompted to input the argument they want
        user_argument_3 = float(user_argument_input_3)                          #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        tan_result = math.tan(math.radians(user_argument_3))                    #the tan calculation is completed
        print(f'\ntan({user_argument_3}) = {tan_result}')                       #the result of the calculation is printed
        user_input = 'tan'                                                      #the input is changed to tan so when the history lists are called tan is what shows up in the operations column
        operations.append(user_input)                                           #adds the tan function to the operations list
        arguments.append(user_argument_3)                                       #adds the argument entered to the arguments list
    elif user_input == '4':
        user_argument_input_4 = input('Enter the argument for operation, [-1,1]:')                  #after the user has selected input 4, they are then prompted to input the argument they want within the range specified
        user_argument_4 = float(user_argument_input_4)                                              #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        if -1 <= user_argument_4 <= 1:                                                              #defines the range of values that asin is defined
            asin_result = math.degrees(math.asin((user_argument_4)))                                #continues with the calculation if the input argument is in the specified range
            print(f'\nasin({user_argument_4}) = {asin_result}')                                     #the result of the calculation is printed
        else:                                                                                         
            print(f'\nYou entered {user_argument_4}, please enter a number between [-1,1]')         #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'asin'                                                                         #the input is changed to asin so when the history lists are called asin is what shows up in the operations column
        operations.append(user_input)                                                               #adds the asin function to the operations list
        arguments.append(user_argument_4)                                                           #adds the argument entered to the arguments list
    elif user_input == '5':
        user_argument_input_5 = input('Enter the argument for operation, [-1,1]:')                  #after the user has selected input 5, they are then prompted to input the argument they want within the range specified
        user_argument_5 = float(user_argument_input_5)                                              #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        if -1 <= user_argument_5 <= 1:                                                              #defines the range of values that acos is defined
            acos_result = math.degrees(math.acos((user_argument_5)))                                #continues with the calculation if the input argument is in the specified range
            print(f'\nacos({user_argument_5}) = {acos_result}')                                     #the result of the calculation is printed
        else:
            print(f'\nYou entered {user_argument_5}, please enter a number between [-1,1]')         #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'acos'                                                                         #the input is changed to acos so when the history lists are called acos is what shows up in the operations column
        operations.append(user_input)                                                               #adds the acos function to the operations list
        arguments.append(user_argument_5)                                                           #adds the argument entered to the arguments list
    elif user_input == '6':
        user_argument_input_6 = input('Enter the argument for operation, [-1,1]:')                  #after the user has selected input 6, they are then prompted to input the argument they want within the range specified
        user_argument_6 = float(user_argument_input_6)                                              #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        if -1 <= user_argument_6 <= 1:                                                              #defines the range of values that atan is defined
            atan_result = math.degrees(math.atan((user_argument_6)))                                #continues with the calculation if the input argument is in the specified range
            print(f'\natan({user_argument_6}) = {atan_result}')                                     #the result of the calculation is printed
        else:
            print(f'\nYou entered {user_argument_6}, please enter a number between [-1,1]')         #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'atan'                                                                         #the input is changed to atan so when the history lists are called atan is what shows up in the operations column
        operations.append(user_input)                                                               #adds the atan function to the operations list
        arguments.append(user_argument_6)                                                           #adds the argument entered to the arguments list
    elif user_input == '7':
        user_argument_input_7 = input('Enter the argument for operation, (0,∞]:')                   #after the user has selected input 7, they are then prompted to input the argument they want within the range specified
        user_argument_7 = float(user_argument_input_7)                                              #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        if user_argument_7 > 0:                                                                     #defines the range of values that ln is defined
            ln_result = math.log((user_argument_7))                                                 #continues with the calculation if the input argument is in the specified range
            print(f'\nln({user_argument_7}) = {ln_result}')                                         #the result of the calculation is printed
        else:
            print(f'\nYou entered {user_argument_7}, please enter a non-negative, non-zero number') #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'ln'                                                                           #the input is changed to ln so when the history lists are called ln is what shows up in the operations column
        operations.append(user_input)                                                               #adds the ln function to the operations list
        arguments.append(user_argument_7)                                                           #adds the argument entered to the arguments list
    elif user_input == '8':
        user_argument_input_8 = input('Enter the argument for operation, [0,∞]:')                   #after the user has selected input 8, they are then prompted to input the argument they want within the range specified
        user_argument_8 = float(user_argument_input_8)                                              #the argument input by the user is converted to a float value in order to allow for mathematical operations to be completed and decimals to be entered
        if user_argument_8 >= 0:                                                                    #defines the range of values that square root is defined
            sqrt_result = math.sqrt((user_argument_8))                                              #continues with the calculation if the input argument is in the specified range
            print(f'\nsqrt({user_argument_8}) = {sqrt_result}')                                     #the result of the calculation is printed
        else:
            print(f'\nYou entered {user_argument_8}, please enter a non-negative number')           #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'Square Root'                                                                  #the input is changed to square root so when the history lists are called square root is what shows up in the operations column
        operations.append(user_input)                                                               #adds the square root function to the operations list
        arguments.append(user_argument_8)                                                           #adds the argument entered to the arguments list
    elif user_input == '9':
        user_argument_input_9 = input('Enter the argument for operation, [0,∞]:')                   #after the user has selected input 9, they are then prompted to input the argument they want within the range specified
        user_argument_9 = math.ceil(float(user_argument_input_9))                                   #the argument input by the user is converted to a float and then the ceiling function is used in order to round any decimal to a whole number so the factorial function can take place
        if user_argument_9 > 0:                                                                     #defines the range of values that factorial is defined
            factorial_result = math.factorial(user_argument_9)                                      #continues with the calculation if the input argument is in the specified range
            print(f'\n{user_argument_9}! = {factorial_result}')                                     #the result of the calculation is printed
        else:
            print(f'\nYou entered {user_argument_9}, please enter a non-negative integer')          #if the user enters an argument outside the range defined before, the user is prompted with what they entered and the range they need to enter a value within
        user_input = 'Factorial'                                                                    #the input is changed to factorial so when the history lists are called factorial is what shows up in the operations column
        operations.append(user_input)                                                               #adds the factorial function to the operations list
        arguments.append(user_argument_9)                                                           #adds the argument entered to the arguments list
    elif user_input == '10':
        for i in range(len(operations)):                                                         #calls for the length of the operations list as both the argument list and operations list will be the same length
            print('{} {}'.format(operations[i], arguments[i]))                                   #allows for the corresponding values in each list to be printed in operation, argument pairs
    else:
        print(f"You entered '{user_input}' please input a valid number")                         #if the user enters anything other than what is defined by the program, they are prompted to enter a valid number for selection of an operation
        
  
 
