# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose**

The purpose of this game is to create an interactive number-guessing game where the player tries to guess a randomly generated secret number within a limited number of attempts. The difficulty levels (Easy, Normal, Hard) change the range of possible numbers and the number of attempts allowed. The game provides feedback after each guess to guide the player toward the correct number.

**Bugs I Found**

While testing the game, I noticed several issues:

The hints were sometimes incorrect. For example, when the guess was lower than the secret number, the game would still suggest going lower.

The score appeared before the game was actually finished.

The number range displayed to the player was inconsistent with the difficulty level.

The New Game button did not properly restart the game after winning.

The number of attempts did not match the selected difficulty level.

**Fixes I Applied**

To resolve these issues, I made several changes:

Corrected the comparison logic so the hints correctly indicate whether the guess is too high or too low.

Adjusted the scoring logic by subtracting 1 from attempt_number so a correct guess on the first attempt results in a score of 100.

Replaced hardcoded number ranges with dynamic ranges based on the selected difficulty level.

Implemented proper range definitions:

**Easy: 1–20**

**Normal: 1–50**

**Hard: 1–100**

Fixed the attempt logic so easier modes allow more attempts while harder modes allow fewer.

Updated the reset logic so the New Game button properly restarts the game.

## 📸 Demo
file:///Users/minthawzin/Downloads/ai110_w3_project.pdf

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
