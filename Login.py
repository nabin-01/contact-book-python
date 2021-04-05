import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk
import tkinter.messagebox as tkm

class Login:
    # Defining constructor for Login class
    def __init__(self, master):
        master.title("Login")
        master.resizable(False, False)
        master.attributes('-topmost', 'true')

        # Defining GUI attributes
        self.arialRegular = tkf.Font(family="Arial", size=10, weight="normal")
        self.arialBold = tkf.Font(family="Arial", size=10, weight="bold")

        self.labelEmail = tk.Label(master, font=self.arialBold, text="Email")
        self.labelPassword = tk.Label(master, font=self.arialBold, text="Password")

        self.entryEmail = tk.Entry(master, font=self.arialRegular, width=20)
        self.entryPassword = tk.Entry(master, font=self.arialRegular, width=20)

        self.buttonLogin = tk.Button(master, font=self.arialBold, text="Login", command=self.login)
        self.buttonExit = tk.Button(master, font=self.arialBold, text="Exit", command=self.exit)

        # Drawing GUI with .grid
        self.labelEmail.grid(row=0, column=0)
        self.labelPassword.grid(row=1, column=0)
        self.entryEmail.grid(row=0, column=1)
        self.entryPassword.grid(row=1, column=1)
        self.buttonLogin.grid(row=2, column=0)
        self.buttonExit.grid(row=2, column=1)
    
    # Called by buttonLogin - after checks sends login information to SMTP instance
    def login():
        pass
    
    # Called by buttonExit - exits out of the login screen with prompt
    def exit():
        pass