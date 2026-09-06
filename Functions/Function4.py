bag_dict = {"simple" : 20,
            "With dedication" : 30,
            "Noa Kila Keep IT Reala " : 40,}
number_of_countries = int(input("Enter the amount of countries: "))
for i in range(number_of_countries):
    budget = int(input(f"Enter the budget for country number #{i}: "))
    amount = int(input(f"Enter the amount of people at show number: "))
    sum_of_amount = amount
    while amount > 0:
        amount = int(input(f"Enter the amount of people at show number: "))
        sum_of_amount += amount
    print(f"For country {i + 1}:")
    print(f"we can afford")