#Name: Gil-li Ness Grota
#
# def no_duplicates(lst):
#     no_duplicates = []
#     for item in lst:
#         if item not in no_duplicates:
#             no_duplicates.append(item)
#     return no_duplicates
#
# lst = [4,9,4,5,8,8,4,1]
# print(no_duplicates(lst))
#
# SECRET_WORD_LIST = "lists"
# WORD_LEN = len(SECRET_WORD_LIST)
# is_finished = False
#
# def guessing_absorption():
#     guess_input = input("Enter guess: ")
#     while len(guess_input) != WORD_LEN:
#         print("Your guess has", len(guess_input), "letters and should have", WORD_LEN)
#         print()
#         guess_input = input("Enter guess: ")
#     return guess_input
#
#
# def sort_letters_by_place(guess_input):
#     for index in range(len(guess_input)):
#         letter = guess_input[index]
#         if SECRET_WORD_LIST[index] == letter:
#             green_list.append(letter)
#         elif letter in SECRET_WORD_LIST:
#             orange_list.append(letter)
#         else:
#             gray_list.append(letter)
#
# def win_or_lose(is_finished_input):
#     if len(green_list) == WORD_LEN:
#         is_finished_input = True
#     else:
#         print("Green letters: ", green_list)
#         print("Orange letters: ", orange_list)
#         print("Gray letters: ", gray_list)
#
# while not is_finished:
#     print()
#     guess = guessing_absorption()
#
#     green_list = []
#     orange_list = []
#     gray_list = []
#
#     sort_letters_by_place(guess)
#     win_or_lose(is_finished)
#
# print("Congratulations!")

def find_size(box, cabinet ):
    in_size = True
    cab_cubic_cc = 1
    box_cubic_cc = 1

    for i in range (3):
        cab_cubic_cc *= cabinet[i]
        box_cubic_cc *= box[i]
        if box[i] < cabinet[i]:
            return False
    return cab_cubic_cc <= box_cubic_cc

def sort_boxes(boxes, cabinets):
    fit_boxes = []
    for cabinet in range(len(cabinets)):
        for box in range(len(boxes)):
            if find_size(boxes[box], cabinets[cabinet]):
                fit_boxes.append(box)
    return fit_boxes



box_size = [(130, 40, 30), (140, 100, 100), (180, 45, 130)]
cabinet_size = [(120, 50, 60), (50, 40, 90)]
print(sort_boxes(box_size, cabinet_size))