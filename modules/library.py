# library.py

class Book:
    def __init__(self, title, author, year, copies_available):
        self.title = title
        self.author = author
        self.year = year
        self.copies_available = copies_available

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Copies Available:", self.copies_available)
        print("-" * 30)

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        self.copies_available += 1
        print(f"You returned '{self.title}'.")
