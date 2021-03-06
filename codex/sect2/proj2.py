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
    def addBook(self, book):
        if book in self.bookList:
            print('Book already exists')
        else:
            self.bookList.append(book)
            bookDB = open(databaseName, 'a')
            bookDB.write("\n")
            bookDB.write(book)
            print('Book Added')
    def lendBook(self, book, user):
        if book in self.bookList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("Book has been lended. DB updated")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print('Apologies! We dont have this in our library')
    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book Returned Successfully')
        else:
            print("The book does not exist in the Book Lending DB")

def main():
    while(True):
        print(f"Welcome to the {library.name} library. The following are the options:" )
        choice = "1. Display Books 2. Lend a Book 3. Add a Book 4. Return a Book"
        print(choice)
        userInput = input('Press Q to quit and C to continue:')
        if userInput == 'C':
            userChoice = int(input("Select an option to continue:"))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend:")
                user = input("Enter the name of the user:")
                library.lendBook(book, user)
            elif userChoice == 3:
                book = input("Enter the name of the book you want to add:")
                library.addBook(book)
            elif userChoice == 4:
                book = input("Enter the name of the book you want to return:")
                library.returnBook(book)
            else: 
                print("Please select a valid option")
        elif userInput == 'Q':
            break
        else:
            print("Please enter a valid option [Q\C]")

if __name__ == '__main__':
    booksList = []
    databaseName = input("Enter the name of the database file with and extension:")
    bookDB = open(databaseName, 'r')
    for book in bookDB:
        booksList.append(book)
    library = Library(booksList, "Python")
    main()

