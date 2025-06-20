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
