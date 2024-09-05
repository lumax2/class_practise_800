# Blackjack Game

```bash
This is a simple Blackjack (21 points) game built using Flask. Players interact with the game through a web browser, choosing to Hit (draw a card) or Stand (stop drawing cards), and compete with the dealer to see who gets closer to 21 without going over.
```

## Project Structure
/blackjack_game
   ├── app.py            # Flask application logic
   ├── templates         # HTML template files
   │   ├── index.html     # Game homepage
   │   ├── game.html      # Game interface
   │   ├── victory.html   # Victory page
   │   └── defeat.html    # Defeat page
   ├── static            # Static files (CSS stylesheets)
   │   └── style.css      # Stylesheet
   ├── .gitignore        # Git ignore file
   └── README.md         # Project documentation

## Installation
### 1. Install Dependencies
Ensure you have Python 3 installed. If Flask is not installed, you can install it via pip:
```
pip install flask
```
### 2. Run the Game
Navigate to the project directory and start the Flask server:
```
python app.py
```
Once the server is running, open a web browser and go to http://127.0.0.1:5000/ to start the game.

## How to Play
- At the start of the game, both the player and the dealer receive two cards. The player can see both of their cards and one of the dealer's cards.
- The player can choose:
  - Hit: Draw another card.
  - Stand: Stop drawing cards, and let the dealer play.
  
- The dealer will automatically draw cards based on standard Blackjack rules: The dealer will continue to draw cards until the hand value is 17 or greater.
- If the player exceeds 21 points, they bust and lose the game.

### Win Conditions:
- Player wins if:
  - The player's hand value is closer to 21 than the dealer's without exceeding 21.
  - The dealer busts (hand value exceeds 21).
  
- Dealer wins if:
  - The dealer's hand value is closer to 21 than the player's without exceeding 21.
  - The player busts (hand value exceeds 21).
  
- Tie:
  - If both player and dealer have the same hand value, the game is a tie.
### Game Logic
1. Card Class:
   - Represents a single card with a suit and a value.
   - Contains to_dict() and from_dict() methods to convert Card objects into dictionaries for session storage.
   
2. Deck Class:
   - Represents a full deck of 52 cards, shuffled at the start of the game.
   - Includes draw_card() method to deal cards from the deck.
   
3. Player Actions:
   - Players can choose to Hit (draw a card) or Stand (stop drawing).
   - After the player stands, the dealer will automatically draw cards based on the rules.
   
4. Victory and Defeat Pages:
   - If the player wins, the game redirects to victory.html.
   - If the player loses, the game redirects to defeat.html.

## .gitignore File
```
The project includes a .gitignore file to ignore the following:

# Python compiled files
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so

# Virtual environments
venv/
env/
.venv/
.env/

# IDE configurations
.vscode/
.idea/

# MacOS system files
.DS_Store

# PyCharm-related files
*.iml
*.ipr
*.iws

# Log files
*.log

# Flask session files
instance/

```

## License
This project is licensed under the MIT License.

### Explanation:
- Every code block is formatted inside the correct code block tags.
- You can copy and paste this entire `README.md` code directly into your `README.md` file in your project.

Let me know if you need further adjustments!
