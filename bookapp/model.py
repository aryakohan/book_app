import sqlite3
from sys import path

class PrimaryKeyError(Exception):
    pass

database = sqlite3.connect(path[0]+"/books_db.db",check_same_thread=False)
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books_table( isbn INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER, price INTEGER, pages INTEGER, genre TEXT)")

def insert_book(isbn, title, author, year, price, pages, genre):
    try:
        cursor.execute("INSERT INTO books_table VALUES (?,?,?,?,?,?,?)", (isbn, title, author, year, price, pages, genre))
        database.commit()
    except(sqlite3.IntegrityError):
        raise PrimaryKeyError("isbn must be a unique number")
    print(f"The book '{title}' has been added to the library.")

def allbooks():
    return list(cursor.execute("SELECT * FROM books_table"))

def update_book(isbn1,isbn2):
    cursor.execute("UPDATE books_table SET isbn=? WHERE isbn=?",[isbn1 , isbn2])
    database.commit()

def update_book1(price,isbn):
    cursor.execute("UPDATE books_table SET price=? WHERE isbn=?",[price , isbn])
    database.commit()


def delete_book(isbn):
    cursor.execute("DELETE FROM books_table WHERE isbn=?", (isbn,))
    database.commit()


