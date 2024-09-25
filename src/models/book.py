class Book:
    def __init__(self, title, author, isbn, price, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "price": self.price,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            price=data["price"],
            id=data.get("id"),
        )
