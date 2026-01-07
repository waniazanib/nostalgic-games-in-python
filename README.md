# nostalgic-games-in-python
 collection of classic nostalgic games developed in Python with a centralized "main menu launcher ".   Running the main file opens a graphical home screen from which users can launch individual games.

---
Games Included

1. Snake Game
- Classic snake gameplay
- Keyboard-controlled movement
- Score increases as the snake grows
- Game ends on self-collision

2.Tic-Tac-Toe
- Two-player game
- Win and draw detection
- Simple and interactive GUI

3. Chess Game
- Full chess board with legal move validation
- Human vs Computer gameplay
- Integrated with the Stockfish chess engine for AI moves
---

## Technologies Used

- Python 3
- Tkinter (GUI)
- python-chess
- Stockfish Chess Engine

---
Requirements

- Python **3.10 or higher**

Install Dependencies

```bash
pip install -r requirements.txt

---
Stockfish Engine Setup (Required for Chess)
The Chess game uses the Stockfish engine, which must be installed separately.

Steps:

1.Download Stockfish from the official website: https://stockfishchess.org/download/

2.Extract the executable file.

3.Update the Stockfish engine path in chess.py:
engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish.exe")
Ensure the path is correct for your operating system
---

How to Run the Project

Clone the repository: git clone https://github.com/waniazanib/nostalgic-games-in-python.git

Navigate into the project folder and run the main launcher: python menu.py

This will open the main menu GUI, from which you can:
Launch Snake
Launch Tic-Tac-Toe
Launch Chess
