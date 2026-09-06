import ss_Constanctes

def init_schedule(amount_of_days, hours_per_day):
    return [[ss_Constanctes.EMPTY_LESSON for hour in range(hours_per_day)] for day in
            range(amount_of_days)]


def does_lesson_fit(schedule, lesson):
    current_day = schedule[ss_Constanctes.DAYS_DICT[lesson["day"]]]

    for hour in range(lesson["duration"]):
        curr_hour_index = (lesson["hour"] - ss_Constanctes.STARTING_HOUR) + hour
        if curr_hour_index >= len(current_day) or \
                current_day[curr_hour_index] != "Free":
            return False

    return True


def insert_lesson(schedule, lesson):
    current_day = schedule[ss_Constanctes.DAYS_DICT[lesson["day"]]]

    for hour in range(lesson["duration"]):
        curr_hour_index = (lesson["hour"] - ss_Constanctes.STARTING_HOUR) + hour
        current_day[curr_hour_index] = lesson["name"]


def insert_lessons_by_request(schedule, lessons):
    rejected_lessons = []

    for lesson in lessons:
        if lesson["hour"] + lesson["duration"] <=  ss_Constanctes.STARTING_HOUR + len(schedule[0]) \
                and does_lesson_fit(schedule, lesson):
            insert_lesson(schedule, lesson)
        else:
            rejected_lessons.append(lesson)

    return rejected_lessons

def find_lesson_location(schedule, lesson):
    new_lesson = lesson.copy()
    end_of_day_hour = len(schedule[0]) + ss_Constanctes.STARTING_HOUR

    for day_index in range(len(schedule)):
        new_lesson["day"] = ss_Constanctes.DAY_LIST[day_index]
        for hour in range(ss_Constanctes.STARTING_HOUR, end_of_day_hour):
            new_lesson["hour"] = hour
            if does_lesson_fit(schedule, new_lesson):
                return {"day": new_lesson["day"],
                        "hour": new_lesson["hour"]}

    return {}

def insert_rejected_lessons(schedule, rejected_lessons):
    for lesson in rejected_lessons:
        lesson_location = find_lesson_location(schedule, lesson)
        if lesson_location:
            lesson["day"] = lesson_location["day"]
            lesson["hour"] = lesson_location["hour"]
            insert_lesson(schedule, lesson)
        else:
           return False
    return True
