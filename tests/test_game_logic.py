from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the reversed-hints bug ---
# Bug: check_guess previously returned "Too Low" when guess > secret (and vice
# versa), so the game told players to guess higher when they should go lower.

def test_hint_direction_not_reversed_high():
    # Regression: guess(80) > secret(30) must say "Too High", NOT "Too Low"
    outcome, _ = check_guess(80, 30)
    assert outcome == "Too High", f"Expected 'Too High' but got '{outcome}' — hints may be reversed again"

def test_hint_direction_not_reversed_low():
    # Regression: guess(10) < secret(90) must say "Too Low", NOT "Too High"
    outcome, _ = check_guess(10, 90)
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}' — hints may be reversed again"

def test_hint_one_away_high():
    # Edge case: guess is exactly one above secret — must still report "Too High"
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_hint_one_away_low():
    # Edge case: guess is exactly one below secret — must still report "Too Low"
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"
