from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from src.models.book import Book


class AddBookDialog(QDialog):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add New Book")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)

        self.author_input = QLineEdit()
        layout.addWidget(QLabel("Author:"))
        layout.addWidget(self.author_input)

        self.isbn_input = QLineEdit()
        layout.addWidget(QLabel("ISBN:"))
        layout.addWidget(self.isbn_input)

        self.price_input = QLineEdit()
        layout.addWidget(QLabel("Price:"))
        layout.addWidget(self.price_input)

        self.add_button = QPushButton("Add Book")
        self.add_button.clicked.connect(self.add_book)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()
        price = float(self.price_input.text())

        book = Book(title, author, isbn, price)
        self.db.add_book(book)
        self.accept()
