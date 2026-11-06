from datetime import datetime

line = "=" * 49
temp_line = "=" * 31

BOOK_FILE = "books.txt"
MEMBER_FILE = "members.txt"
ISSUE_BOOKS = "issue_books.txt"

# ====================================================================================#

# Book records aur books.txt file se related methods.
class Books:
    # Object ke fields ko initialize karta hai.
    def __init__(self, book_id, title, author, category, copies, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.copies = copies
        self.status = status

    # Book ki details screen par dikhata hai.
    def show_books(self):
        print("ID      :",self.book_id)
        print("Title   :",self.title)
        print("Author  :",self.author)
        print("Category:",self.category)
        print("Copies  :",self.copies)
        print("Status  :",self.status)
        print("-------------------------------")

    # Book ko pipe-separated text line mein badalta hai.
    def get_data(self):
        return f"{self.book_id}|{self.title}|{self.author}|{self.category}|{self.copies}|{self.status}\n"

    # books.txt se book records read karke objects ki list banata hai.
    def read_books(self):
        books = []            
        try:
            with open(BOOK_FILE, "r") as f:
                for line in f:

                    data = line.strip()

                    if not data:
                        print("No data found!..")
                        return

                    data = data.split("|")
                    
                    book_id  = data[0]
                    title    = data[1]
                    author   = data[2]
                    category = data[3]
                    copies   = int(data[4])
                    status   = data[5]

                    book = Books(book_id, title, author, category, copies, status)
                    books.append(book)

        except FileNotFoundError:
            pass

        return books

    # Author, category aur copies ki input validation karta hai.
    def book_validation(self, author, category, copies):
        if not author.replace(" ", "").isalpha():
            print("Author name allowed only in alphabets!..")
            return False

        if len(author) < 3:
            print("Invalid author name!..")
            return False

        if not category.replace(" ", "").isalpha():
            print("Category allowed only in alphabets!..")
            return False

        if len(category) < 2:
            print("Invalid category!..")

        if copies < 1 or copies > 100:
            print("Copies must be only between '1' and '100'!..")
            return False

        return True

    # Book list ko books.txt mein save karta hai.
    def save_books(self, books):
        try:
            with open(BOOK_FILE, "w") as f:

                for book in books:

                    f.write(book.get_data())

        except FileNotFoundError:
            print("File not found!..")


# Library members aur members.txt file se related methods.
class Members:
    # Object ke fields ko initialize karta hai.
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone

    # Member ki details screen par dikhata hai.
    def show_members(self):
        print("ID     :",self.member_id)
        print("Name   :",self.name)
        print("Phone  :",self.phone)
        print("------------------------")

    # Member ko pipe-separated text line mein badalta hai.
    def member_get_data(self):
        return f"{self.member_id}|{self.name}|{self.phone}\n"

    # members.txt se member records read karta hai.
    def read_members(self):
        members = []

        try:
            with open(MEMBER_FILE, "r") as f:
                for line in f:
                    data = line.strip()

                    if not data:
                        print("No data found!..")
                        return

                    data = data.split("|")
                        
                    member_id = data[0]
                    name = data[1]
                    phone = data[2]

                    member = Members(member_id, name, phone)

                    members.append(member)

        except FileNotFoundError:
            print("Member file not found!..")

        return members

    # Member name aur phone number ki validation karta hai.
    def member_validation(self, name, phone):

        if not name.replace(" ", "").isalpha():
            print("Name must be valid in alphabets!..")
            return False

        if len(name) < 3:
            print("Invalid name!..")
            return False

        if len(phone) < 10 or len(phone) > 10:
            print("Invalid phone number, try again!..")
            return False

        if not phone[0] in "6789":
            print("Invalid phone number!..")
            return False
        
        return True

    # Member list ko members.txt mein save karta hai.
    def save_members(self, members):
        with open(MEMBER_FILE, "w") as f:
            for member in members:
                f.write(member.member_get_data())


# Issue/return transaction records ke methods.
class Issued_books:
    # Object ke fields ko initialize karta hai.
    def __init__(self, transaction_id, member_name, book_title, issue_date, return_date):
        self.transaction_id = transaction_id
        self.member_name = member_name
        self.book_title = book_title
        self.issue_date = issue_date
        self.return_date = return_date

    # Issue transaction ki details dikhata hai.
    def show_issued_books(self):
        print("Transaction ID :",self.transaction_id)
        print("Member ID      :",self.member_name)
        print("Book ID        :",self.book_title)
        print("Issued Date    :",self.issue_date)
        print("Return Date    :",self.return_date)
        print("------------------------------")

    # issue_books.txt se issue records read karta hai.
    def read_issued_books(self):
        issued_books = []

        try:
            with open(ISSUE_BOOKS, "r") as f:
                for line in f:

                    data = line.strip()

                    if not data:
                        print("~No data found!..")
                        return
                    
                    else:
                        data = data.split("|")

                        transaction_id = data[0]
                        member_name    = data[1]
                        book_title     = data[2]
                        issue_date     = data[3]
                        return_date    = data[4]

                        issued_book = Issued_books(transaction_id, member_name, book_title, issue_date, return_date)

                        issued_books.append(issued_book)

        except FileNotFoundError:
            pass

        return issued_books

    # Issue record ko text line mein badalta hai.
    def issued_get_data(self):
        return f"{self.transaction_id}|{self.member_name}|{self.book_title}|{self.issue_date}|{self.return_date}\n"

    # Issue date aur return date ko validate karta hai.
    def issued_book_validation(self, issue_date, return_date):
        if return_date <= issue_date:
            print("Invalid return date!..")
            return False

        return True

    # Issued books ki list ko file mein save karta hai.
    def save_issued_books(self, issued_books):
        with open(MEMBER_FILE, "w") as f:
            for issued_book in issued_books:
                f.write(issued_book.issued_get_data())

# Library ke menu aur saare operations ko manage karne wali class.
class LibraryManagement(Books, Members, Issued_books):

    # Object ke fields ko initialize karta hai.
    def __init__(self):
        self.books       = []
        self.members     = []
        self.issue_books = []

    # Main menu ke options display karta hai.
    def menu(self):
        print("")
        print(line)
        print("           LIBRARY MANAGEMENT SYSTEM  ")
        print(line)
        print(" 1. Add Book            2. Show Books            ")
        print(" 3. Search Book         4. Update Book(Details)  ")
        print(" 5. Check Book(Status)  6. Delete Book           ")
        print("-------------------------------------------------")
        print(" 7. Add Member          8. Show Members          ")
        print(" 9. Search Member      10. Update Member(Details)")
        print("11. Delete Member                                ")
        print("-------------------------------------------------")
        print("12. Issue Book         13. Show Issued Books     ")
        print("14. Seach Issued Book  15. Update Issue Record   ")
        print("16. Return Book        17. Exit Program          ")
        print("=================================================")

    # Return date aa chuki ho to book ka status update karne ki koshish karta hai.
    def update_overdue_returns(self, books, issued_books):
        today = datetime.now().date()
        books_to_save = False

        for issued_book in issued_books:
            return_date = datetime.strptime(
                issued_book.return_date, "%d-%m-%Y"
            ).date()

            if today >= return_date:
                for book in books:
                    if book.title == issued_book.book_title:
                        book.status = "Available"
                        books_to_save = True
                        break

        if books_to_save:
            self.save_books(books)

    # Nayi book ki details lekar list mein add karta hai.
    def add_books(self, books):
        if len(books) == 0:
            book_id = "B001"

        else:
            last_id = books[-1].book_id
            number = int(last_id[1:]) + 1    
            book_id = f"B{number:03d}"
        
        print(f"ID : {book_id}\n")

        try:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            category = input("Enter Book Category: ")
            copies = int(input("Enter Number of Copies: "))
            print("")
            status = "Available"

        except ValueError:
            print("Invalid details!..")

        else:
            valid = self.book_validation(author, category, copies)

            if valid:
                book = Books(book_id, title, author, category, copies, status)

                books.append(book)

                with open(BOOK_FILE, "a") as f:
                    f.write(f"{book.get_data()}")

                print(f"Book ID : '{book_id}', added successfully!..")

            else:
                return


    # Saari books ki details display karta hai.
    def show_books_func(self, books):
        print("")
        print(temp_line)
        print("-----------BOOK-LIST-----------")
        print(temp_line)

        for book in books:
            book.show_books()

    # Book ko search karta hai.
    def search_book(self, books):
        book_id_to_search = input("Enter book id to search: ")

        print("\nBook(s) Found..")
        for book in books:

            if book_id_to_search in book.book_id:
                book.show_books()

            else:
                print("Book not found with given details!..")

    # Maujooda book ki details update karta hai.
    def update_book_details(self, books):
        book_id_to_update = input("Enter book id to update: ")
        found = False

        for book in books:

            if book_id_to_update == book.book_id:
                found = True
                print("\nBook Found..")
                book.show_books()

                print("\nEnter New Details to Update..")
                new_title = input("Enter new title: ")
                new_author = input("Enter new author name: ")
                new_category = input("Enter new category: ")
                new_copies = int(input("Enter new copies quantity: "))

                valid = self.book_validation(new_author, new_category, new_copies)
                
                if valid:
                    book.title = new_title
                    book.author = new_author 
                    book.category = new_category
                    book.copies = new_copies

                    self.save_books(books)

                    print("Book details updated successfully!..")
                    return

        if not found:
            print("Book not found with given details!..")

    # Book ki availability/status check karta hai.
    def check_book_status(self, books):
        id_to_check_status = input("Enter book id to check status: ")

        for book in books:
            if id_to_check_status in book.book_id:
                print(f"BOOK TITLE  : {book.title}")
                print(f"BOOK STATUS : {book.status}")
                return

            else:
                print("Book not found with given details!..")

    # Book record delete karta hai.
    def delete_book(self, books):
        id_to_delete = input("Enter book id to delete: ")

        for book in books:
            if id_to_delete == book.book_id:

                print("Book found!..")
                book.show_books()

                book_quantity_to_delete = int(input("Enter book quantity to delete: "))
                if book_quantity_to_delete <= 0:
                    print("Quantity must be greater than '0' !..")
                    reid
                else:
                    book.copies -= book_quantity_to_delete
                    
                    print(f"Book '{title_to_delete}' deleted '{book_quantity_to_delete}' copies successfuly!..")

                    self.save_books(books)

                    if int(book.copies) == 0:
                    
                        books.remove(book)
                        print(f"Book '{title_to_delete}' fully deleted successfully!..")
                        self.save_books(books)
                        return
            else:
                print("Book not found with given title!..")


    # Naya member add karta hai.
    def add_member(self, members):
        if len(members) == 0:
            member_id = "M001"

        else:
            last_id = members[-1].member_id
            number = int(last_id[1:]) + 1
            member_id = f"M{number:03d}"

        print("Member ID :",member_id)

        name = input("Enter member name: ")
        phone = input("Enter 10-digit member phone: +91-")

        valid = self.member_validation(name, phone)

        if valid:
            member = Members(member_id, name, phone)

            members.append(member)

            with open(MEMBER_FILE, "a") as f:
                f.write(f"{member.member_get_data()}")
                    
            print(f"Member ID '{member_id}' added successfully!..")

    # Saare members display karta hai.
    def show_members_func(self, members):
        print(temp_line)
        print("----------MEMBERS-LIST----------")
        print(temp_line)

        for member in members:
            member.show_members()

    # Member ko search karta hai.
    def search_member(self, members):
        id_to_search = input("Enter member id number to search: ")

        for member in members:
            if id_to_search == member.member_id:
                print("Member found..")
                member.show_members()
                return
        else:
            print("No member found with given details!..")

    # Member ki details update karta hai.
    def update_member_details(self, members):
        phone_to_update = input("Enter member id number to update: ")

        for member in members:
            if id_to_update == member.member_id:
                print("Member found..")
                member.show_members()

                print("\nEnter new details..")
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")

                valid = self.member_validation(new_name, new_phone)

                if valid:
                    member.name = new_name
                    member.phone = new_phone

                    self.save_members(members)

                    print("Member details updated successfully!..")
                    return

        else:
            print("Member not found with given details!..")

    # Member record delete karta hai.
    def delete_member(self, members):
        id_to_delete = input("Enter id number to delete member: +91-")

        for member in members:
            if id_to_delete == member.member_id:

                print("Member found..")
                member.show_members()
                
                confirm = input("Are you sure for delete this member(y/n): ").lower()

                if confirm == 'y':
                    members.remove(member)

                    print("Member deleted successfully!..")
                    self.save_members(members)
                    return

                else:
                    return

        else:
            print("Member not found with given details!..")

    # Member ko book issue karne ka process handle karta hai.
    def issue_book(self, books, members, issued_books):
        if len(issued_books) == 0:
            transaction_id = "T001"

        else:
            last_id = issued_books[-1].transaction_id
            number = int(last_id[1:]) + 1
            transaction_id = f"T{number:03d}"

        print(f"Transaction ID : {transaction_id}\n")


        member_id_to_input = input("Enter member ID: ")
        for member in members:
            if member_id_to_input == member.member_id:
                print("Member found..\n")

                book_id_to_input = input("Enter book ID: ")
                for book in books:
                    if book_id_to_input == book.book_id:
                        print("Book found..\n")

                        issue_date = datetime.now().date()
                        print(f"Issue Date : {issue_date}")
                        
                        try:
                            return_date_input = input("Enter return date (DD-MM-YY): ")
                            return_date = datetime.strptime(return_date_input, "%d-%m-%Y").date()

                        except ValueError:
                            print("Invalid return date!..")
                            return

                        if book.status == 'Unavailable':
                            print("No books are available!..")
                            return

                        valid = self.issued_book_validation(issue_date, return_date)

                        if valid:

                            issue_book = Issued_books(
                            transaction_id,
                            member_id_to_input, 
                            book_id_to_input, 
                            issue_date.strftime("%d-%m-%Y"), 
                            return_date.strftime("%d-%m-%Y")
                            )

                            issued_books.append(issue_book)

                            with open(ISSUE_BOOKS, "a") as f:
                                f.write(issue_book.issued_get_data())
                                
                            book.copies -= 1
                            if book.copies == 0:
                                book.status = "Unavailable"
                                
                            self.save_books(books)

                            print(f"'{book.title}' issued by '{member.name}'...")
                            return

                    else:
                        print("Book not found!..")
                        return

            else:
                print("Member not found!..")
                return

    # Saare issue records display karta hai.
    def show_issued_books_func(self, issued_books):
        print(temp_line)
        print("      ISSUED-BOOKS-LIST")   
        print(temp_line)

        for issued_book in issued_books:
            issued_book.show_issued_books()

    # Issue record ko search karta hai.
    def search_issued_book(self, issued_books):
        member_name_to_search_issued = input("Enter member name to search issued book: ").lower()

        for issued_book in issued_books:
            if member_name_to_search_issued == issued_book.member_name.lower():

                book_title_to_search_issued = input("Enter book title to search issued book: ").lower()

                if book_title_to_search_issued == issued_book.book_title.lower():
                    print("\nTransaction found..")
                    issued_book.show_issued_books()
                    return

                else:
                    print("Transaction not found!..")
                    return

        else:
            print("Transaction not found with given member name!..")

    # Issue record ki details update karta hai.
    def update_issued_book_details(self, books, members, issued_books):
        member_name_to_update_issued = input("Enter member name to update issued book: ").lower()

        for issued_book in issued_books:
            if member_name_to_update_issued == issued_book.member_name.lower():

                book_title_to_update_issued = input("Enter book title to update issued book: ").lower()

                if book_title_to_update_issued == issued_book.book_title.lower():
                    print("\nTransaction found..")
                    issued_book.show_issued_books()

                    print("\nEnter new details...")
                    new_member_name = input("Enter member name: ")

                    for issued_book in issued_books:
                        if new_member_name == issued_book.member_name:
                            print("Member found..\n")

                            new_book_title = input("Enter book title: ")
                            for book in books:
                                if new_book_title == issued_book.book_title:
                                    print("Book found..\n")
                        
                                    try:
                                        return_date_input = input("Enter return date (DD-MM-YY): ")
                                        new_return_date = datetime.strptime(return_date_input, "%d-%m-%Y").date()

                                    except ValueError:
                                        print("Invalid return date!..")
                                        return

                                    if book.status == 'Unavailable':
                                        print("This book is already issued, issue another book!..")
                                        return

                                    valid = self.issued_book_validation(issue_date, return_date)

                                    if valid:
                                        issued_book.member_name = new_member_name
                                        issued_book.book_title = new_book_title
                                        issued_book.return_date = new_return_date

                                        self.save_issued_books(issued_books)
                                        print("Transaction details updated successfully!..")

                                else:
                                    print("No book found with given title!..")

                    else:
                        print("No member found with given name!..")
                    return

                else:
                    print("Transaction not found!..")
                    return

        else:
            print("Transaction not found with given member name!..")

    # Issued book ko return karne ka process handle karta hai.
    def return_issued_book(self, books, issued_books):
        transaction_id_to_return = input("Enter transaction id to return book: ")

        for issued_book in issued_books:
            if transaction_id_to_return == issued_book.transaction_id:
                print("\nTransaction found!..")
                issued_book.show_issued_books()

                confirm = input("Are you sure to return this book (y/n): ").lower()
                if confirm == 'y':

                    issued_books.remove(issued_book)
                    self.save_issued_books(issued_books)

                    for book in books:
                        if issued_book.book_title == book.book_id:
                            book.copies += 1
                            print(f"'{book.title}' is returned successfully!..")
                            self.save_books(books)
                            return

                        else:
                            print("Book details not found in book file!..")
                            return

                else:
                    return

        else:
            print("No transaction found with given details!..")


    # Program ka main loop chalata hai.
    def run(self):
        while True:

            books        = self.read_books()
            members      = self.read_members()
            issued_books = self.read_issued_books()

            self.update_overdue_returns(books, issued_books)

            self.menu()
            choice = input("Enter choice: ")
            print("")

            if choice == "1":
                self.add_books(books)

            elif choice == "2":
                self.show_books_func(books)

            elif choice == "3":
                self.search_book(books)

            elif choice == "4":
                self.update_book_details(books)

            elif choice == "5":
                self.check_book_status(books)

            elif choice == "6":
                self.delete_book(books)

            elif choice == "7":
                self.add_member(members)

            elif choice == "8":
                self.show_members_func(members)

            elif choice == "9":
                self.search_member(members)

            elif choice == "10":
                self.update_member_details(members)

            elif choice == "11":
                self.delete_member(members)

            elif choice == "12":
                self.issue_book(books, members, issued_books)

            elif choice == "13":
                self.show_issued_books_func(issued_books)

            elif choice == "14":
                self.search_issued_book(issued_books)

            elif choice == "15":
                self.update_issued_book_details(books, members, issued_books)

            elif choice == "16":
                self.return_issued_book(books, issued_books)

            elif choice == "17":
                confirm = input("Are you sure for exit the program(y/n): ")
                if confirm == 'y':
                    print("Exiting...")
                    break

                else:
                    continue

            else:
                print("Invalid choice!..")
                continue

library = LibraryManagement()
library.run()
