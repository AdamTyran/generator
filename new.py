import random, sys, requests
import re, json, math

import soup
from bs4 import BeautifulSoup
from collections import Counter
from bokeh.plotting import figure, show, output_file
import datetime


def zadanie1():
    input = ['ala', 'ma', 'kota', 'a', 'kot', 'ma', 'ale', 'a ', 'ala', 'kota', 'miala']
    # input2 = {'pies', 'kot', 'kot', 'koń', 'chomik', 'koń', 'krowa'}
    # input(„What is your name”)
    word_count = 0
    idiota = {
    }

    for i in input:
        if idiota.get(i) is None:
            idiota.update({i: 1})
        else:
            idiota[i] += 1

    print(idiota)


def zadanie2(tuple1, tuple2):
    wynik = []

    for i in tuple2:
        for j in tuple1:
            if j == i:
                wynik.append(j)
    return tuple(wynik) == tuple1


def zadanie3():
    lista = [1, 2, 0, 0, 5, 0, 1]

    for i in range(len(lista)):
        if lista[i] == 0:
            lista.append(0)
            lista.remove(0)
    return lista


def zadanie4():
    dic = {
        "car": "red", "python": "To gówno", 'Jebać': 'Pythona'
    }
    new_dic = {}
    x = list(dic.keys())
    y = list(dic.values())

    # new_dic = dict(zip(y, x))

    new_dic = {y[i]: x[i] for i in range(len(dic))}
    print(new_dic)


def zadanie5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    return list(filter(lambda x: x < 5, a))


def zadanie6():
    player1 = int(input("Player 1: Kamień, papier, nożyce: "))
    player2 = int(input("Player 2: Kamień, papier, nożyce: "))
    # kamien 0 papier 1 nozyce 2
    winners = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

    if winners[player1][player2] == 1:
        print("Player 1 wygrywa")
    elif winners[player1][player2] == 0:
        print("remis")
    else:
        print("Player 2 wygrywa")


def zadanie7():
    a = [random.randint(1, 20) for _ in range(random.randint(30, 60))]
    b = [random.randint(1, 20) for _ in range(random.randint(30, 60))]

    print(a)
    print(b)

    c = []

    for i in a:
        if i in b and i not in c:
            c.append(i)
    c.sort()
    return c


def zadanie8():
    word = str(input("Sprawdź, czy słowo jest palindromem: "))
    palindrome = word[::-1]

    if word == palindrome:
        return True
    else:
        return False


def zadanie9():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [i for i in a if i % 2 == 0]

    return b


def zadanie10():
    number = random.randint(1, 10)

    while True:
        guessed_number = int(input("Wprowadź liczbę od 1 do 9: "))

        if number == guessed_number:
            print("Gratulacje, zgadłeś")
            break
        elif number < guessed_number:
            print("Za duża liczba")
        else:
            print("Za mała liczba")
        retry = input("Przegrałeś, czy chcesz spróbować ponownie? (y/n): ")
        if retry == "y":
            continue
        else:
            sys.exit(0)


def zadanie11():
    number = int(input("Wpisz numer i sprawdź, czy liczba jest liczbą pierwszą: "))

    lista = list(range(1, number))
    divisors_list = []

    for i in lista:
        if number % i == 0:
            divisors_list.append(i)
    if len(divisors_list) == 1:
        print("Liczba jest liczbą pierwszą")
    else:
        print("Liczba nie jest liczbą pierwszą")


def zadanie12():
    a = [5, 10, 15, 20, 25]

    return [a[0], a[-1]]


def zadanie13(fibonacci):
    bonifacy = []

    if fibonacci == 1:
        bonifacy.append(1)
    elif fibonacci == 2:
        bonifacy.append(1)
        bonifacy.append(1)
    else:
        bonifacy = [1, 1]
        for i in range(1, fibonacci - 1):
            bonifacy.append(bonifacy[i] + bonifacy[i - 1])

    return bonifacy


def zadanie14():
    a = [1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 45, 43, 45]
    b = []

    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])

    return b


def zadanie15():
    a = "My name is Michele My"
    b = a.split()

    return " ".join(b[::-1])


def zadanie16():
    # To nie działa
    base_url = 'http://www.nytimes.com'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)

    with open("text.txt", 'w') as f:
        for story_heading in soup.find_all(class_="story-heading"):
            if story_heading.a:
                f.write(story_heading.a.text.replace("\n", " ").strip())
            else:
                f.write(story_heading.contents[0].strip())


def zadanie17():
    random_number = str(random.randint(1000, 9999))
    result = {"cows": 0, "bulls": 0}
    print(random_number)
    no_of_tries = 5

    while no_of_tries > 0:
        number = input("Wpisz zgadywaną liczbę: ")
        if number == random_number:
            print("Gratulacje, zgadłeś")
            break
        else:
            for i in range(len(random_number)):
                if number[i] == random_number[i]:
                    result["cows"] += 1
                elif number[i] in random_number:
                    result["bulls"] += 1
            no_of_tries -= 1
        print(result)
        print("Pozostało ci", no_of_tries, "prób")
        result = {"cows": 0, "bulls": 0}


