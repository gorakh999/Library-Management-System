class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    # Display all available books
    def displayAvailableBooks(self):
        print("\nBooks Present in this Library are : ")
        for book in self.books:
            print('\t' + book)

    # Borrow Book from Library
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"\nYou Have been Issued {bookName}. Please Keep it safe and return it with in 14 days")
            self.books.remove(bookName)
            return True

        else:
            print("\n Sorry This Book is Not Available in The Library")
            return False

    # Return Book to Library
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("\nThanks for Returning this Book")   

class Student:

    # Request Book 
    def requestBook(self):
        self.book = input("\nEnter Name of the Book you Want to Borrow : ")
        return self.book

    # Return Book or Add a new Book to the Library
    def returnBook(self):
        self.book = input("\nEnter Name of the Book you Want to Return : ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    # centralLibrary.displayAvailableBooks()
    s1 = Student()
    while (1):
        welcomeMsg = '''\n=====Welcome to Central Library=====. 
        Please Choose an Option
        1. Listing all the Book
        2. Request a book
        3. Add/Return a Book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a Choice : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            bookname = s1.requestBook()
            centralLibrary.borrowBook(bookname)
            

        elif a == 3:
            bookname = s1.returnBook()
            centralLibrary.returnBook(bookname)

        elif a == 4:
            print("Thank You for Using the Library")
            input()
            exit()

        else:
            print("Invalid Choice")