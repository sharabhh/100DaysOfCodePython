class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addBooks(self, bookName):
        self.books.append(bookName)
        self.no_of_books +=1

    def showAllBooks(self):
        for book in self.books:
            print(f"{book}")

a = Library()
a.addBooks("Harry Potter")
a.addBooks("Twilight")
a.showAllBooks()
# print(a.no_of_books)