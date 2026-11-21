# Aaron Mairel
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORD_LIST,
    choose_random_word,
    process_guess,
    get_display_word,
)


def test_choose_random_word():
    # make sure the chosen word actually comes from the predefined word list
    chosen = choose_random_word()
    assert chosen in WORD_LIST


def test_process_guess_correct():
    # verify a right guess returns true and reveals all matching spots in the word
    guessed = []
    result = process_guess("loop", guessed, "o")
    assert result is True
    assert "o" in guessed
    assert get_display_word("loop", guessed) == "_ o o _"


def test_process_guess_incorrect():
    # verify a wrong guess returns false and keeps the display word hidden
    guessed = []
    result = process_guess("python", guessed, "z")
    assert result is False
    assert "z" in guessed
    assert get_display_word("python", guessed) == "_ _ _ _ _ _"
