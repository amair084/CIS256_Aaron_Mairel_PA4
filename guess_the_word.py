# Aaron Mairel
# CIS256 Fall 2026
# Programming Assignment 4

import random

# list of possible words for the game
WORD_LIST = ["python", "variable", "function", "loop", "tuple", "string"]


def choose_random_word(words=WORD_LIST):
    # pick one random word from the predefined list
    selected_word = random.choice(words)
    return selected_word


def process_guess(secret_word, guessed_letters, guess):
    # check if the guessed letter is in the secret word and update the guessed list
    guess = guess.lower()
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if guess in secret_word:
        return True
    else:
        return False


def get_display_word(secret_word, guessed_letters):
    # build the current word string showing guessed letters and underscores for hidden ones
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)