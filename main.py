import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox as tkm
import sqlite3 as sql
import smtplib as smtp
import ssl as ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Main:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")
        master.resizable(False, False)

        # Defining Fonts
        self.arial10bold = tkf.Font(family="Arial", size=10, weight="bold")
        self.arial10regular = tkf.Font(family="Arial", size=10, weight="normal")

        # Defining GUI
        self.label_name = tk.Label(master, text="Name", font=self.arial10bold)
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(master, width=20, font=self.arial10regular)
        self.entry_name.grid(row=0, column=1)

        self.label_email = tk.Label(master, text="Email", font=self.arial10bold)
        self.label_email.grid(row=1, column=0)
        self.entry_email = tk.Entry(master, width=20, font=self.arial10regular)
        self.entry_email.grid(row=1, column=1)

        self.label_phone = tk.Label(master, text="Phone", font=self.arial10bold)
        self.label_phone.grid(row=2, column=0)
        self.entry_phone = tk.Entry(master, width=20, font=self.arial10regular)
        self.entry_phone.grid(row=2, column=1)

        self.button_add = tk.Button(master, text="ADD", font=self.arial10regular, command=self.add)
        self.button_add.grid(row=3, column=0)
        self.button_delete = tk.Button(master, text="DEL", font=self.arial10regular, command=self.delete)
        self.button_delete.grid(row=3, column=1)

    def add(self):
        if self.entry_name.get() == "" or self.entry_email.get() == "" or self.entry_phone.get() == "":
            tkm.showinfo(title="INFO", message="Please make sure all fields are filled with valid, unique contact information before adding a contact.")
        elif "@" in self.entry_email.get() and self.entry_phone.get().isdigit():
            # TODO: Add contact to database
            pass
        else:
            tkm.showinfo(title="INFO", message="Please make sure you have entered valid information before adding a contact.")

    def delete(self):
        if self.entry_name.get() == "":
            tkm.showinfo(title="INFO", message="Please make sure the name field is not empty when deleting a contact.")
        elif self.entry_name.get().isdigit():
            # TODO: Delete contact from database based on the ID
            pass
        else:
            tkm.showinfo(title="INFO", message="Please make sure the name field has a valid contact ID to delete.")


class Database:
    def __init__(self):
        self.connection = sql.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            cid PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE
        )''')
        self.connection.commit()

    # This function inserts a new contact into the contacts -table in the database.db
    def insert(self):
        # TODO: Name, Address, Email & Phone value calls from GUI when creating a contact
        self.cursor.execute('INSERT INTO contacts (name, address, email, phone) VALUES (?,?,?,?)', (self.name, self.email, self.phone))
        self.connection.commit()

    # This function selects & deletes a contact from the contacts -table in the database.db based on CID (contact ID) which is a unique Primary Key
    def remove(self):
        # TODO: Contact ID call from the GUI when deleting a contact
        self.cursor.execute('SELECT FROM contacts WHERE cid = ?', self.cid)
        self.connection.commit()

    # This function selects all contacts from the contacts -table in the database.db - Used for displaying all contacts in the database in the GUI
    def select_all(self):
        self.cursor.execute('SELECT * FROM contacts')
        self.connection.commit()


class SMTP:
    # This function is called when the SMTP class is instantiated
    # Fetches user credentials to log into SMTP server, establishes secure connection via TLS & tests the integrity of the connection
    def __init__(self):
        self.smtp = "smtp.gmail.com"  # using gmail smtp server for development purposes
        self.port = 587
        self.user_email = 1  # TODO: User email input when application starts (for SMTP login)
        self.password = 1  # TODO: User password input when application starts (for SMTP login)
        self.recipient_email = 1  # TODO: Fetch Recipient email(s) from GUI as defined by user
        self.ssl_context = ssl.create_default_context()
        server = smtp.SMTP(self.smtp, self.port)

        # Test integrity of connection, if connection is not established properly print error messages for traceback
        try:
            server.starttls(context=self.ssl_context)
            server.login(self.user_email, self.password)
        except Exception as e:
            print(e)
        finally:
            server.quit()

    # This functions connects to the SMTP server defined in __init__ & sends the user's message to the selected contact(s)
    def send(self):
        server = smtp.SMTP(self.smtp, self.port)
        server.starttls(context=self.ssl_context)
        server.login(self.user_email, self.password)

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.user_email
        self.message["To"] = self.recipient_email
        self.text = """ TEST """  # TODO: Fetch plain text version of the message from GUI
        self.html = """ <html>
                                <body>
                                    <h1> HTML TEST <h1>
                                </body>
                            </html> 
                            """
        # TODO: Fetch html version of the message from GUI
        self.plaintext = MIMEText(self.text, "plain")
        self.htmltext = MIMEText(self.html, "html")
        self.message.attach(self.plaintext)
        self.message.attach(self.htmltext)

        server.sendmail(self.user_email, self.recipient_email, self.message.as_string())


if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()
