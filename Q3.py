#Name: Gil-li Ness Grota
import datetime

date = datetime.datetime

books = 18
notebooks = 23
pens = 9

buy_books = int(input("How many books do you want to buy? "))
if books - buy_books < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {books} books")
    buy_books = books
    books = 0
else:
    books -= buy_books


buy_notebooks = int(input("How many notebooks do you want to buy? "))
if notebooks - buy_notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {notebooks} notebooks")
    buy_notebooks = notebooks
    notebooks = 0
else:
    notebooks -= buy_notebooks

buy_pens = int(input("How many pens do you want to buy? "))
if pens - notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {pens} pens")
    buy_pens = pens
    pens = 0
else:
    pens -= buy_pens
print(f"current stock: books: {books}, notebooks: {notebooks}, pens: {pens}")
print(f"purchase date: {date.now().date()}")


books += 4
notebooks += 2
pens += 5



#first
print(f"current stock: books: {books}, notebooks: {notebooks}, pens: {pens}")

buy_books = int(input("How many books do you want to buy? "))
if books - buy_books < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {books} books")
    buy_books = books
    books = 0
else:
    books -= buy_books


buy_notebooks = int(input("How many notebooks do you want to buy? "))
if notebooks - buy_notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {notebooks} notebooks")
    buy_notebooks = notebooks
    notebooks = 0
else:
    notebooks -= buy_notebooks

buy_pens = int(input("How many pens do you want to buy? "))
if pens - notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {pens} pens")
    buy_pens = pens
    pens = 0
else:
    pens -= buy_pens

first_day = int(input("plese enter the day of purchase (1 - 31): "))
first_month = int(input("plese enter the month of purchase (1 - 12): "))
first_year = int(input("plese enter the year of purchase: "))


#second

buy_books = int(input("How many books do you want to buy? "))
if books - buy_books < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {books} books")
    buy_books = books
    books = 0
else:
    books -= buy_books


buy_notebooks = int(input("How many notebooks do you want to buy? "))
if notebooks - buy_notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {notebooks} notebooks")
    buy_notebooks = notebooks
    notebooks = 0
else:
    notebooks -= buy_notebooks

buy_pens = int(input("How many pens do you want to buy? "))
if pens - notebooks < 0:
    print(f"Sorry, those quantities are out of stock, you may buy {pens} pens")
    buy_pens = pens
    pens = 0
else:
    pens -= buy_pens

second_day = int(input("plese enter the day of purchase (1 - 31): "))
second_month = int(input("plese enter the month of purchase (1 - 12): "))
second_year = int(input("plese enter the year of purchase: "))

if first_year > second_year:
    print("second purchase was made first")
elif second_year > first_year:
    print("first purchase was made second")
else:
    if first_month > second_month:
        print("second purchase was made second")
    elif second_month > first_month:
        print("first purchase was made first")
    else:
        if first_day > second_day:
            print("second purchase was made second")
        elif second_day > first_day:
            print("first purchase was made first")
        else:
            print("something went wrong")

print(f"current stock: books: {books}, notebooks: {notebooks}, pens: {pens}")
