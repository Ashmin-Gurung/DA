# Task: Create a Simple Book Class
# Objective: Design a class to represent a book, including its title, author, and a method to display the book's information.

class Book:
    def book_info(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Creating a Book object for "The Fault in Our Stars"
book1 = Book()
book1.book_info("The Fault in Our Stars", "John Green")

# Displaying its information
book1.display_info()
