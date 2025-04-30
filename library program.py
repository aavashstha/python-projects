#library book tracker


class Book():
    
    def __init__(self, name, is_available, book_code):
        self.name = name
        self.is_available = is_available
        self.book_code = book_code

def add_book(list_of_books, list_of_names, list_of_book_codes):
    while True:
        name = input("Enter the name of the book: ")
        if len(name) == 0:
            print("Please enter a valid name!!!")
            continue
        elif len(name) > 25:
            print("Enter a name within 25 characters!!!")
            continue
        elif name in list_of_names:
            print(f"There is already a book with same name '{name}'!!!")
            continue
        else:
            list_of_names.append(name)

        while True:
            book_code = input("Enter the book code no.: ")
            if not book_code.isdigit():
                print("***Enter a valid book code no.!!!")
                continue
            elif book_code in list_of_book_codes:
                print(f"There is already a book with same book code no. '{book_code}'!!!")
                continue
            else:
                list_of_book_codes.append(book_code)
                break

        while True:
            is_available = input("Is the book currently available? (Y or N): ").upper()
            if is_available not in ("Y", "N"):
                print("INVALID INPUT!")
                continue
            elif is_available == "Y":
                is_available = "available"
                break
            else:
                is_available = "is checked out"
                break

        book = Book(name, is_available, book_code)
        list_of_books.append(book)
        
        add_more = ""
        while add_more not in ("Y", "N"):
            add_more = input("Do you want to add more books? (Y or N): ").upper()
        if add_more == "Y":
            continue
        else:
            break

def remove_book(list_of_books, list_of_book_codes):
    if len(list_of_book_codes) > 1:
        while True:
            while True:
                remove_book_code = input("Enter the book code no. of the book to be removed: ")
                if not remove_book_code.isdigit():
                    print("***Enter a valid book code no.")
                    continue
                elif remove_book_code not in list_of_book_codes:
                    print(f"****There is no book with the code no. '{remove_book_code}'")
                    continue
                else:
                    break
            
            for book in list_of_books:
                if book.book_code == remove_book_code:
                    list_of_books.remove(book)

            remove_more = ""
            while remove_more not in ("Y", "N"):
                remove_more = input("Do you want to remove more books? (Y or N): ").upper()
            if remove_more == "Y":
                continue
            else:
                break
    else:
        print("There are no books in the library!!!")

def search_book(list_of_books, list_of_book_codes):
    if len(list_of_book_codes) > 1:
        while True:
            search_more = ""
            search_book_code = input("Enter the book code no. of the book you want to view: ")
            if not search_book_code.isdigit():
                print("***Enter a valid book code no.")
                continue
            elif search_book_code not in list_of_book_codes:
                print(f"****There is no book with the code no. '{search_book_code}'")
                continue
            else:
                for book in list_of_books:
                    if book.book_code == search_book_code:
                        print("*******************************************************")
                        print("          NAME           |  BOOK CODE  |  AVAILABILITY ")
                        print(f"{book.name:^25}|{book.book_code:^13}|{book.is_available:^15}")
                        print("*******************************************************")
                        break

            while search_more not in ("Y", "N"):
                search_more = input("Do you want to search another book as well? (Y or N): ").upper()
            if search_more == "Y":
                continue
            else:
                break
    elif len(list_of_book_codes) <= 0:
        print("There are no books in the library!!!")
    else:
        print("There's only one book currently, so please select the option 4. Display all the books")
        


        
def display_books(list_of_books):
    if len(list_of_books) > 1:
        print()
        print("*******************************************************")
        print("          NAME           |  BOOK CODE  |  AVAILABILITY ")
        for book in list_of_books:
            print(f"{book.name:^25}|{book.book_code:^13}|{book.is_available:^15}")
        print("*******************************************************")
        print()
    else:
        print("There are no books in the library!!!")


def main():
    list_of_books = []
    list_of_names = []
    list_of_book_codes = []
    is_running = True

    print()
    print("********** LIBRARY PROGRAM **********")

    while is_running:
        print()
        print("1. Add books")
        print("2. Remove books")
        print("3. Search for a book")
        print("4. Display all the books")
        print("5. Quit")
        print()

        while True:
            library_func = input("Enter a function to perform (1 - 5): ")
            if library_func not in ("1", "2", "3", "4", "5"):
                print("***Enter a valid number!!!!")
            else:
                break
        
        print()
        if library_func == "1":
            add_book(list_of_books, list_of_names, list_of_book_codes)
        elif library_func == "2":
            remove_book(list_of_books, list_of_book_codes)
        elif library_func == "3":
            search_book(list_of_books, list_of_book_codes)
        elif library_func == "4":
            display_books(list_of_books)
        else:
            print("BYE!👋")
            is_running = False
        
if __name__ == '__main__':
    main()