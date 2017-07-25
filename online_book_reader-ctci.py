class OnlineLibrary(object):
    """ An online library management system """
    def __init__(self):
        self.library = Library()
        self.user_manager = UserManager()
        self.display = Display(self)

    def set_active_book(self, book):
        self.active_book = book
        self.display.set_display_book(book)

    def get_active_book(self):
        return self.active_book

    def set_active_user(self, user):
        self.active_user = user
        self.display.set_display_user(user)

    def get_active_user(self):
        return self.active_user


class Library(object):
    """ The collection of books associated with a library """

    def __init__(self):
        self.books = set([])

    def add_book(self, author, title, pages):
        self.books.add(Book(author, title, pages))
        return

    def remove_book(self, book):
        self.books.remove(book)
        return

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


class Book(object):
    """ Individual books """

    def __init__(self, author, title, length):
        self.author = author
        self.title = title
        self.length = length


class UserManager(object):
    """ A class to encapsulate user methods """

    users = set([])

    @classmethod
    def add_user(cls, name, details):
        cls.users.add(User(name, details))

    @classmethod
    def find(cls, name):
        for user in cls.users:
            if user.name == name:
                return user


class User(object):
    """ An individual user of the library """

    def __init__(self, name, details):
        self.name = name
        self.details = details


class Display():
    """ Display of current reader, book and page. """

    def __init__(self, online_reader):
        self.online_reader = online_reader

    def set_display_user(self, user):
        self.active_user = user

    def set_display_book(self, book):
        self.active_book = book
        self.current_page = 1

    def show_status(self):
        print "%s is reading %s and is on page %d" % (self.active_user.name, 
                                                      self.active_book.title, 
                                                      self.current_page)

    def turn_page(self):
        if self.current_page < self.active_book.length:
            self.current_page += 1
            print "on page %d" % self.current_page
        else:
            print "on last page"

    def turn_page_back(self):
        if self.current_page > 0:
            self.current_page -= 1
            print "on page %d" % self.current_page
        else:
            print "on first page"


if __name__ == "__main__":
    online_reader = OnlineLibrary()
    online_reader.library.add_book("JK", "HP", 123)
    online_reader.library.add_book("JR", "Hobbit", 789)
    online_reader.user_manager.add_user("sally", "things")
    online_reader.user_manager.add_user("bob", "things")

    user = online_reader.user_manager.find("sally")
    book = online_reader.library.find_book("Hobbit")

    online_reader.set_active_user(user)
    online_reader.set_active_book(book)

    online_reader.display.show_status()
    online_reader.display.turn_page()
    online_reader.display.turn_page_back()
    online_reader.display.turn_page_back()
