# By: Sam Belin
# Random Password Generator
import random,string,sys


def password(size, tf_uppercase, tf_lowercase, tf_numbers_list, tf_special_chars, tf_website_break, includeDups):
    check = 0
    # lists
    total_list = []
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    numbers_list = list(string.digits)
    # i wanted to separate some of the characters in case the backend database is not coded correctly
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+"]
    website_breakers = ["(", "{", "}", "[", "]", "(", ")", "/", "\\", "'", "`", "~", ",", ";", ":", ".", "<", ">",
                        ")", '"']

    if tf_uppercase:
        total_list.extend(uppercase)
    else:
        check = check + 1
    if tf_lowercase:
        total_list.extend(lowercase)
    else:
        check = check + 1
    if tf_numbers_list:
        total_list.extend(numbers_list)
    else:
        check = check + 1
    if tf_special_chars:
        total_list.extend(special_chars)
    else:
        check = check + 1
    if tf_website_break:
        total_list.extend(website_breakers)
    else:
        check = check + 1

    if check == 5:
        print("you didn't put anything in. please try again")
        exit(0)

    return_string = ""
    if includeDups:
        for i in range(size):
            return ''.join(total_list[random.randint(0, (len(total_list) - 1))])
    else:
        while (len(return_string)) != size:
            p = ""
            return_string = return_string + total_list[random.randint(0, (len(total_list) - 1))]
            for char in return_string:
                if char not in p:
                    p = p + char
            return_string = p

    return return_string


def createpassword():
    passuppercase = False
    passlowercase = False
    passnumbers = False
    passspecial = False
    passwebsite = False
    passinclude = False
    length = 0
    try:
        length = int(input("Password Length: "))
    except ValueError:
        print("Oops! That's not a valid number.")
        createpassword()

    tf_uppercase = input("include Uppercase letters [Y/N]")
    if tf_uppercase == "Y" or tf_uppercase == "y":
        passuppercase = True
    tf_lowercase = input("include Lowercase letters [Y/N]")
    if tf_lowercase == "Y" or tf_lowercase == "y":
        passlowercase = True
    tf_numbers_list = input("include Numbers [Y/N]")
    if tf_numbers_list == "Y" or tf_numbers_list == "y":
        passnumbers = True
    tf_special_chars = input("include Special Characters letters ! @ # $ % [Y/N]")
    if tf_special_chars == "Y" or tf_special_chars == "y":
        passspecial = True
    tf_website_break = input("include Website Breakers letters ( { } [ ] [Y/N]")
    if tf_website_break == "Y" or tf_website_break == "y":
        passwebsite = True
    includeDups = input("include Duplicate letters [Y/N]")
    if includeDups == "Y" or includeDups == "y":
        passinclude = True

    print(password(length, passuppercase, passlowercase, passnumbers, passspecial, passwebsite, passinclude))

    sys.exit(0)

createpassword()
