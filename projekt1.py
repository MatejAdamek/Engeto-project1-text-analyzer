"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Matěj Adámek
email: matej.311@seznam.cz
discord: Addy#8986
"""
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

def user_input():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


def text_control(text):
    words = text.split()
    words = [word.strip('.,!?"\'') for word in words]

    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_count = sum(1 for word in words if word.isnumeric())
    sum_of_numbers = sum(int(word) for word in words if word.isnumeric())

    word_lengths = {}

    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    return word_count, titlecase_count, uppercase_count, lowercase_count, numeric_count, sum_of_numbers, word_lengths


def graph_with_stars(graph):
    print("-"*40)
    print("LEN|  OCCURENCES  |NR.")
    print("-"*40)
    for length, count in sorted(graph.items()):
        print(f"{length:3}|{'*' * count:14}|{count}")

def check_right_user(username, password):
    if username in users and users[username] == password:
        return True
    else:
        print("unregistered user, terminating the program.")
        return False

def final_code():
    username, password = user_input()
    if not check_right_user(username, password):
        exit()

    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("-"*40)
    print("Enter a number btw. 1 and 3 to select:", end=' ')


    while True:
        try:
            choice = int(input())
            if choice < 1 or choice > 3:
                print("Invalid choice. Program terminating.")
                return

            word_count, titlecase_count, uppercase_count, lowercase_count, numeric_count, sum_of_numbers, word_lengths = text_control(
                TEXTS[choice - 1])

            print("-"*40)
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numeric_count} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")


            graph_with_stars(word_lengths)
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    final_code()