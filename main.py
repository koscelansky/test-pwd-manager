# tazko hacknutelne (bezpecne)
# lahko kopirovali hesla
# generovat hesla <--

import secrets
import string
import json
from os import path

DATA_FILENAME = 'data.txt'

PASSWORD = [
]


if path.exists(DATA_FILENAME):
    try:
        with open(DATA_FILENAME, 'r') as infile:
            PASSWORD = json.load(infile)
    except:
        PASSWORD = []

def generate_password(length, **kwargs):
    """Vygeneruje nové bezpečné heslo dĺžky ``length``, nastavenia sú

    ``lowercase`` heslo obsahuje malé písmená
    ``uppercase`` heslo obsahuje veľké písmená
    ``digit``
    ``punctuation``

    Example:
    """
    unknown = ''
    for (k, v) in kwargs.items():
        if k == 'lowercase':
            if v:
                unknown += string.ascii_lowercase
        elif k == 'uppercase':
            if v:
                unknown += string.ascii_uppercase
        elif k == 'digit':
            if v:
                unknown += string.digits
        elif k == 'punctuation':
            if v:
                unknown += string.punctuation
        else:
            raise KeyError(k + ' is not valid parameter.')

    password = ''    
    for i in range(length):
        password += secrets.choice(unknown)

    return password


def add():
    web = input('Zadaj web adresu ')
    username = input('Zadaj užívateľské meno ')
    password = input('Zadaj heslo (ak prázdne vygeneruje sa nové) ')

    if password == '':
        password = generate_password(16, lowercase=True, uppercase=True, digit=True)

    PASSWORD.append({
        'web': web,
        'username': username,
        'password': password
    })

def print_menu():
    print('ADD - Zadávanie nového vstupu')
    print('DEL - Mazanie položky')
    print('VIEW - Zobrazenie položky')
    print('EXIT - Ukončenie programu')

print('Best password managed')

while True:
    print_menu()
    cmd = input('Zadaj príkaz ')
    if cmd == 'ADD':
        add()
    elif cmd == 'DEL':
        pass
    elif cmd == 'VIEW':
        pass
    elif cmd == 'EXIT':
        break
    else:
        print('Nesprávny príkaz.')

with open('data.txt', 'w') as outfile:
    json.dump(PASSWORD, outfile)

print(PASSWORD)