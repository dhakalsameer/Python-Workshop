# main.py

from library import Book

# Create book objects
book1 = Book("Python Programming", "John Smith", 2020, 5)
book2 = Book("Data Science Basics", "Alice Brown", 2019, 3)
book3 = Book("Machine Learning", "David Lee", 2022, 2)

# Borrow books
book1.borrow_book()
book2.borrow_book()
book3.borrow_book()

# Return a book
book1.return_book()

# Display all book details
print("\nLibrary Books Information:\n")

book1.display_info()
book2.display_info()
book3.display_info()
