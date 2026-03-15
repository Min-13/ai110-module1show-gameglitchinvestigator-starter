# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, the UI loaded correctly and allowed me to enter guesses, but several logical bugs appeared during gameplay.

One bug was that the hints were incorrect. For example, when the correct answer was 77 and my first guess was 25, the game told me to go lower, which was wrong. In fact, it always told me to go lower no matter what number I entered. Even when I guessed 1, it still suggested going lower. In another case, when the correct answer was 68 and I guessed 100 (the maximum value), the game told me to go higher, which is impossible.

Another bug involved the New Game button. After winning, pressing New Game changed the secret number, but the game would not allow me to continue playing.

There were also logical inconsistencies in the difficulty settings. For example, easy mode had fewer attempts than normal mode, and the guessing ranges did not match the difficulty levels (normal mode used a wider range of 1–100, while hard mode used a narrower range of 1–50).

The attempt counter logic was also incorrect. The game-over message appeared when I still had one attempt left. For example, in normal mode I should have had 6 attempts, but the game ended after my 5th guess and displayed the score.

Finally, the scoring logic was incorrect. Winning on the first attempt should give 100 points, but the original scoring formula did not produce that result.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot on this project.

One AI suggestion that was correct was related to the score formula. Originally, the formula was points = 100 - 10 * attempt_number, but Copilot suggested subtracting 1 from the attempt number so that winning on the first attempt would give 100 points. I reviewed the logic and tested the game, and the scoring worked correctly after the change.

One AI suggestion that was misleading involved the game difficulty logic. AI confidently suggested that the range and number of attempts for each difficulty level were correct, even though the logic was inconsistent. For example, the relationship between the guessing range and the number of attempts did not properly reflect what “easy” or “hard” should mean. I discovered this by manually testing the UI and noticing that the difficulty levels did not feel consistent, which showed that AI does not truly understand concepts like difficulty unless a programmer clearly defines them.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed when the issue itself was resolved and the change still worked well with the rest of the code. I also checked the UI to make sure the game behaved consistently across different modes.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran the pytest test test_parse_guess_below_lower_limit, which checks whether the parse_guess function correctly rejects numbers below the allowed range. The test used "0" as the input while the valid range was 1 to 100. The expected result was that the function should return ok = False, guess = None, and an error message saying "Enter a number between 1 and 100."
This test showed me that my code correctly validates the range of the guess and prevents users from entering numbers outside the allowed limits. It confirmed that the input validation logic in parse_guess works as expected.

- Did AI help you design or understand any tests? How?
 Yes, AI helped me understand some of the tests. After AI generated the test code, I asked it to explain what each line was doing, which helped me understand how the test worked. This was especially helpful because I do not have much experience writing tests yet.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Rerun = Streamlit reloads the whole script whenever the user interacts with the app.
Session state = a memory that keeps important variables so they don’t reset every time the script reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse in future projects is being more judicious about AI-generated code by carefully reviewing and reflecting on its output to ensure the logic is consistent. I also plan to use AI as a tool to help explain concepts so I can better understand the code rather than just copying it.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would test the code using different AI models so that one model can catch mistakes that another model might miss.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can still contain logical mistakes and may not fully consider real-world expectations, such as balancing difficulty levels in a game. In this project, I noticed that the AI did not properly align the difficulty settings—for example, giving the hard mode fewer attempts while also having a wider guessing range.