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

there_is_free_day = False
free_day_teachers_dict = {}

for i in range(5):
    free_day = input(f"Does Teacher{i + 1} have a disclaimer? If so on which day?")
    if(free_day != ""):
        there_is_free_day = True
        match i:
            case 0:
                free_day_teachers_dict[1] = free_day
                t1.pop(free_day)
            case 1:
                free_day_teachers_dict[2] = free_day
                t2.pop(free_day)
            case 2:
                free_day_teachers_dict[3] = free_day
                t3.pop(free_day)
            case 3:
                free_day_teachers_dict[4] = free_day
                t4.pop(free_day)
            case 4:
                free_day_teachers_dict[5] = free_day
                t5.pop(free_day)


t1 = creat_scheduled(t1, timeslots)
t2 = creat_scheduled(t2, timeslots)
t3 = creat_scheduled(t3, timeslots)
t4 = creat_scheduled(t4, timeslots)
t5 = creat_scheduled(t5, timeslots)

teachers_list = [t1, t2, t3, t4, t5]
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

if(there_is_free_day):
    print("Unavailable Slots:")
    for teacher, day in free_day_teachers_dict.items():
        volunteer = input(f"Teacher{teacher} can't attend to the slot on {day}. Is there any teacher that can take this slot? (If no one volunteers, enter the word \'None\'): >?")
        if(volunteer == "None"):
            print()
        else:
            teacher_index = int(volunteer[7:])
            if day not in teachers_list[teacher_index - 1].keys():
                volunteer = input("Teacher3 cannot take this slot. Please choose another teacher. Is there any teacher that can take this slot? (If no one volunteers, enter the word \'None\'): >?")
                