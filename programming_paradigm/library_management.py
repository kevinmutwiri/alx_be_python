class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        book = self._find_book(title)
        if book:
            book.check_out()

    def return_book(self, title):
        book = self._find_book(title)
        if book:
            book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)
