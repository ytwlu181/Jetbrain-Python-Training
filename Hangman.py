# Write your code here
import random


def update_display(answer, guess_set):
    _display = ""
    for _char in answer:
        if _char not in guess_set:
            _char = '-'
        _display += _char
    return _display


def check_end():
    if life < 8 and display == answer:
        print('\n', answer)
        print("You guessed the word!")
        print("You survived!")
        return True
    if life >= 8 and display != answer:
        print("You are hanged!")
        return True


def game_update():
    life_update = 0
    if guess not in answer:
        print("No such letter in the word")
        wrong_guess_set.add(guess)
        life_update = 1
    else:
        guess_set.add(guess)
    _display = update_display(answer, guess_set)
    return [life_update, _display]


def input_correct():
    if len(guess) != 1:
        print("You should input a single letter")
        return False
    if guess in guess_set or guess in wrong_guess_set:
        print("You already typed this letter")
        return False
    if not guess.islower():
        print("It is not an ASCII lowercase letter")
        return False
    return True


def start_game():
    if_start = input('Type "play" to play the game, "exit" to quit: ')
    if if_start == "play":
        return True
    if if_start == "exit":
        return False
print("H A N G M A N")

while start_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(word_list)
    display = "-" * len(answer)
    guess_set = set()
    wrong_guess_set = set()
    life = 0
    while life < 8:
        print('\n', display)
        guess = input("Input a letter: ")
        if input_correct():
            updates = game_update()
            life += updates[0]
            display = updates[1]
        if check_end():
            break