def zadanie18():
    lista = [random.randint(1, 100) for _ in range(30, 60)]
    lista.sort()
    print(lista)
    player_input = int(input("Sprawdź, czy liczba znajduje się w zbiorze: "))

    if player_input in lista:
        return True
    else:
        return False


def zadanie19():
    result = {}
    with open('text.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in result:
                result[line] += 1
            else:
                result[line] = 1
            line = f.readline()
    print(result)


def zadanie20():
    def file_reading(plik):
        result = []
        with open(plik, 'r') as f:
            line = f.readline()
            while line:
                result.append(int(line))
                line = f.readline()
        return result

    list_a = file_reading('primes.txt')
    list_b = file_reading('happy.txt')
    overlap = [i for i in list_a if i in list_b]
    print(overlap)


def zadanie21():
    def print_w_bok():
        print(" --- " * board_size)

    def print_w_gore():
        print("|    " * (board_size + 1))

    board_size = int(input(" Jak duża ma być plansza do gry: "))

    for i in range(board_size):
        print_w_bok()
        print_w_gore()
    print_w_bok()

def zadanie22():
    minimum = 0
    maximum = 100
    middle = 50
    tries = 1
    print("Spróbuję zgadnąć twój numer")
    print("Czy twoja liczba to", str(middle) + "?")
    answer = int(input())
    while answer != 1:
        tries += 1
        if answer == 0:
            minimum = middle + 1
        elif answer == 2:
            maximum = middle - 1
        middle = round((minimum + maximum) / 2)
        answer = int(input("Czy twoja liczba to " + str(middle) + "?"))
    print("Zgadłem!, zajęło mi to", str(tries), "prób")

def zadanie23():
    board = [['tu', 'nic', 'nie ma'], ['', ' ', ' ', ' '], ['', ' ', ' ', ' '], ['', ' ', ' ', ' ']]

    def drawboard(board):
        print('  |   |   ')
        print('' + board[3][1] + ' | ' + board[3][2] + ' | ' + board[3][3])
        print('  |   |   ')
        print('-----------')
        print('  |   |   ')
        print('' + board[2][1] + ' | ' + board[2][2] + ' | ' + board[2][3])
        print('  |   |   ')
        print('-----------')
        print('  |   |   ')
        print('' + board[1][1] + ' | ' + board[1][2] + ' | ' + board[1][3])
        print('  |   |   ')


    def game(player):
        print("Gracz " + player)
        condition = True

        while condition:
            try:
                player_input1 = int(input("Wprowadź pierwszy koordynat (1, 3) :"))
                player_input2 = int(input("Wprowadź drugi koordynat (1, 3) :"))
            except ValueError:
                print("Niepoprawny format danych")
                continue
            if board[player_input1][player_input2] == ' ' and player == '1':
                board[player_input1][player_input2] = 'x'
                condition = False
            elif board[player_input1][player_input2] == ' ' and player == '2':
                board[player_input1][player_input2] = 'o'
                condition = False
            else:
                print("Nieprawidłowe dane")
                continue
        drawboard(board)

    def win_in_line(board):
        for i in range(1, 3):
            if board[i][1] == board[i][2] == board[i][3] == 'x':
                print("Player 1 wygrywa")
                print("Wygrana w rzędzie")
                return True
            elif board[i][1] == board[i][2] == board[i][3] == 'o':
                print("Player 2 wygrywa")
                print("Wygrana w rzędzie")
                return True
        return False

    def win_in_row(board):
        for i in range(1, 3):
            if board[1][i] == board[2][i] == board[3][i] == 'x':
                print("Player 1 wygrywa")
                print("Wygrana w pionie")
                return True
            elif board[1][i] == board[2][i] == board[3][i] == 'o':
                print("Player 2 wygrywa")
                print("Wygrana w pionie")
                return True
        return False

    def win_in_diagonal(board):
        if board[1][1] == board[2][2] == board[3][3] or board[1][3] == board[2][2] == board[3][1]:
            # środkowa kratka decyduje
            if board[2][2] == 'x':
                print("Player 1 wygrywa")
                print("Wygrana po przekątnej")
                return True
            elif board[2][2] == 'o':
                print("Player 2 wygrywa")
                print("Wygrana po przekątnej")
                return True
        return False

    def check_if_full(board):
        elements_in_list = 0
        for i in board:
            if " " in i:
                elements_in_list += 1
        if elements_in_list == 0:
            print("Tablica pełna, koniec gry")
            return True
        else:
            return False


    def check_win_condition(board):
        if win_in_line(board) or win_in_diagonal(board) or win_in_row(board) or check_if_full(board):
            return True
        else:
            return False

    while True:
        game("1")
        if check_win_condition(board):
            break
        game("2")
        if check_win_condition(board):
            break

def zadanie24():
    liczby = []
    max_number = 0
    for _ in range(3):
        x = int(input("Wpisz liczbę: "))
        liczby.append(x)

    if liczby[0] > liczby[1]:
        max_number = liczby[0]
    else:
        max_number = liczby[1]
    if max_number < liczby[2]:
        max_number = liczby[2]

    print("największa liczba wynosi", max_number)

def zadanie25():
    words = []

    with open("words.txt", "r") as f:
        line = f.readline().strip()
        words.append(line)
        while line:
            line = f.readline().strip()
            words.append(line)

    random_word = random.randint(0, len(words))
    print("Losowe słowo: ", words[random_word])

def zadanie26():
    word = "adele"
    user_word = []
    used_letters = []
    letter = ""
    game_continue = True

    def word_input():
        player_input = ""
        pattern = r"[a-z]$"
        incorrect_word = True

        while incorrect_word:
            player_input = input("Wprowadź małą literę: ")
            if not re.match(pattern, player_input):
                print("Niepoprawny format danych, wprowadź małą literę")
            if not validate_letters(player_input, used_letters):
                print("Litera została już użyta")
            else:
                incorrect_word = False

        return player_input

    def check_letters(word, player_input):
        indexes = []

        for index, value in enumerate(word):
            if player_input == value:
                indexes.append(index)
        return indexes

    def validate_letters(letter, list):
        validate = True
        if letter in list:
            validate = False
        return validate


    for _ in range(len(word)):
        user_word.append("_")

    while game_continue:
        letter = word_input()
        used_letters.append(letter)
        found_indexes = check_letters(word, letter)

        if len(found_indexes) == 0:
            print("Nie ma takiej litery")
        else:
            for i in found_indexes:
                user_word[i] = letter

        print(user_word)
        print(used_letters)

        if "".join(user_word) == word:
            print("gratulacje, wygrałeś")
            game_continue = False

def zadanie27():
    print("Welcome to hangman!!")
    word = "EVAPORATE"
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("guess letter: ")
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            print(''.join(guessed))
#            if letter is not '':
 #               lstGuessed.append(letter.upper())
            letter = input("guess letter: ")

        #if '_' not in guessed:
        #   print("You won!!")
        #    break

def zadanie28():
    birthday = {
        "Albert Einstein": "11.01.1939",
        "Isaac Newton": "20.05.1839",
        "Young Igi": "30.06.1998"
    }

    user_input = str(input("Kogo urodziny mamy podać? "))
    print(birthday[user_input])

def zadanie29():
    birthday = {}
    name = ""

    with open("birthday.json", "r") as f:
        birthday = json.load(f)

    def add_entry():
        name = input("Czyje urodziny mamy dodać? ").title()
        date = input("Kiedy ma urodziny? ")
        birthday[name] = date
        with open("birthday.json", "w") as f:
            json.dump(birthday, f)
        print("Dodano do listy")

    def find_date():
        name = input("Czyje urodziny chcesz wyszukać? ").title()
        try:
            if birthday[name]:
                print("{} urodził się {}".format(name, birthday[name]))
        except KeyError:
            print("Nie ma takiej osoby na liście")

    def list_entries():
        print("Obecnie zapisane są następujące osoby: ")
        for key in birthday:
            print(key.ljust(31), ":", birthday[key])
            print()

    while True:
        task = input("Co chcesz zrobić? Możesz dodać, znaleźć, wypisać: ")
        if task == "q":
            sys.exit(0)
        elif task == "d":
            add_entry()
        elif task == "z":
            find_date()
        elif task == "w":
            list_entries()


def zadanie30():
    with open("birthday.json", "r") as f:
        birthday = json.load(f)

    num_to_string = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    months = {}
    for name, string in birthday.items():
        month = num_to_string[int(string.split(".")[1])]
        if string in months:
            months[month] += 1
        else:
            months[month] = 1

    print(months)

def zadanie31():
    data_file = "birthdays.json"
    output_file("plot.html")

    with open(data_file, "r") as f:
        data = json.load(f)

    num_to_string = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    months = []
    months = []
    for name, birthday_string in data.items():
        month = int(birthday_string.split("/")[0])
        months.append(num_to_string[month])
    months = Counter(months)

    months, counts = list(zip(*months.items()))

    categories = list(num_to_string.values())
    p = figure(x_range=categories, title="Scientists' Birthday Months")
    p.xaxis.major_label_orientation = math.pi / 4
    p.vbar(x=months, top=counts)
    show(p)

def zadanie32():
    age = int(input("Ile masz lat? "))

    print(f"Do setki zostało Ci {100-age} lat")

def zadanie33():
    teraz = datetime.datetime.now()

    name = input("Jak masz na imię? ")
    age = int(input("Ile masz lat? "))

    print(f"{name} będzie miał 100 lat w {teraz.year + (100 - age)}")


if __name__ == '__main__':
    #   korotka1 = (3, 4, 5)
    #    korotka2 = (1, 2, 3, 5, 6, 7, 8, 9)

    #    print(zadanie2(korotka1, korotka2))
    # fibonacci = int(input("Wpisz ile chcesz otrzymać liczb bonifacego: "))
    #test_function()
    zadanie33()
