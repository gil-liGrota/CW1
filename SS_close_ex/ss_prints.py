import ss_Constanctes

def print_schedule(schedule, amount_of_days):
    for day_index in range(amount_of_days):
        print(ss_Constanctes.DAY_LIST[day_index] + ": ")
        for hour in schedule[day_index]:
            print(hour, end=" ")
        print()


def print_creation_failed():
    print("The schedule's creation failed")
