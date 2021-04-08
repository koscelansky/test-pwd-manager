print('Password manager')

# tazko hacknutelne (bezpecne)
# lahko kopirovali hesla
# generovat hesla <--
# vstup dlzka hesla
# a-zA-Z0-9

import secrets
import string

def generate_password(length, lowercase, uppercase, digit, punctuation):
    # function should generate password with length. 
    # lowercase, uppercase, digit, punctuation are bools, to indicate
    # what characters should be used in generations, for example
    # generate_password(4, False, True, True, False) moze napriklad vygenerovat 
    # heslo AH7R, alebo 8845, ale nie hj4U, lebo su tam aj male prismena, 
    # doprogramujte tuto funkciu... (3body)
    password = ''

    for i in range(pwd_length):
        password += secrets.choice(string.ascii_letters + string.digits)

pwd_length = int(input('Zadaj dĺžku hesla: '))

password = generate_password(pwd_length)

print(password)