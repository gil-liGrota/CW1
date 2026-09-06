#Name: Gil-li Ness Grota
#without double characters
from colorama import Fore,Style

WORD = "while"
WORD_LEN = len(WORD)
user_guess = ""
win = False

green_list = []
orange_list = []
grey_list = []

double_chare =  False

print("WELCAME TO WORDLE")

for i in range(6):
    user_guess =  input(f"enter your {i + 1} guess: ").lower().strip()
    double_chare = False
    green_list = []
    orange_list = []
    grey_list = []

    for char in user_guess:
        if char == " " or type(char) != str:
            print("please enter 5 characters")
            user_guess = input(f"enter your {i + 1} guess: ").lower().strip()

    if len(user_guess) != WORD_LEN:
        print("please enter 5 characters")
        user_guess = input(f"enter your {i + 1} guess: ").lower().strip()


    if user_guess == WORD:
        print(Fore.GREEN + WORD)
        print(Fore.GREEN + 'Congratulations! You were right')
        win = True
        break

    for char in user_guess:
        if user_guess.count(char) > 1:
            double_chare = True
            break

    if not double_chare:
        for i in range(WORD_LEN):
            is_colored = False
            for j in range(WORD_LEN):
                if user_guess[i] == WORD[j]:
                    if j == i:
                        green_list.append(user_guess[i])
                        is_colored = True
                    elif i != j:
                        orange_list.append(user_guess[i])
                        is_colored = True
                if j == 4 and not is_colored:
                    grey_list.append(user_guess[i])

    else:
        for char in user_guess:
            if user_guess.count(char) == 1:
                for i in range(WORD_LEN):
                    is_colored = False
                    for j in range(WORD_LEN):
                        if user_guess[i] == WORD[j]:
                            if j == i:
                                green_list.append(user_guess[i])
                                is_colored = True
                            elif i != j:
                                orange_list.append(user_guess[i])
                                is_colored = True
                        if j == 4 and not is_colored:
                            grey_list.append(user_guess[i])
            #else:


    for i in range(WORD_LEN):
        if user_guess[i] in green_list:
            print(Fore.GREEN + user_guess[i], end='')
        if user_guess[i] in orange_list:
            print(Fore.YELLOW + user_guess[i], end='')
        if user_guess[i] in grey_list:
            print(Fore.BLACK + user_guess[i], end='')
    print(Style.RESET_ALL)

if not win:
    print(Fore.RED + 'Next time you\'ll have better luck.')