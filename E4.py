import datetime

print("Enter a future date: ")
future_day = int(input("day: "))
future_month = int(input("month: "))
future_year = int(input("year: "))

current_day = datetime.datetime.today().day
current_month = datetime.datetime.today().month
current_year = datetime.datetime.today().year

delta_day = future_day - current_day
delta_month = future_month - current_month
delta_year = future_year - current_year

print(delta_day + delta_month * 30 + delta_year * 365)