#Name: Gil-li Ness Grota

list = [3,5,45,97,32,22,10,19,39,43]

new_list = [x for x in list if x % 2 == 0]
print(new_list)

list = [2,3.75,0.04,59.354,6,7.777,8,9]
new_list = [x for x in list if type(x) == int]
print(new_list)

for i in range(1000):
    temp = i
    for j in range(3):
        if temp % 10 == 3:
            print(i)
        temp //= 10

len_list = int(input("enter your list length: "))
list = []
sum = 0
for i in range(len_list):
    list.append(int(input("enter a number: ")))

for i in range(len_list - 1):
    if list[i] < list[i+1]:
        sum += list[i]

print(sum)

my_list = [543,777,10 ,22 ,543 ,10 ,777 ,22 ,543 ,21 ,21 ,777 ,10 ,81 ,777]
max_count = my_list.count(my_list[0])
max_num = my_list[0]

for i in range(len(my_list)):
    if max_count < my_list.count(my_list[i]):
        max_count = my_list.count(my_list[i])
        max_num = my_list[i]

print(max_count)
print(max_num)

dict = {}
for i in range(len(my_list)):
    if my_list[i] not in dict.keys():
        dict[my_list[i]] = 1
    else:
        dict[my_list[i]] += 1

max_count = 0

for val in dict.values():
    if max_count < val:
        max_count = val

for num, count in dict.items():
    if count == max_count:
        print(num)


first_list = ["father", "kayak", "madam", "Ronaldo", "Noa", "David"]
second_list = ["xavi", "Xman", "banana", "aoN", "madam", "kayak"]
combo_list = {}
index = 0
for i in range(len(first_list) * 2):
    if i % 2 == 0:
        combo_list[i] = first_list[index]
    else:
        combo_list[i] = second_list[index][::-1]
        index += 1

final_list = []
for i in range(len(combo_list)):
    if combo_list[i] not in final_list:
        final_list.append(combo_list[i])
print(final_list)

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


print(trush_product)

