import re


def validate_isbn(isbn):
    """
    Validate ISBN-10 or ISBN-13 format.
    """
    isbn = isbn.replace("-", "").replace(" ", "").upper()
    match = re.match(r"^(\d{9}[\dX]|\d{13})$", isbn)
    return bool(match)


def format_currency(amount):
    """
    Format a float as currency (USD).
    """
    return f"${amount:.2f}"


def truncate_string(string, length):
    """
    Truncate a string to a specified length, adding '...' if truncated.
    """
    return string[:length] + "..." if len(string) > length else string
