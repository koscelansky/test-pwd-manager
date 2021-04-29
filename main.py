import secrets
import string
import json
import tkinter
import webbrowser
from os import path

from src.library import load_passwords, save_passwords
from src.consts import *
from src.gui import addDialog

def copyToCliboard(root, entry):
    def result():
        root.clipboard_clear()
        root.clipboard_append(entry.get())

    return result

def goToUrl(entry):
    def result():
        webbrowser.open(entry.get())

    return result



def main():
    PASSWORD = load_passwords(DATA_FILENAME, 'heslo')

    root = tkinter.Tk()
    root.title('Best password manager')
    root.minsize(200, 150)

    # Creating Listbox
    records = tkinter.Listbox(root)

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
    records.grid(column=0, row=0, rowspan=3, columnspan=3, padx=5, pady=5)

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

    usernameButton = tkinter.Button(text='Copy', command=copyToCliboard(root, usernameText))
    usernameButton.grid(column=6, row=1, padx=5)

    l3 = tkinter.Label(text = 'Password:')
    l3.grid(column=4, row=2, padx=5, sticky=tkinter.E)

    passwordText = tkinter.Entry()
    passwordText.grid(column=5, row=2)

    passwordButton = tkinter.Button(text='Copy', command=copyToCliboard(root, passwordText))
    passwordButton.grid(column=6, row=2, padx=5)

    def addDialogCallback(password):
        PASSWORD.append(password)

        records.insert(tkinter.END, PASSWORD[len(PASSWORD) - 1]['web'])

    addButton = tkinter.Button(text = 'Add')
    addButton.bind('<Button>', lambda _: addDialog(root, addDialogCallback))
    addButton.grid(column=0, row=4, pady=5)

    removeButton = tkinter.Button(text = 'Remove')
    removeButton.bind('<Button>', delete)
    removeButton.grid(column=1, row=4, pady=5)

    root.mainloop()

    save_passwords(DATA_FILENAME, PASSWORD, 'heslo')

if __name__ == '__main__':
    main()