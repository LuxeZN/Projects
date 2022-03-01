#Author: Zach Naymik
#Date: February 20, 2022
#Description: This program takes a zipcode entered by a user and transforms into a bar code value, 
#             this is what happens in a real post office, and we seek to replicate that here.

#Function that gets the code for an individual digit

def getDigitCode(digit):
    digit_code = ""
    if (digit == '1'):
        digit_code = ":::||"
    elif (digit == '2'):
        digit_code = "::|:|"
    elif (digit == '3'):
        digit_code = "::||:"
    elif (digit == '4'):
        digit_code = ":|::|"
    elif (digit == '5'):
        digit_code = ":||::"
    elif (digit == '6'):
        digit_code = "|:::|"
    elif (digit == '7'):
        digit_code = "|:::|"
    elif (digit == '8'):
        digit_code = "|::|:"
    elif (digit == '9'):
        digit_code = "|:|::"
    elif (digit == '0'):
        digit_code = "||:::"
    return digit_code


#Function that checks to see if the given zipcode is all digits or not

def isDigits(zip):
    counter = 0
    t_or_f = True

    for i in zip:
        if (i.isdigit() == False):
            counter += 1
    if (counter > 0):
        return False
    else:
        return True

#Function that returns the check value for the end of the zipcode barcode

def getCheckDigitValue(sum):
    return (10 - (sum % 10))

#Function that gets the sum of all the numbers in the zip in order to get the check digit

def getSumNumbers(zip):
    for i in zip:
        total_value = 0
        ascii_value = ord(i)
        actual_num = ascii_value - 48
        total_value += actual_num
    return total_value

#Function that gets the barcode for the entire zipcode

def getWholeZip(zip):
    full_code = "|"
    char_list = list(zip)
    for i in char_list:
        digit_code = getDigitCode(i)
        full_code += digit_code + " "
    
    check_digit_int = getCheckDigitValue(getSumNumbers(zip))

    if (check_digit_int == 1):
        check_digit_char = '1'
    elif (check_digit_int == 2):
        check_digit_char = '2'
    elif (check_digit_int == 3):
        check_digit_char = '3'
    elif (check_digit_int == 4):
        check_digit_char = '4'
    elif (check_digit_int == 5):
        check_digit_char = '5'
    elif (check_digit_int == 6):
        check_digit_char = '6'
    elif (check_digit_int == 7):
        check_digit_char = '7'
    elif (check_digit_int == 8):
        check_digit_char = '8'
    elif (check_digit_int == 9):
        check_digit_char = '9'
    elif (check_digit_int == 0):
        check_digit_char = '0' 

    check_digit_code = getDigitCode(check_digit_char)

    full_code += check_digit_code + "|"

    return full_code   


#Initialize the more codes string in order to enter the while loop

more_codes = ' '

#While loop that continues if the user wished to enter more zipcodes

while more_codes != 'n':
    #Initialize sentinel value in order to enter the while loop
    sentinel_value = True
    #While loop used to verify that the input follows our conditions
    while sentinel_value == True:
        user_zip = input("Enter a zip code: ")
        if (len(user_zip) < 5 or len(user_zip) > 5):      
            print("Error: Zip code must be 5 digits")
            sentinel_value = True
        elif (isDigits(user_zip) == False):
            print("Error: Invalid characters in zip code")
            sentinel_value = True
        else:
            sentinel_value = False
    #Calls the getWholeZip function and stores the whole zipcode barcode into the whole_zip variable
    whole_zip = getWholeZip(user_zip)
    #Prints out the zipcode barcode to the user
    print(f"Code: {whole_zip}")
    #Resets the more_codes variable to nothing to allow the while loop to be entered
    more_codes = ' '
    #While loop that asks the user if they wish to enter more zipcodes and verifies they entered a valid choice
    while (more_codes != 'y' and more_codes != 'n'):
        more_codes = input("More codes (y/n)? ")
        if (more_codes != 'y' and more_codes != 'n'):
            print("Error: Invalid selection")

#Prints exit prompt if user decides to not enter any more codes
print("Goodbye!")


    