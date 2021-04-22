# tazko hacknutelne (bezpecne)

import secrets
import string
import json
import tkinter
import webbrowser
from os import path

DATA_FILENAME = 'data.json'

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

    if unknown == '':
        unknown = string.ascii_lowercase + string.digits

    password = ''    
    for i in range(length):
        password += secrets.choice(unknown)

    return password


root = tkinter.Tk()
root.title('Best password manager')
root.minsize(200, 150)

# Creating Listbox
records = tkinter.Listbox(root)

def copyToCliboard(entry):
    def result():
        root.clipboard_clear()
        root.clipboard_append(entry.get())

    return result

def goToUrl(entry):
    def result():
        webbrowser.open(entry.get())

    return result

def add(event):
    top = tkinter.Toplevel(root)
    top.title('Add')
    top.transient(root)
    top.grab_set()

    l1 = tkinter.Label(top, text = 'Web:')
    l1.grid(column=0, row=0, pady=5, padx=5, sticky=tkinter.E)

    webText = tkinter.Entry(top)
    webText.grid(column=1, row=0, pady=5, padx=5)

    l2 = tkinter.Label(top, text = 'Username:')
    l2.grid(column=0, row=1, pady=5, padx=5, sticky=tkinter.E)

    usernameText = tkinter.Entry(top)
    usernameText.grid(column=1, row=1, pady=5, padx=5)

    l3 = tkinter.Label(top, text = 'Password:')
    l3.grid(column=0, row=2, pady=5, padx=5, sticky=tkinter.E)

    passwordText = tkinter.Entry(top)
    passwordText.grid(column=1, row=2, pady=5, padx=5)

    def ok():
        password = passwordText.get()
        if password == '':
            password = generate_password(16)

        PASSWORD.append({
            'web': webText.get(),
            'username': usernameText.get(),
            'password': password
        })

        records.insert(tkinter.END, PASSWORD[len(PASSWORD) - 1]['web'])

        top.destroy()

    def cancel():
        top.destroy()

    okButton = tkinter.Button(top, text='OK', command=ok)
    okButton.grid(column=0, row=3, pady=5)

    cancelButton = tkinter.Button(top, text='Cancel', command=cancel)
    cancelButton.grid(column=1, row=3, pady=5)
   
    x = root.winfo_x() + root.winfo_width() // 2 - top.winfo_reqwidth() // 2
    y = root.winfo_y() + root.winfo_height() // 2 - top.winfo_reqheight() // 2
    top.geometry(f'+{x}+{y}')

    webText.focus_set()


def view(event):
    try:
        i = event.widget.curselection()[0]
    except:
        return

    webText.delete(0, tkinter.END)
    webText.insert(0, PASSWORD[i]['web'])

    usernameText.delete(0, tkinter.END)
    usernameText.insert(0, PASSWORD[i]['username'])

    passwordText.delete(0, tkinter.END)
    passwordText.insert(0, PASSWORD[i]['password'])

def delete(event):
    try:
        i = records.curselection()[0]
    except:
        return

    del PASSWORD[i]
    records.delete(i)

# Inserting passwords
for i in PASSWORD:
    records.insert(tkinter.END, i['web'])
   
records.bind('<<ListboxSelect>>', view)
records.grid(column=0, row=0, rowspan=3, columnspan=3)

l1 = tkinter.Label(text = 'Web:')
l1.grid(column=4, row=0, padx=5, sticky=tkinter.E)

webText = tkinter.Entry()
webText.grid(column=5, row=0)

webButton = tkinter.Button(text='Open', command=goToUrl(webText))
webButton.grid(column=6, row=0, padx=5)

l2 = tkinter.Label(text = 'Username:')
l2.grid(column=4, row=1, padx=5, sticky=tkinter.E)

usernameText = tkinter.Entry()
usernameText.grid(column=5, row=1)

usernameButton = tkinter.Button(text='Copy', command=copyToCliboard(usernameText))
usernameButton.grid(column=6, row=1, padx=5)

l3 = tkinter.Label(text = 'Password:')
l3.grid(column=4, row=2, padx=5, sticky=tkinter.E)

passwordText = tkinter.Entry()
passwordText.grid(column=5, row=2)

passwordButton = tkinter.Button(text='Copy', command=copyToCliboard(passwordText))
passwordButton.grid(column=6, row=2, padx=5)

addButton = tkinter.Button(text = 'Add')
addButton.bind('<Button>', add)
addButton.grid(column=0, row=4)

removeButton = tkinter.Button(text = 'Remove')
removeButton.bind('<Button>', delete)
removeButton.grid(column=1, row=4)

root.mainloop()

with open(DATA_FILENAME, 'w') as outfile:
    json.dump(PASSWORD, outfile)
