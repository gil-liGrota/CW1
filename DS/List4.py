#Name: Gil-li Ness Grota
import random

def removing_a_product_from_the_cart(shopping_dict):
    current_money = 0
    for price in shopping_dict.values():
        current_money += price

    over_value_prices = {}
    for product, price in shopping_dict.items():
        diff = current_money - price
        if diff < 50:
            over_value_prices[product] = price

    min_price = 50
    trush_product = ""
    for product, price in over_value_prices.items():
        if 50 - (current_money - price) < min_price:
            min_price = 50 - (current_money - price)
            trush_product = product
    return trush_product

shopping_list = {"eggs", "milk", "chocolate", "banana" ,"salt" ,"chips"}
prices = {
    "eggs": 20.2,
    "yogurt": 5,
    "cheese": 3,
    "milk": 6.75,
    "chocolate": 15.5,
    "cornflakes":25.3,
    "banana":2,
    "apple":3.1,
    "salt":1.8,
    "chips":13}

shopping_dict = {}

for item in shopping_list:
    if item not in shopping_dict.keys():
        shopping_dict[item] = prices[item]


print(removing_a_product_from_the_cart(shopping_dict))

first_product = random.choice(list(shopping_dict.keys()))
list_without_product = shopping_dict.copy().pop(first_product)
second_product = random.choice(list(shopping_dict.keys()))
discount_in_flot = random.randrange(0, 1)

print(f"you have to buy: {first_product} to get discount on: {second_product}")
print(f"befor discount: {shopping_dict[second_product]} after discount: {discount_in_flot * shopping_dict[second_product]}")


if(first_product in shopping_dict.keys()):
    if(second_product in shopping_dict.keys()):
        shopping_dict[second_product] *= discount_in_flot

copy_of_shopping_dict = shopping_dict.copy()
copy_of_shopping_dict[second_product] += copy_of_shopping_dict[first_product]
copy_of_shopping_dict.pop(first_product)


product_that_need_to_be_removed = removing_a_product_from_the_cart(copy_of_shopping_dict)
shopping_dict.pop(product_that_need_to_be_removed)

print(removing_a_product_from_the_cart(copy_of_shopping_dict))
print(shopping_dict)