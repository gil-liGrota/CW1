
#Name: Gil-li Ness Grota
import random

my_list = ["orange", "banana", "apple", "kiwi"]
index = int(input("Enter an index: "))
my_list.insert(index, "pineapple")
print(my_list)

my_list = []

value = input("Enter a value: ")

while value != "stop":
    my_list.append(value)
    value = input("Enter another value: ")

print(my_list)

my_list = ["o" , "hat" , "aba" , "1221" , "umbrella" , "pickup" , "22.3.22"]
conter = 0

for string in my_list:
    if len(string) > 1:
        if(string[0] == string[len(string) - 1]):
            conter += 1
print(conter)

list = [3,5,45,97,32,22,10,19,39,43]

new_list = [x for x in list if x % 2 == 0]
print(new_list)

list = [5,4,8,1]
copylist = list
new_list = []
for i in range(0,len(list)):
    random_number = random.randint(0,len(copylist) - 1)
    new_list.append(copylist[random_number])
    copylist.remove(copylist[random_number])

print(new_list)
dict = {"bob" : 35, "tom" : 17, "lana" : 70}

dict["joe"] = 19
print(dict["joe"])
print(len(dict))
print(dict.keys())
dict.pop("joe")
print(dict)
key_list = dict.keys()
for key in key_list:
    if key == "jack":
        print("True")
        break
age_sum = 0
value_list = dict.values()
for value in value_list:
    age_sum += value
print(age_sum / len(value_list))

for key in dict:
    if dict[key] >= 18:
        print(key)
dict.clear()