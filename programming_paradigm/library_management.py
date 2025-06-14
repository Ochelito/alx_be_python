"""Implementing Basic OOP for a Library Management System
mandatory
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
Expected Outputs for Each Step in main.py:
After Initial Setup:
   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
After Checking Out ‘1984’:
   Available books after checking out '1984':
   Brave New World by Aldous Huxley
After Returning ‘1984’:
   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell
Note for you:
Your Book class should provide methods to check a book out and return it, affecting its availability.
Your Library class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly."""

class Book:
    def __init__(self, title, author): #The __init__ method is the constructor. It's automatically called when a new Book object is created. It takes title and author as arguments and assigns them to the book.
        self.title = title
        self.author = author
        self._is_checked_out = False #It's initialized as False, meaning the book is available by default.

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True                     #It marks the book as checked out and returns True to indicate success.
        return False                #If the book was already checked out, it returns False (i.e., the checkout failed).

    def return_book(self):          #If the book was checked out, this marks it as available again and returns True.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False                #If the book wasn’t checked out, return False (no action needed).

    def is_available(self):
        return not self._is_checked_out #This method tells whether the book is available for checkout.It returns True if _is_checked_out is False.

    def __str__(self): #This special method allows you to control what gets printed when you do print(book).
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self._books = [] #The constructor initializes a private list _books to store all the Book instances.

    def add_book(self, book):
        if isinstance(book, Book):      #It checks that the object being added is actually an instance of the Book class.
            if any(b.title.lower() == book.title.lower() for b in self._books):     #It checks that the object being added is actually an instance of the Book class.
                print(f"The book '{book.title}' already exists in the library.")    #This avoids adding duplicate books by comparing titles (case-insensitive).
            else:
                self._books.append(book) 
        else:
            print("Only Book instances can be added.") #If you try to add something that isn't a Book, a warning is shown.

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"You checked out {book}")
                return
        print(f"'{title}' is not available or does not exist.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"You returned {book}")
                return
        print(f"'{title}' is not currently checked out or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f" - {book}")


    
