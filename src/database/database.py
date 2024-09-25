import sqlite3
from src.models.book import Book


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS books
                            (id INTEGER PRIMARY KEY,
                             title TEXT,
                             author TEXT,
                             isbn TEXT,
                             price REAL)"""
        )
        self.conn.commit()

    def add_book(self, book):
        self.cur.execute(
            "INSERT INTO books (title, author, isbn, price) VALUES (?, ?, ?, ?)",
            (book.title, book.author, book.isbn, book.price),
        )
        self.conn.commit()
        book.id = self.cur.lastrowid
        return book

    def get_book(self, book_id):
        self.cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = self.cur.fetchone()
        if row:
            return Book.from_dict(
                dict(zip(["id", "title", "author", "isbn", "price"], row))
            )
        return None

    def update_book(self, book):
        self.cur.execute(
            "UPDATE books SET title = ?, author = ?, isbn = ?, price = ? WHERE id = ?",
            (book.title, book.author, book.isbn, book.price, book.id),
        )
        self.conn.commit()

    def delete_book(self, book_id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()

    def search_books(self, keyword):
        self.cur.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?",
            ("%" + keyword + "%", "%" + keyword + "%", "%" + keyword + "%"),
        )
        return [
            Book.from_dict(dict(zip(["id", "title", "author", "isbn", "price"], row)))
            for row in self.cur.fetchall()
        ]

    def close(self):
        self.conn.close()
