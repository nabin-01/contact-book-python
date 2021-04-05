import sqlite3 as sql
from sqlite3 import Error

class Database:
    # Defining constructor for Database class
    def __init__(self):
        # Try to connect to or create database.db & create contacts table if it doesn't exist
        try:
            self.connection = sql.connect("database.db")
            self.cursor = self.connection.cursor()
            # Using UNIQUE constraints to avoid duplicate contacts 
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE,
                phone TEXT UNIQUE,
                address TEXT
            )''')
            self.connection.commit()
        # If something goes wrong, return the error for traceback
        except Error as e:
            return e

    # Add a contact into the database.db contacts table
    def insert(self, name, email, phone, address):
        self.cursor.execute('INSERT INTO contacts (name, email, phone, address) VALUES (?,?,?,?)', (name, email, phone, address))
        self.connection.commit()

    # Remove a contact from the database.db contacts table
    def remove(self, id):
        self.cursor.execute('SELECT FROM contacts WHERE id = ?', id)
        self.connection.commit()
