#Name: Gil-li Ness Grota - 332011865

lst = ['a','b','c','da']
def add_book():
    global lst

    new_book = input("please enter a book name: ")
    if new_book not in lst:
        lst.append(new_book)
    else:
        print("book already exists")

def remove_book():
    global lst
    remove_book = input("please enter a book name: ")
    if remove_book in lst:
        lst.remove(remove_book)
    else:
        print("book already taken")

def look_for():
    global lst
    books_that_contain_the_word = []
    look_for = input("please enter a book name: ")
    for book in lst:
        if look_for.lower() in book.lower():
            books_that_contain_the_word.append(book)
    return books_that_contain_the_word

def print_books():
    global lst
    [print(f"{i + 1}. {book}") for i, book in enumerate(lst)]

print("welcome to the library")
choice = 0
while choice != 5:
    print("Add - 1")
    print("Remove - 2")
    print("Search - 3")
    print("Print All - 4")
    print("Exit - 5")

    choice = int(input("Enter your choice: "))
    match(choice):
        case 1:
            add_book()
        case 2:
            remove_book()
        case 3:
            print(look_for())
        case 4:
            print_books()
        case 5:
            print("goodbye world :(")