from flask import Flask
from src.database.database import Database

app = Flask(__name__)
db = Database("bookstore.db")

from src.web import routes
