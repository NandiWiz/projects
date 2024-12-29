class Library:
    def __init__(self):
        self.books=[]
    def buy_book(self,book):
        self.books.append(book)
randolph=Library()
class Book:
    def __init__(self,name,author,isbn):
        self.name=name
        self.author=author
        self.isbn=isbn
    def __str__(self):
        return self.name+ " " + self.author
book1 = Book("Harry Potter", "J.K.Rowling","61")
book2 = Book("Percy Jackson", "Rick Rordan","75")
randolph.buy_book(book1)
randolph.buy_book(book2)
for book in randolph.books:
    print(book)
