import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "Congratulations! You've guessed the secret number."

def test_guess_too_high():
    # If the secret is 50 and guess is 60, it should return "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "Your guess is too high. Try again!"

def test_guess_too_low():
    # If the secret is 50 and guess is 40, it should return "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "Your guess is too low. Try again!"

def test_parse_guess_valid_upper_limit():
    # If the range is 1 to 100, 100 should be valid
    ok, guess, err = parse_guess("100", 1, 100)
    assert ok is True
    assert guess == 100
    assert err is None

def test_parse_guess_above_upper_limit():
    # If the range is 1 to 100, 101 should be invalid
    ok, guess, err = parse_guess("101", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_valid_lower_limit():
    # If the range is 1 to 100, 1 should be valid
    ok, guess, err = parse_guess("1", 1, 100)
    assert ok is True
    assert guess == 1
    assert err is None

def test_parse_guess_below_lower_limit():
    # If the range is 1 to 100, 0 should be invalid
    ok, guess, err = parse_guess("0", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_non_integer():
    # Non-integer input like "abc" should be invalid
    ok, guess, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "That is not a valid whole number."