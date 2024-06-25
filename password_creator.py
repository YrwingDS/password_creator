import string
 
def password_creator():
    tries = 3
    print("Hello, welcome to the password creator!")
    print("Note that your password needs to have 9 characters, with atleast one number, special character, one lowercase letter and one uppercase letter.")
    while tries > 0:    
        print("Please type your password:")
        password = input()
        pass_list = list(password)
        if len(pass_list) < 9:
            print("Password is not long enough (9 characters minimum)")
            tries -= 1
            if tries > 0:
                print("You have " + str(tries) + " tries left")
        else:
            lc_true = False
            uc_true = False
            dig_true = False
            punc_true = False
            lc_true = lowercase_check(pass_list)
            uc_true = uppercase_check(pass_list)
            dig_true = digit_check(pass_list)
            punc_true = punctuation_check(pass_list)
            if lc_true == True and uc_true == True and dig_true ==True and punc_true ==True:
                print("Password created!")
                break
            else:
                print("Please check the requirements needed")
                tries -= 1
                if tries > 0:
                    print("You have " + str(tries) + " tries left")
            


def lowercase_check(pass_list):
        lowercase = list(string.ascii_lowercase)
        has_lowercase = False
        for item in pass_list:
                for char in lowercase:
                    temporary = char
                    if item == temporary and has_lowercase == False:
                        has_lowercase = True
                        return True
                        break
        if has_lowercase == False or has_lowercase == None:
            print("Your password needs a lowercase letter")
def uppercase_check(pass_list):
    uppercase = list(string.ascii_uppercase)
    has_uppercase = False
    for item in pass_list:
            for char in uppercase:
                temporary = char
                if item == temporary and has_uppercase == False:
                    has_uppercase = True
                    return True
                    break
    if has_uppercase == False or has_uppercase == None:
        print("Your password needs a uppercase letter")
def digit_check(pass_list):
    digit = list(string.digits)
    has_digits = False
    for item in pass_list:
            for char in digit:
                temporary = char
                if item == temporary and has_digits == False:
                    has_digits = True
                    return True
                    break
    if has_digits == False or has_digits == None:
        print("Your password needs a digit")
def punctuation_check(pass_list):
    especial = list(string.punctuation)
    has_punctuation = False
    for item in pass_list:
            for char in especial:
                temporary = char
                if item == temporary and has_punctuation == False:
                    has_punctuation = True
                    return True
                    break
    if has_punctuation == False or has_punctuation == None:
        print("Your password needs a punctuation character")
        
password_creator()