#Name: Gil-li Ness Grota
import random

def creat_scheduled(t, time):
    copyTime = time.copy()
    for day, time in t.items():
        t[day] = random.choice(copyTime)
        copyTime.remove(t[day])
    return t


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
timeslots = ["8:00 - 9:30", "10:00 - 11:30", "12:00 - 13:30","14:00 - 15:30", "16:00 - 17:30"]

t1 = {"Sunday" : "",
      "Monday" : "",
      "Tuesday" : "",
      "Wednesday" :  "",
      "Thursday" : ""}
t2 = t1.copy()
t3 = t1.copy()
t4 = t1.copy()
t5 = t1.copy()

for i in range(5):
    free_day = input(f"Does Teacher{i + 1} have a disclaimer? If so on which day?")
    if(free_day != ""):
        match i:
            case 0:
                t1.pop(free_day)
            case 1:
                t2.pop(free_day)
            case 2:
                t3.pop(free_day)
            case 3:
                t4.pop(free_day)
            case 4:
                t5.pop(free_day)


t1 = creat_scheduled(t1, timeslots)
t2 = creat_scheduled(t2, timeslots)
t3 = creat_scheduled(t3, timeslots)
t4 = creat_scheduled(t4, timeslots)
t5 = creat_scheduled(t5, timeslots)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)


