import ss_init_schedule
import gets_methodes
import ss_valid_lessones
import ss_prints

def main():
    amount_of_days = gets_methodes.get_amount_of_days()
    hours_per_day = gets_methodes.get_hours_per_day()

    schedule = ss_init_schedule.init_schedule(amount_of_days, hours_per_day)
    lessons = ss_valid_lessones.get_lessons_data(amount_of_days, hours_per_day)
    rejected_lessons = ss_init_schedule.insert_lessons_by_request(schedule, lessons)

    was_insertions_successful = ss_init_schedule.insert_rejected_lessons(schedule,
                                                        rejected_lessons)
    if not was_insertions_successful:
        ss_prints.print_creation_failed()
    else:
        ss_prints.print_schedule(schedule, amount_of_days)


main()