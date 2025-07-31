# War Card Game CLI 🃏
**War Card Game CLI** is a modular, object-oriented Python application implementing the classic two-player card game *War* with a command-line interface (CLI). Designed with clean architecture and interactive gameplay, this project demonstrates advanced Python programming principles and CLI development best practices.

## Overview
War (also known as Battle in the United Kingdom) is a simple card game typically played by two players using a standard playing card deck. The objective of the game is to win all of the cards. In this implementation, the player with the higher number of cards at the end of 10 rounds is declared the winner.


## Features
- **Clean Architecture:** Well-structured Python modules and classes that facilitate maintenance and extension  
- **CLI Integration:** User-friendly command-line experience with input prompts and options  
- **Customizable Gameplay:** Dynamic player names and adjustable round counts  
- **Real-time Feedback:** Step-by-step game state updates with controlled pacing for readability  
- **Test Coverage:** Comprehensive unit tests to validate core functionality

## Requirements
- Python 3.7 or higher  
- [`click`](https://pypi.org/project/click/) (install via `pip install click`)  
- No additional third-party dependencies  

## Setup
Clone the repository:
```bash
git clone https://github.com/<username>/cardgame.git
```
Install package:
```bash
pip install --user .
```

Verify Installation:
```bash
pip list
# Confirm that 'cardgame' version 1.0.0 is installed
```

Run CLI:
```bash
cardgame --player1 <player1-name> --player2 <player2-name> 
```

## Testing
```bash
pytest tests/
```
If using an IDE such as PyCharm, tests can be run and debugged directly within the interface, offering visualization and coverage tools.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.