# TASK: Add remove_book method and update using File Handling and Exception Handling

class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author


class EBook(Book):
    def __init__(self, title, pages, author, filesize):
        super().__init__(title, pages, author)
        self.filesize = filesize


harry_potter = Book("Harry Potter", 105, "Ujjwal Neupane")
abc = Book("ABC", 125, "ABC")
spiderman = EBook("Spiderman", 200, "Ujjwal Neupane", "0.6GB")


class LMS:
    def __init__(self):
        self.books = []
        self.load_books()

    # ---------- FILE HANDLING ----------
    def load_books(self):
        try:
            file = open("books.txt", "r")
            for line in file:
                data = line.strip().split(",")
                if data[0] == "BOOK":
                    self.books.append(Book(data[1], int(data[2]), data[3]))
                else:
                    self.books.append(EBook(data[1], int(data[2]), data[3], data[4]))
            file.close()
        except FileNotFoundError:
            pass

    def save_books(self):
        file = open("books.txt", "w")
        for book in self.books:
            if isinstance(book, EBook):
                file.write(f"EBOOK,{book.title},{book.pages},{book.author},{book.filesize}\n")
            else:
                file.write(f"BOOK,{book.title},{book.pages},{book.author}\n")
        file.close()

    # ---------- LMS METHODS ----------
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self):
        title = input("Enter book name to remove: ")

        try:
            for book in self.books:
                if book.title == title:
                    self.books.remove(book)
                    self.save_books()
                    print("Book removed.")
                    return
            raise Exception("Book not found.")
        except Exception as e:
            print(e)

    def search_book(self):
        name = input("Enter book name: ")
        for book in self.books:
            if book.title == name:
                print("Book found.")
                return
        print("Book not found.")

    def display(self):
        for i in self.books:
            print(i.title)
            print(i.pages)
            print(i.author)

            if isinstance(i, EBook):
                print(i.filesize)
            else:
                print("Book is physical product")
            print("-" * 20)


# ---------- RUN ----------
lms1 = LMS()

lms1.add_book(harry_potter)
lms1.add_book(spiderman)
lms1.add_book(abc)

lms1.display()
lms1.remove_book()
