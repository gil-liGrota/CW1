#Name: Gil-li Ness Grota - 332011865

import random

word_list = ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange', 'potato', 'august', 'better', 'breath', 'market', 'repair', 'school','colony', 'online', 'carrot', 'rabbit', 'doctor']

FIRST_PLAYER_NAME = input("Please enter your name: ")
FIRST_PLAYER_WORD = random.choice(word_list)
first_player_word_guess = ['_' for c in FIRST_PLAYER_WORD]

SECOND_PLAYER_NAME = input("Please enter your name: ")
SECOND_PLAYER_WORD = random.choice(word_list)
second_player_word_guess = ['_' for c in SECOND_PLAYER_WORD]

is_win = False
def check_guess(guess, word, list):
    if guess in word:
        for char in range(len(word)):
            if guess == word[char]:
                list[char] = guess
        print(f"the letter {guess} is in the word {list}")
    else:
        print(f"The letter {guess} is not in the word:")

def guess_player(player_name):
    global first_player_word_guess, second_player_word_guess

    guess = input(f"Hello {player_name}, please guess your next letter: ______")
    if player_name == FIRST_PLAYER_NAME:
        check_guess(guess, FIRST_PLAYER_WORD, first_player_word_guess)
    else:
        check_guess(guess, SECOND_PLAYER_NAME, second_player_word_guess)

while not is_win:
    if '_' in first_player_word_guess:
        guess_player(FIRST_PLAYER_NAME)
    else:
        is_win = True
    if is_win: break
    if '_' in second_player_word_guess:
        guess_player(SECOND_PLAYER_NAME)
    else:
        is_win = True

