class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def info(self):
        status = "Bor" if self.available else "Berilgan"
        return f"{self.title} - {self.author} | {status}"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow(self, book):
        self.books.append(book)


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def show_books(self):
        for i, b in enumerate(self.books):
            print(i, b.info())

    def lend_book(self, book_index, reader_index):
        book = self.books[book_index]
        if book.available:
            book.available = False
            self.readers[reader_index].borrow(book)
            print("Kitob berildi")
        else:
            print("Kitob band")

    def report(self):
        for r in self.readers:
            print(r.name, "olgan kitoblar:", len(r.books))


lib = Library()

while True:
    print("\n1.Kitob 2.O‘quvchi 3.Ijara 4.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        lib.add_book(Book(input("Nomi: "), input("Muallif: ")))
    elif c == "2":
        lib.add_reader(Reader(input("Ism: ")))
    elif c == "3":
        lib.lend_book(int(input("Kitob index: ")), int(input("O‘quvchi index: ")))
    elif c == "4":
        lib.report()
    elif c == "0":
        break
