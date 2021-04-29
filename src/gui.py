import tkinter

from src.library import generate_password

def addDialog(root, addCallback):
    top = tkinter.Toplevel(root)
    top.title('Add')
    top.transient(root)
    top.grab_set()

    webLabel = tkinter.Label(top, text = 'Web:')
    webLabel.grid(column=0, row=0, pady=5, padx=5, sticky=tkinter.E)

    webText = tkinter.Entry(top)
    webText.grid(column=1, row=0, pady=5, padx=5)

    usernameLabel = tkinter.Label(top, text = 'Username:')
    usernameLabel.grid(column=0, row=1, pady=5, padx=5, sticky=tkinter.E)

    usernameText = tkinter.Entry(top)
    usernameText.grid(column=1, row=1, pady=5, padx=5)

    passwordLabel = tkinter.Label(top, text = 'Password:')
    passwordLabel.grid(column=0, row=2, pady=5, padx=5, sticky=tkinter.E)

    passwordText = tkinter.Entry(top)
    passwordText.grid(column=1, row=2, pady=5, padx=5)

    def ok():
        password = passwordText.get()
        if password == '':
            password = generate_password(16)

        addCallback({
            'web': webText.get(),
            'username': usernameText.get(),
            'password': password
        })

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