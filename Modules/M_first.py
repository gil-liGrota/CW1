import M_second
# The function print the menu
ADD = 1
REMOVE = 2
SEARCH = 3
PRINT_ALL = 4
EXIT = 5

def print_menu():
    print(str(ADD) + " - Add")
    print(str(REMOVE) + " - Remove")
    print(str(SEARCH) + " - Search")
    print(str(PRINT_ALL) + " - Print all")
    print(str(EXIT) + " - Exit")


def manage_library():
    my_library = []
    print("welcome to the library")
    print_menu()
    user_choice = int(input("Enter choice number"))

    while user_choice != EXIT:
        if user_choice == PRINT_ALL:
            M_second.print_book_list(my_library)
        else:
            book_name = input("Enter book name")
            if user_choice == ADD:
                M_second.add_book(my_library, book_name)
            elif user_choice == REMOVE:
                is_found = M_second.remove_book(my_library, book_name)
                if not is_found:
                    print("book does not exist")
            elif user_choice == SEARCH:
                result_list = M_second.search_name(my_library, book_name)
                if len(result_list) == 0:
                    print("book does not found")
                else:
                    M_second.print_book_list(result_list)
            else:
                print("choice doesn't found, please try again")

        print_menu()
        user_choice = int(input("Enter choice number"))

