#Name: Gil-li Ness Grota - 332011865

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def print_matrix(lst):
    for row in lst:
        for col in row:
            print(col, end=" ")
        print()

print_matrix(matrix)

def sum_matrix(lst):
    sum = 0
    for row in lst:
        for col in row:
            sum += col
    return sum

print(sum_matrix(matrix))

def calc_diagonal_sum(lst):
    sum = 0
    for row in range(len(lst)):
        for col in range(len(lst)):
            if row == col:
                sum += lst[row][col]
    return sum

print(calc_diagonal_sum(matrix))

special_guests = ["Ofir", "Bar", "Neta"]
family = ["Aviram", "Ohad"]
friends = ["Moti", "Liron", "Roni"]

all_guests = [special_guests, family, friends]
print_matrix(all_guests)

vip_guests = input("Enter the vip guest name: ")
for row in all_guests:
    if vip_guests in row:
        for col in row:
            if vip_guests == col:
                row.remove(vip_guests)
print_matrix(all_guests)

new_friends = input("Enter the new friends name: ")
for row in all_guests:
    if new_friends not in row and "Moti" in row:
        row.append(new_friends)
print_matrix(all_guests)



matrix_length = int(input("enter the matrix length: "))
matrix = []
for row in range(matrix_length):
    matrix.append([])
    for col in range(matrix_length):
        matrix[row].append(row - col if (row - col) > 0 else 0 )

print_matrix(matrix)

WORKING_SCREEN = "work"
FAULTY_SCREEN = "problem"
tv = [
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
]

broken_screens = []

for row in range (len(tv)):
    for col in range(len(tv[row])):
        if tv[row][col] == "problem":
            broken_screens.append((row, col))


print(broken_screens)

def print_bord():
    global board
    for row in board:
        print(row)



def get_queen_moves(queen_row_index: int, queen_col_index: int, matrix:list[list]) -> None:
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[row_index])):
            if (row_index == queen_row_index or column_index == queen_col_index) or (row_index - queen_row_index == column_index - queen_col_index) or (row_index - queen_row_index == queen_col_index - column_index):
                matrix[row_index][column_index] = 1

    matrix[queen_row_index][queen_col_index] = "x"
    return matrix

matrix = [[0 for _ in range(8)] for _ in range(8)]
print_matrix(get_queen_moves(2, 5, matrix))
def get_row():
    input_row = int(input("Enter the row number: "))
    while input_row < 0 or input_row >= len(board):
        input_row = int(input("out of bord range,Enter the row number: "))
    return input_row

def get_column():
    input_column = int(input("Enter the column number: "))
    while input_column < 0 or input_column >= len(board):
        input_column = int(input("out of bord range,Enter the column number: "))
    return input_column

def count_until_hit_submarine():
    global board
    count_trys = 0
    input_row = get_row()

    input_column = get_column()

    while board[input_row - 1][input_column - 1] == 'O':
        print('you miss')
        print('LOSERRRRR try again')
        count_trys += 1
        input_row = get_row()
        input_column = get_column()

    board[input_row - 1][input_column - 1] = 's'

    return count_trys

SUBMARINE = 'X'
EMPTY = 'O'
board = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY]
]

print_matrix(board)
print(count_until_hit_submarine())
