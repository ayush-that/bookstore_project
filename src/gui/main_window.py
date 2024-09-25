from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
)
from src.gui.add_book_dialog import AddBookDialog
from src.gui.search_dialog import SearchDialog
from src.database.database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database("bookstore.db")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bookstore Management System")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.add_book_btn = QPushButton("Add Book")
        self.add_book_btn.clicked.connect(self.show_add_book_dialog)
        layout.addWidget(self.add_book_btn)

        self.search_btn = QPushButton("Search Books")
        self.search_btn.clicked.connect(self.show_search_dialog)
        layout.addWidget(self.search_btn)

        self.book_table = QTableWidget()
        self.book_table.setColumnCount(5)
        self.book_table.setHorizontalHeaderLabels(
            ["ID", "Title", "Author", "ISBN", "Price"]
        )
        layout.addWidget(self.book_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.update_book_table()

    def show_add_book_dialog(self):
        dialog = AddBookDialog(self.db)
        if dialog.exec_():
            self.update_book_table()

    def show_search_dialog(self):
        dialog = SearchDialog(self.db)
        dialog.exec_()

    def update_book_table(self):
        books = self.db.search_books("")
        self.book_table.setRowCount(len(books))
        for row, book in enumerate(books):
            self.book_table.setItem(row, 0, QTableWidgetItem(str(book.id)))
            self.book_table.setItem(row, 1, QTableWidgetItem(book.title))
            self.book_table.setItem(row, 2, QTableWidgetItem(book.author))
            self.book_table.setItem(row, 3, QTableWidgetItem(book.isbn))
            self.book_table.setItem(row, 4, QTableWidgetItem(str(book.price)))
