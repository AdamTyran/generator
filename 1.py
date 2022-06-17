import sys, random, string, re

def check_is_digit(str):
    if str.strip().isdigit():
        return True
    else:
        return False

def get_password_length(min, max):
    password_length = 0
    exit = False
    while not exit:
        password_length = input("Podaj długość hasła (" + str(min) + "-" + str(max) + " znaków): ")
        if check_is_digit(password_length):
            if min <= int(password_length) <= max:
                exit = True
            else:
                print("Niepoprawna długość")
    return int(password_length)

def get_lowercase_letters(pwd_length):
    lowercase_letters = 0
    exit = False
    while not exit:
        lowercase_letters = input("Ile małych liter ma mieć hasło (0-"+str(pwd_length)+"): ")
        if check_is_digit(lowercase_letters):
            lowercase_letters = int(lowercase_letters)
            if lowercase_letters < 0:
                print("Liczba znaków powinna być dodatnia")
            elif lowercase_letters > pwd_length:
                print("Liczba znaków spoza zakresu 0, " + str(pwd_length))
            else:
                exit = True
    return lowercase_letters


def get_uppercase_letters(char_left):
    uppercase_letters = 0
    exit = False
    while not exit:
        uppercase_letters = input("Ile dużych liter ma mieć hasło (0-"+str(char_left)+"): ")
        if check_is_digit(uppercase_letters):
            uppercase_letters = int(uppercase_letters)
            if uppercase_letters < 0:
                print("Liczba znaków powinna być dodatnia")
            elif uppercase_letters > char_left:
                print("Liczba znaków spoza zakresu 0, " + str(char_left))
            else:
                exit = True
    return uppercase_letters

def get_special_characters(char_left):
    special_characters = 0
    exit = False
    while not exit:
        special_characters = input("Ile znaków specjalnych ma mieć hasło (0-"+str(char_left)+"): ")
        if check_is_digit(special_characters):
            special_characters = int(special_characters)
            if special_characters < 0:
                print("Liczba znaków powinna być dodatnia")
            elif special_characters > char_left:
                print("Liczba znaków spoza zakresu 0, " + str(char_left))
            else:
                exit = True
    return special_characters

def get_digits(char_left):
    digits = 0
    exit = False
    while exit == False:
        digits = input("Ile znaków specjalnych ma mieć hasło (0-"+str(char_left)+"): ")
        if check_is_digit(digits):
            digits = int(digits)
            if digits < 0:
                print("Liczba znaków powinna być dodatnia")
            elif digits > char_left:
                print("Liczba znaków spoza zakresu 0, " + str(char_left))
            else:
                exit = True
    return digits


def generate_password():
    password_length = get_password_length(min=8, max=32)
    lowercase_letters = get_lowercase_letters(password_length)
    char_left = password_length - lowercase_letters

    uppercase_letters = get_uppercase_letters(char_left)
    char_left -= uppercase_letters

    special_characters = get_special_characters(char_left)
    char_left -= special_characters

    digits = get_digits(char_left)
    char_left -= digits

    if char_left > 0:
        print("Nie wszystkie znaki zostały wykorzystane, hasło zostanie uzupełnione małymi literami")
        lowercase_letters += char_left

    print("Długość hasła:", password_length)
    print("Duże litery:", uppercase_letters)
    print("Małe litery:", lowercase_letters)
    print("Znaki specjalne:", special_characters)
    print("Cyfry:", digits)

    password = ""
    for i in range(password_length):
        if lowercase_letters > 0:
            password += (random.choice(string.ascii_lowercase))
            lowercase_letters -= 1
        if uppercase_letters > 0:
            password += (random.choice(string.ascii_uppercase))
            uppercase_letters -= 1
        if special_characters > 0:
            password += (random.choice(string.punctuation))
            special_characters -= 1
        if digits > 0:
            password += (random.choice(string.digits))
            digits -= 1

    random.shuffle(list(password))
    return '' + password

if __name__ == '__main__':
    password = generate_password()
    print(password)
