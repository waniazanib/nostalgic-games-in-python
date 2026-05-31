# Nostalgic Games in Python

A collection of classic nostalgic games developed in Python with a centralized graphical menu launcher. Launch and play multiple games from a unified interface.

## Overview

This project features a **Game Hub** application built with Tkinter that provides access to multiple classic games through an intuitive GUI. The main menu launcher allows seamless switching between games with a consistent, retro-themed interface.

## Features

- **Centralized Game Launcher**: Graphical menu interface to access all games
- **Snake Game**: Classic snake gameplay with adjustable difficulty levels (Easy, Medium, Hard)
- **Tic Tac Toe**: Turn-based strategic gameplay
- **Chess Game**: Full chess implementation with standard rules
- **Score Tracking**: Real-time score display during gameplay
- **Fullscreen Mode**: Immersive gaming experience
- **Smooth Game Switching**: Return to menu and launch new games seamlessly
- **Confirmation Dialogs**: Prevent accidental quitting with score confirmation

## Tech Stack

- **Language**: Python 3.x
- **GUI Framework**: Tkinter (built-in)
- **Architecture**: Object-Oriented Programming

## Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/waniazanib/nostalgic-games-in-python.git
   cd nostalgic-games-in-python
   ```

2. No external dependencies required - Tkinter is included with most Python distributions.

## Usage

### Launch the Game Hub

Start the application by running the main menu:

```bash
python menu.py
```

The Game Hub window will open in fullscreen mode with four options:
- **Snake Game**: Start a new snake game session
- **Tic Tac Toe**: Play tic tac toe
- **Chess Game**: Play chess
- **Quit**: Exit the application

### Game Controls

**Snake Game**:
- Arrow keys to control snake direction
- Eat food to increase score
- Avoid hitting yourself
- Click "Quit" to return to menu

**Tic Tac Toe**:
- Click on board positions to place your move

**Chess Game**:
- Follow standard chess rules and controls

## Environment Variables

No environment variables are required for this project. All configuration is handled internally.

## Folder Structure

```
nostalgic-games-in-python/
├── menu.py           # Main menu launcher (entry point)
├── snake.py          # Snake game implementation
├── tic.py            # Tic tac toe game implementation
├── ch.py             # Chess game implementation
├── requirements.txt  # Project dependencies (currently empty)
└── README.md         # This file
```

## Future Improvements

- Add sound effects and background music
- Implement game difficulty settings persistence
- Add high score leaderboard
- Create additional classic games (Pac-Man, Breakout, etc.)
- Add animations and visual effects
- Implement multiplayer support for applicable games
- Create installer/executable for distribution
- Add settings menu for customization
- Implement pause functionality during gameplay
- Add tutorial/help screens for each game

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for bug fixes or new features.

---

**Author**: [waniazanib](https://github.com/waniazanib)