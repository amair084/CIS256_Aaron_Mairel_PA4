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


def play_game():
    # main loop to run the word guessing game in the console
    secret_word = choose_random_word()
    guessed_letters = []
    attempts_left = 6

    print("welcome to the word guessing game")
    print(f"the word has {len(secret_word)} letters")

    while attempts_left > 0:
        current_progress = get_display_word(secret_word, guessed_letters)
        print("\nword:", current_progress)
        print("attempts left:", attempts_left)

        # check if there are no underscores left which means the player won
        if "_" not in current_progress:
            print(f"\ncongratulations you guessed the word: {secret_word}")
            return

        guess = input("guess a single letter: ").strip().lower()

        # make sure the player entered one valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("please enter just one valid letter")
            continue

        if guess in guessed_letters:
            print("you already guessed that letter try another one")
            continue

        is_correct = process_guess(secret_word, guessed_letters, guess)
        if is_correct:
            print(f"nice job '{guess}' is in the word")
        else:
            attempts_left -= 1
            print(f"sorry '{guess}' is not in the word")

    print(f"\nout of attempts the word was: {secret_word}")


if __name__ == "__main__":
    play_game()
