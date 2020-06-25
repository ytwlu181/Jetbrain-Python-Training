# Write your code here
import random


def update_display(answer, guess_set):
    _display = ""
    for _char in answer:
        if _char not in guess_set:
            _char = '-'
        _display += _char
    return _display


def check_end(display, answer, life):
    if life < 8 and display == answer:
        print('\n', answer)
        print("You guessed the word!")
        print("You survived!")
        return True
    if life >= 8 and display != answer:
        print("You are hanged!")
        return True


print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(word_list)
display = "-" * len(answer)
guess_set = set()
life = 0
while life < 8:
    print('\n', display)
    guess = input("Input a letter: ")

    if guess not in answer:
        life += 1
        print("No such letter in the word")
    else:
        if guess in guess_set:
            life += 1
            print("No improvements")

        guess_set.add(guess)
        display = update_display(answer, guess_set)
    if check_end(display, answer, life):
        break
