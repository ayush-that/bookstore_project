from flask import render_template, request, redirect, url_for
from src.web.app import app, db
from src.models.book import Book


@app.route("/")
def index():
    books = db.search_books("")
    return render_template("index.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keyword = request.form["keyword"]
        books = db.search_books(keyword)
        return render_template("search_results.html", books=books, keyword=keyword)
    return render_template("search_results.html", books=[], keyword="")


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            isbn=request.form["isbn"],
            price=float(request.form["price"]),
        )
        db.add_book(book)
        return redirect(url_for("index"))
    return render_template("add_book.html")
