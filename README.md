# War Card Game CLI 🃏
**War Card Game CLI** is a modular, object-oriented Python application implementing the classic two-player card game *War* with a command-line interface (CLI). Designed with clean architecture and interactive gameplay, this project demonstrates advanced Python programming principles and CLI development best practices.

## Overview
War (also known as Battle in the United Kingdom) is a simple card game typically played by two players using a standard playing card deck. The objective of the game is to win all of the cards. In this implementation, the player with the higher number of cards at the end of 10 rounds is declared the winner.

## How to Play
To play the game, follow these steps:

- Run the main Python program main.py.
- Enter the names of the two players.
- View the cards dealt to each player.
- Watch as the game progresses through 10 rounds.
- At the end of the game, the winner will be declared.

## Features
Object-oriented design: The game is implemented using classes and objects, making it modular and easy to understand.
Customizable: Players can enter their names and initial number of cards.
Interactive: The game prints out the moves and waits between rounds to build tension.
Unit tests: The program includes unit tests to ensure the correctness of the classes.

## Requirements
- Python 3.7 or higher  
- [`click`](https://pypi.org/project/click/) (install via `pip install click`)  
- No additional third-party dependencies  

## Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/cardgame-cli-app.git
cd cardgame-cli-app
python3 cli.py
```
2. 

## Unit Tests
If you're using PyCharm, you can run unit tests directly from the PyCharm interface instead of using terminal commands:
- Open your PyCharm project.
- Navigate to the test file in the Project tool window.
- Right-click on the test file and select "Run `Test-Name`" or "Run `Test-Name` with Coverage" from the context menu.
- PyCharm will execute the unit tests and display the results in the "Run" tool window.

By running the tests through PyCharm, you can take advantage of its features such as test result visualization, debugging, and coverage analysis.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
