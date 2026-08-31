#332011865 Gil-li Ness Grota
from shlex import split  #1.
 #setting data
 #2.
 #input data from user
 #insert into list
 #3.
 #insert into schedule
 #4.
 #check if possible to put unplaced lessons into schedule
 #if there is no any left place, find the closest day with according hours
 #all left unplaced lessons, print Error
# consts

STARTING_HOUR = 8
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
DAYS_DICT = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5}


def get_amount_of_days():
    days_amount = int(input("Enter the amount of days:"))
    while 7 <= days_amount:
        days_amount = int(input("Invalid days amount."
                                "Enter the amount of days:"))
    return days_amount


def get_hours_per_day():
    hours_amount = int(input("Enter the hours per day:"))
    while 9 <= hours_amount:
        hours_amount = int(input("Invalid hours amount. "
                                 "Enter the hours per day:"))
    return hours_amount


amount_of_days = get_amount_of_days()
hours_per_day = get_hours_per_day()
schedule = []

# Initializing the schedule
def init_schedule(days_amount, hours_for_day):
    global schedule
    schedule = []
    for day in range(days_amount):
        schedule.append([])
        for hours in range(hours_for_day):
            schedule[day].append("Free")

# The data is inserted:
# [name of class]_[how many hours the class]_[day]_[starting hour]
def get_inserted_schedule():
    global schedule, amount_of_days
    schedule_lst = []
    lesson = input("Enter the data for the lesson:")
    while "done" != lesson:
        schedule_lst.append(lesson)
        if not is_lesson_valid(lesson):
            print("Invalid lesson, please try again.")
            while is_lesson_valid(lesson):
                lesson = input("Enter the data for the lesson:")
        lesson = input("Enter the data for the lesson:")
    if not schedule_lst:
        print_schedule(amount_of_days, schedule)
    return schedule_lst

def get_lesson(lesson):
    split_lesson = lesson.split("_")
    return split_lesson[0]

def get_how_many_hours_lesson(lesson):
    split_lesson = lesson.split("_")
    return int(split_lesson[1])

def get_day_of_the_lesson_in_number(lesson):
    split_lesson = lesson.split("_")
    return DAYS_DICT.get(split_lesson[2])

def lesson_start_time(lesson):
    split_lesson = lesson.split("_")
    return int(split_lesson[3])

def is_lesson_valid(lesson):
    global hours_per_day
    if STARTING_HOUR + hours_per_day <= int(lesson_start_time(lesson)):
        return False
    return True

# Initial insertion of lessons
def insert_lesson_into_schedule_and_return_invalid_lessons(lesson_lst):
    global schedule, hours_per_day, amount_of_days
    invalid_lesson = []
    for lesson in range(len(lesson_lst)):
        for hour in range(get_how_many_hours_lesson(lesson_lst[lesson]) + 1):#+1
            if len(schedule[get_day_of_the_lesson_in_number(lesson_lst[lesson])]) < len(lesson_lst) and hour < get_how_many_hours_lesson(lesson_lst[lesson]):
                if schedule[get_day_of_the_lesson_in_number(lesson_lst[lesson])][hour] != "Free":
                    if lesson_lst[lesson] not in invalid_lesson:
                        invalid_lesson.append(lesson_lst[lesson])
        if lesson_lst[lesson] not in invalid_lesson:
            for hour in range(get_how_many_hours_lesson(lesson_lst[lesson])):
                try:
                    schedule[get_day_of_the_lesson_in_number(lesson_lst[lesson])][lesson_start_time(lesson_lst[lesson]) - 8 + hour] = get_lesson(lesson_lst[lesson])
                finally:
                    pass
    if not invalid_lesson:
        print_schedule(amount_of_days, schedule)
    return invalid_lesson

# Final insertion of lessons
def insert_invalid_lesson(invalid_lessons):
    global schedule, hours_per_day, amount_of_days
    is_proggram_failed = False
    copy_of_schedule = schedule.copy()
    for invalid_lesson in invalid_lessons:
        if is_invalid_lesson_can_be_added(copy_of_schedule, get_how_many_hours_lesson(invalid_lesson), invalid_lesson):
            print("The schedule's creation failed.")
            is_proggram_failed = True
    if not is_proggram_failed:
        print_schedule(amount_of_days, copy_of_schedule)


def is_invalid_lesson_can_be_added(copy_schedule, lesson_hours,lesson):
    count_times_that_added = 0
    for day in range(len(copy_schedule)):
        for hour in range(len(copy_schedule[day])):
            if copy_schedule[day][hour] == "Free":
                try:
                    if copy_schedule[day][hour] != "Free":
                        return False
                    else:
                        if count_times_that_added < lesson_hours:
                            copy_schedule[day][hour] = get_lesson(lesson)
                            count_times_that_added += 1
                finally:
                    pass
            elif day == len(copy_schedule) - 1 and hour == len(copy_schedule[day]) - 1:
                return False
    return True


#print schedule
def print_schedule(days_amount, schedule):
    for day in range(amount_of_days):
        print(DAY_LIST[day] + ": " + str(schedule[day]))


if __name__ == "__main__":
    init_schedule(amount_of_days, hours_per_day)
    inserted_lessons_lst = get_inserted_schedule()
    invalid_lesson_list = insert_lesson_into_schedule_and_return_invalid_lessons(inserted_lessons_lst)
    insert_invalid_lesson(invalid_lesson_list)

