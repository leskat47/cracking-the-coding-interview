class Library(object):

    def __init__(self, name):
        self.name = name
        self.books = set([])

    def add_book(self, book):
        self.books.add(book)

    def get_books(self):
        return self.books

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return


class Book(object):
    """ Individual books """

    def __init__(self, author, title, length):
        self.author = author
        self.title = title
        self.length = length


class User(object):

    def __init__(self, name, details, library):
        self.name = name
        self.details = details
        self.books = []
        self.library = library

    def show_books(self):
        print [(book.title, Reading.get_reading(self, book).status) for book in self.books]

    def add_book(self, title):
        book = self.library.get_book(title)
        if book:
            reading = Reading(self, book)
            if book in self.library.books:
                self.books.append(book)
                print "%s has been added to your reading list" % title
                return reading
        print "Sorry, that book is not available in your library"

    def update_book(self, title, status):
        book = self.library.get_book(title)
        reading = Reading.get_reading(self, book)
        reading.status = status


class Reading(object):
    """ An indiviual user reading a book """

    readings = []

    def __init__(self, user, book, status='to read'):
        self.status = status
        self.book = book
        self.user = user
        self.page = 0
        Reading.readings.append(self)

    def update_status(self, status):
        self.status = status

    def turn_page(self):
        if self.page < self.book.length:
            self.page += 1

    def turn_page_back(self):
        if self.page > 0:
            self.page -= 1

    @classmethod
    def get_reading(cls, user, book):
        for reading in cls.readings:
            if reading.book == book and reading.user == user:
                return reading


if __name__ == "__main__":
    library = Library("online reader")
    hp = Book("JK", "HP", 123)
    hb = Book("JR", "Hobbit", 789)
    library.add_book(hp)
    library.add_book(hb)

    sally = User("sally", "things", library)
    bob = User("bob", "things", library)

    hobbit = sally.add_book("Hobbit")
    hp = sally.add_book("HP")
    sally.show_books()
    hobbit.turn_page()
    sally.update_book("Hobbit", "finished")
    sally.show_books()


