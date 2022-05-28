## Project 2 Python - Library Management System ##
## Functionalites:
    # Fetch all the availablebooks in the library
    # Add new books
    # Keep track of borrowed books
    # Update the details bsed on the books returned
    # Implement OOP
## Project Flow:
    # 1st step from users pov would be to display the menu
    #       of the library management system w/options:
        # 1 Display Books - displayBooks()
        # 2 Lend a Book - lendBook()
        # 3 Add a Book - addBook()
        # 4 Return a book - returnBook()
    # Depending on choice entered, we would need to perform the
    #       operation and return the details to the output screen
    # The process must be done repeatedly until user quits
## Approach:
    # The major focus will be on OOP, we will have a class that
    #       is responsible for the creation of the library object
    #       A single library object would represent one library
    # Thus the idea od using OOP is t bring the foctor of reusability
    #       Therefore, this software can be used by as many libraries 
    #       as needed by just creating a new object #
class Library:
    def __init__(self, booklist, name):
        self.bookList = booklist
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f'We have the following books in our library: {self.name}')
        for book in self.bookList:
            print(book)