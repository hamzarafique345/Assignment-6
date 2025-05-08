# Assignment 11:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_book = 0

    def __init__(self,name):
        self.name = name 
        Book.incrementcount()
    
    @classmethod
    def incrementcount(cls):
        cls.total_book += 1

book1 = Book("Tommy")
book2 = Book("Avenger")
print(Book.total_book)
