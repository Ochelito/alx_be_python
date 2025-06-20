""" Dive into Python Magic Methods
mandatory
Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

Task Description:
Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

Requirements for Book Class in book_class.py:
Attributes:

title (str): The title of the book.
author (str): The author of the book.
year (int): The publication year of the book.
Magic Methods:

Constructor (__init__): Initializes a Book instance with title, author, and year.
Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
Provided for Testing: main.py
To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:"""


class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        #print(f"{self.title} by {self.author}, published in {self.year}")
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #print(f"{self.title} by {self.author}, published in {self.year}")
        return f"Book('{self.title}', '{self.author}', {self.year})"
