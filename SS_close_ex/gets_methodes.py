def get_amount_of_days():
    days_amount = int(input("Enter the amount of days: "))
    while 7 <= days_amount:
        days_amount = int(input("Invalid days amount."
                                "Enter the amount of days: "))
    return days_amount

def get_hours_per_day():
    hours_amount = int(input("Enter the hours per day: "))
    while 9 <= hours_amount:
        hours_amount = int(input("Invalid hours amount. "
                                 "Enter the hours per day: "))
    return hours_amount


def get_data_for_lesson():
    return input("Enter the data for the lesson: ")


def get_lesson_from_string(lesson_string):
    data_list = lesson_string.split("_")
    return {"name": data_list[0],
            "duration": int(data_list[1]),
            "day": data_list[2],
            "hour": int(data_list[3])}
