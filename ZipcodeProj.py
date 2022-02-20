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

def getCheckDigitValue(sum):
    return (10 - (sum % 10))

def getSumNumbers(zip):
    for i in zip:
        total_value = 0
        ascii_value = ord(i)
        actual_num = ascii_value - 48
        total_value += actual_num
    return total_value

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

more_codes = ' '

while more_codes != 'n':
    sentinel_value = True
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

    whole_zip = getWholeZip(user_zip)

    print(f"Code: {whole_zip}")

    more_codes = ' '

    while (more_codes != 'y' and more_codes != 'n'):
        more_codes = input("More codes (y/n)? ")
        if (more_codes != 'y' and more_codes != 'n'):
            print("Error: Invalid selection")


print("Goodbye!")


    
