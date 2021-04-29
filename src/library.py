from os import path
import string
import json
import secrets
import hashlib
import base64

from cryptography.fernet import Fernet

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

    if unknown == '':
        unknown = string.ascii_lowercase + string.digits

    password = ''    
    for i in range(length):
        password += secrets.choice(unknown)

    return password


def load_passwords(filename, master):
    m = hashlib.sha256()
    m.update(master.encode('utf-8'))

    key = base64.urlsafe_b64encode(m.digest())
    f = Fernet(key)
    if path.exists(filename):
        try:
            with open(filename, 'rb') as infile:
                decrypted = f.decrypt(infile.read()).decode('utf-8')
                return json.loads(decrypted)
        except:
            pass
        
    return []

def save_passwords(filename, passwords, master):
    m = hashlib.sha256()
    m.update(master.encode('utf-8'))
    
    key = base64.urlsafe_b64encode(m.digest())
    f = Fernet(key)
    with open(filename, 'wb') as outfile:
        s = json.dumps(passwords)
        encrypted = f.encrypt(s.encode('utf-8'))
        outfile.write(encrypted)