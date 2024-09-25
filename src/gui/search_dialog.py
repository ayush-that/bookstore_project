from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
)


class SearchDialog(QDialog):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Search Books")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        layout.addWidget(QLabel("Search:"))
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_books)
        layout.addWidget(self.search_button)

        self.results_list = QListWidget()
        layout.addWidget(self.results_list)

        self.setLayout(layout)

    def search_books(self):
        keyword = self.search_input.text()
        books = self.db.search_books(keyword)
        self.results_list.clear()
        for book in books:
            self.results_list.addItem(str(book))
