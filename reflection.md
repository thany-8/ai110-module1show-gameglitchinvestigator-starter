# 💭 Reflection: Game Glitch Investigator

  Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your        process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  When I first ran the game, the basic interface loaded, but several features were not working correctly. I tested the main gameplay        functions by interacting with the controls and observing the game's behavior. During my initial testing, I noticed multiple bugs that     affected gameplay and user experience.
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

 * Bug #1: The score calculation logic in the update_score function was incorrect. The game was calculating the winning score incorrectly    because of an off-by-one error. In addition, wrong guesses were not penalized consistently, causing some incorrect guesses to receive     points instead of losing points.
   
 * Bug #2: The game allowed guesses outside the valid range of 1 to 100. It continued to provide "higher" and "lower" hints even when the    player entered values below 1 or above 100, resulting in confusing gameplay.
   
 * Bug #3: When I tried to start a new game, the game did not reset as expected. Instead, I had to manually refresh the browser page to      begin another round, the reset functionality was not working correctly.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|I tested the score after making guesses during the game, including correct and incorrect guesses. |The score should be calculated correctly. A correct guess should receive the proper win score, and incorrect guesses such as "Too High" or "Too Low" should be penalized consistently. |The update_score function calculated the score incorrectly. The win score was 10 points lower than expected because of an extra +1 in the formula. Also, some wrong guesses were rewarded points instead of being penalized.|No console error was displayed, but the score logic was incorrect. |
|I entered guesses outside the valid range, including values below 1 and above 10 | The game should only accept guesses between 1 and 100. If the player enters a value outside this range, the game should display an error message and request a valid input. |The game allowed guesses outside the valid range of 1 to 100. It continued to provide "higher" and "lower" hints even when I entered values below 1 or above 100, resulting in confusing gameplay. |No console error was displayed, but the game logic did not properly validate user input.|
|The New Game command does not work |the game should reset and start a new round with a new secret number |Nothing happen when I selected New Game. I have to refresh the browser to start a new game | No console error  |



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  GitHub Copilot, using Claude Sonnet 4.6.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  The AI suggested adding input validation to prevent guesses below 1 or above 100. I implemented the suggested changes and tested the      game by entering values such as -1 and 200. The game correctly displayed an error message and did not accept the invalid guesses,         confirming that the AI's suggestion was correct.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI suggested deleting one of the conditions because, according to its analysis, that condition did not exist in the original code.    I found this suggestion interesting, so I checked the original repository to verify it. After reviewing the source code, I discovered     that the condition was actually present. This showed that the AI's suggestion was incorrect and highlighted the importance of verifying   AI generated recommendations against the original codebase.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
  I played the game several times and came to the conclusion that the issue had been fixed because I no longer received the incorrect       messages that appeared at the beginning. I then worked with the AI assistant to review the code and verify my observations. After         additional testing, I confirmed that the behavior I observed in the game matched the expected results.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  
  While testing the game manually, I discovered that the code responsible for displaying the hint messages did not enforce the valid        range of 1 to 100. As a result, the game continued to suggest guesses below 1 and above 100. After reviewing the code with the AI         assistant, I identified the missing range validation and corrected the issue. I then tested the game again and confirmed that the bug     had been resolved.

- Did AI help you design or understand any tests? How?

  Yes, AI helped me design and understand the tests. It explained the purpose of testing more clearly and helped me think about different   scenarios that should be tested, including edge cases and invalid inputs. I also learned several testing and debugging commands that I    had not used before. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  A good example is to imagine you have a notebook, and every time you write something, someone erases the entire page and makes you        start over. This is similar to how Streamlit reruns work every time a user clicks a button.
  Session state is the memory that allows the app to remember information. Even if someone erases your work, session state helps the app    remember what was there before.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  
  This project helped me become more familiar with VS Code and Git. One thing I want to reuse in future projects is learning how to take    advantage of AI assistants without overusing them.

- This could be a testing habit, a prompting strategy, or a way you used Git.
  
  AI helped me understand how to create efficient tests that cover possible edge cases that may occur in a program. I also enjoyed          becoming more familiar with Git and learning that it is not as complicated as it initially seemed.

- What is one thing you would do differently next time you work with AI on a coding task?
  
  I would rely less on the AI assistant at the beginning and spend more time developing my own ideas and understanding of the problem       first. Then, I would use AI to verify my reasoning, identify any misunderstandings, or fill in gaps in my knowledge.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project taught me that AI-generated code is most effective as an initial draft rather than a finished product, I realized that while AI speed up development, strict human oversight is always necessary to catch logical bugs and maintain system integrity.
