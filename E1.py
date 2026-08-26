#Name: Gil-li Ness Grota
import time
import random
import math

sec = float(input("Enter a seconds: "))

print("start")
time.sleep(sec)
print("end")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

val1 = num1 / num2
val2 = math.pow(num1, num2)

sec = random.uniform(val1, val2)
print("start")
time.sleep(sec)
print("end")