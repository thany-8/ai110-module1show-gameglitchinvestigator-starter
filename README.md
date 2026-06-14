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

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the app — Run python -m streamlit run app.py in your terminal. The game opens in the browser with the title "Game Glitch Investigator".
2. hoose a difficulty — In the left sidebar, select a difficulty level. For this walkthrough, choose Normal (range 1–100, 8 attempts allowed).
3. First guess: 50 — Type 50 and click Submit Guess. The hint reads "📉 Go LOWER!" and your score drops to -5. Attempts left: 7.
4. Second guess: 25 — Type 25 and click Submit Guess. The hint reads "📈 Go HIGHER!" and score drops to -10. Attempts left: 6.
5. Third guess: 37 — Type 37 and click Submit Guess. The hint reads "🎉 Correct!" — balloons animate on screen. Points awarded: 100 - 10 * 3 = 70. Final score: 60.
6. Game over — won — A success banner displays: "You won! The secret was 37. Final score: 60."
7. Start a new game — Click New Game 🔁. The secret resets to a new random number, score resets to 0, and attempt counter resets — ready to play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
