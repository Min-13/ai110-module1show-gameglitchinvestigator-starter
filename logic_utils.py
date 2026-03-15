def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)  # Ensure the input is an integer
    except ValueError:
        return False, None, "That is not a valid whole number."

    # Validate the range dynamically
    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None

def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "Congratulations! You've guessed the secret number."
    elif guess > secret:
        return "Too High", "Your guess is too high. Try again!"
    else:
        return "Too Low", "Your guess is too low. Try again!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")