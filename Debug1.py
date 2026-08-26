print("Welcome to the meal calculator!")
print("What is the average price of a dish?")
dish_price = int(input())
print("How many dishes shall we have?")
dishes = int(input())
print("How many families are attending?")
families = int(input())

total_price = 0
family_sum = 0

for i in range(1, families + 1):
    print("family", i, ":")
    family_sum = 0
    for j in range(1, dishes + 1):
        print("How much of dish", j, "did family", i, "ordered?")
        family_sum += dish_price * int(input())

    print("family", i, "will cost a total of", family_sum)
    total_price += family_sum

print("the total price of the dinner will be", total_price)