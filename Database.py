import sqlite3 as sql

# This class handles all database interactions via the SQLite3 library.
class Database:
    # This function is ran when the Database class is instantiated.
    # Creates and connects to an SQL database & creates the necessary tables if they don't exist.
    def __init__(self):
        self.connection = sql.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            cid PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE
        )''')
        self.connection.commit()

    # This function inserts a new contact into the contacts -table in the database.db
    def insert(self):
        # TODO: Name, Address, Email & Phone value calls from GUI when creating a contact
        self.cursor.execute('INSERT INTO contacts (name, address, email, phone) VALUES (?,?,?,?)', (self.name, self.address, self.email, self.phone))
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
