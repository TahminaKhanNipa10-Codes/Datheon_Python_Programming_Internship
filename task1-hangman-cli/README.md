<div align="center">

# 🎮 Hangman Word Guessing Game (Console)

**Datheon Python Programming Internship: Task 1**

An interactive, modular console game built with string manipulation and control flow. The player guesses a hidden word letter by letter within 6 attempts.

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/type-console%20game-red)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

</div>

---

## 🎯 Features

- **ASCII Art Visuals:** Gallows art that updates with each incorrect guess.
- **Word Selection:** Randomly picks the secret word from `words.txt` (falls back to a built-in list if the file is missing).
- **Game Logic:** Tracks previously guessed letters, shows them every round, and does not penalize duplicate guesses.

## 🛠️ Technology Stack

| Category         | Details    |
|------------------|------------|
| Language         | Python 3   |
| Standard Library | `random`   |

## 📁 Project Structure

```text
task1-hangman-cli/
├── hangman.py   # Main game script
└── words.txt    # Word list for random selection
```

## 🚀 How to Run

1. **Navigate to the project directory**
   ```bash
   cd task1-hangman-cli
   ```

2. **Run the game**
   ```bash
   python hangman.py
   ```

## 🕹️ How to Play

1. A hidden word is shown as blanks, for example `_ _ _ _ _ _`.
2. Guess one letter at a time.
3. Each wrong guess adds a part to the gallows. You have **6 attempts**.
4. Guess the whole word before the drawing is complete to win!

## 🖥️ Sample Gameplay

```text
Word: _ _ _ _ _ _
Guessed letters: (none)
Attempts left: 6

Enter a letter: a
<your game's actual output here>
```

> Replace the sample output with your game's real output so the README matches the code.

## 👩‍💻 Author

**Tahmina Khan Nipa**

- GitHub: [@TahminaKhanNipa10-Codes](https://github.com/TahminaKhanNipa10-Codes)
- Datheon Batch: 01

---

<div align="center">⭐ If you found this useful, consider giving it a star!</div>
