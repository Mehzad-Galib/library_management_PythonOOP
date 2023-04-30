class User:

    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []


class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list

    def borrow_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("return pls")
                    return
                if self.book_list[book] == 0:
                    print("sorry no books available")
                    return

                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print('you borrowed a book')
                return
        print('not available')

    def return_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += 1
                user.borrow_books.remove(bookName)
                user.returned_books.append(bookName)
                print('book returned successfully')

        print('kar boi ferot dite ascho?')

    def check_availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book)

    def donate_book(self, bookName, amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Book donated successfully")
                return

        self.book_list[book] = amount


library = Library({"English": 2, "Bangla": 5, "Math": 3})
allUsers = []
currentUser = None


while True:
    if currentUser == None:
        print("Not logged in\nPlease login or create accunt (L/C)")
        option = input()
        if option == 'L':
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password:
                    currentUser = user
                    match = True

            if match == False:
                print("No user found")

        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            user = User(name, roll, password)
            currentUser = user
            allUsers.append(user)

    else:
        print("Options\n_________")
        print("1. Borrow a Book\n2. Return a Book\n3. Check Availability\n4. Donate Book\n5. Exit")
        x = int(input("Give Option: "))
        if x == 1:
            bookName = input("Enter book name: ")
            library.borrow_book(bookName, currentUser)

        if x == 2:
            bookName = input("Enter book name: ")
            library.return_book(bookName, currentUser)

        if x == 3:
            library.check_availability()
        if x == 4:
            bookName = input("Enter book name: ")
            amount = int(input("Enter Amount of Books: "))
            library.donate_book(bookName, amount)

        if x == 5:
            break
