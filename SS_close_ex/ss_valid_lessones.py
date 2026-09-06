import ss_Constanctes
import gets_methodes

def check_if_lesson_valid(new_lesson, days_in_sched, hours_in_sched):
    if ss_Constanctes.STARTING_HOUR <= new_lesson["hour"] < ss_Constanctes.STARTING_HOUR + hours_in_sched  \
            and 0 < new_lesson["duration"] <= hours_in_sched \
            and new_lesson["day"] in ss_Constanctes.DAY_LIST[:days_in_sched]:
        return True

    return False


def get_lessons_data(days_in_sched, hours_in_sched):
    lessons = []
    data_for_current_lesson = gets_methodes.get_data_for_lesson()

    while data_for_current_lesson != ss_Constanctes.EXIT_CODE:
        new_lesson = gets_methodes.get_lesson_from_string(data_for_current_lesson)
        if check_if_lesson_valid(new_lesson, days_in_sched, hours_in_sched):
            lessons.append(new_lesson)

        else:
            print("Invalid lesson info, Please try again.")

        data_for_current_lesson = gets_methodes.get_data_for_lesson()

    return lessons
