https://roadmap.sh/projects/number-guessing-game
# Number Guessing Game (CLI – Python)

A command-line based Number Guessing Game built with Python.  
The computer randomly selects a number, and the player must guess it within a limited number of attempts based on the selected difficulty level.  
The game tracks player performance persistently using a JSON file.

---

## 🎯 Features

- Random number generation between 1 and 100
- Three difficulty levels:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Persistent score tracking using `scores.json`
- Tracks:
  - Games played per difficulty
  - Best (lowest) number of attempts
  - History of attempts
- Input validation and error handling
- Replayable game loop
- Clean, modular Python code

---

## 🛠 Technologies Used

- Python 3.x
- Standard Python libraries:
  - `random`
  - `json`
  - `os`

---

## 📁 Project Structure

```text
number_guessing_game/
│
├── game.py          # Main game logic
├── scores.json      # Persistent score storage
└── README.md        # Project documentation
