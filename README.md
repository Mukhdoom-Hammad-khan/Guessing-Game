# Flask Number Guessing Game
## Overview
This is a simple number guessing game built using Python's Flask framework. Users can register and log in, with credentials stored in plain text files. Once logged in, players can choose from three difficulty levels (Easy, Normal, or Hard) that determine the range of the randomly generated number. The game then gives feedback—indicating if the guess is too high or too low—and limits the number of turns a player has to win.

## Features
User Authentication: Register and log in with credentials stored in text files.
Difficulty Levels:
    Easy: Guess a number between 1-10
    Normal: Guess a number between 1-100
    Hard: Guess a number between 1-1000
Turn-based Gameplay: Players have a set number of turns to guess the correct number.
Real-time Hints: Receive feedback if the guess is too high or too low.
Frontend: Built using HTML, CSS, and Jinja templating.

## Installation
### Prerequisites
Python 3.x
Flask

## Setup
Clone the Repository:
```bash
git clone https://github.com/yourusername/guessing-game.git
cd guessing-game
```

Create a Virtual Environment (Optional but Recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install Dependencies:
```bash
pip install flask
```

Run the Application:
```bash
python app.py
```

Access the Application: Open your browser and navigate to http://127.0.0.1:5000.

## Usage
Register: Create a new account using the registration form.
Login: Log in with your registered credentials.
Start the Game: Click on the "Start" button on the home page to select a difficulty level.
Play: Use the on-screen keypad to input your guess. The game will provide hints like "Guess Is Greater" or "Guess Is Lesser."
Game Outcome:
    Win: If you guess the number correctly, a win screen is displayed.
    Loss: If you run out of turns without guessing correctly, a loss screen is shown.
    Play Again: Choose to restart the game from the win or loss screen.

## Project Structure
```pgsql
  guessing-game/
  │
  ├── app.py               # Main Flask application file
  ├── templates/           # HTML templates (base.html, index.html, game.html, login.html, register.html, page1.html, win.html, loss.html)
  ├── static/              # CSS files (style.css)
  ├── D:\Name.txt         # Text file for storing usernames (update file path as needed)
  ├── D:\Password.txt     # Text file for storing passwords (update file path as needed)
  └── README.md            # This file
```
Note: Adjust the file paths for Name.txt and Password.txt according to your operating system if necessary.

## Technologies Used
Flask: Python web framework.
Jinja2: Template engine for rendering HTML pages.
HTML & CSS: Frontend structure and styling.
Plain Text Files: Used to store user credentials (usernames and passwords).

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact [your-email@example.com].
