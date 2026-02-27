🎮 Tetris Game (Python + Pygame)
📌 Overview

This project is a fully functional Tetris game built using Python and Pygame.
It follows an object-oriented design and separates game logic into multiple modules for better structure and maintainability.

The game includes block movement, rotation, collision detection, row clearing, scoring logic, and sound effects.

🧠 Features

✅ Classic Tetris gameplay

✅ 7 different Tetromino shapes (I, J, L, O, S, Z, T)

✅ Block rotation system

✅ Collision detection

✅ Row clearing system

✅ Score tracking

✅ Sound effects

✅ Clean modular structure

🗂️ Project Structure
sounds/          # Game sound effects
block.py         # Base Block class
blocks.py        # All Tetromino shapes
colors.py        # RGB color definitions
game.py          # Main game logic
grid.py          # Grid management and row clearing
main.py          # Game loop and rendering
position.py      # Position class (row, column)
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/tetris-game.git
cd tetris-game
2️⃣ Install dependencies

Make sure Python 3 is installed.

Install pygame:

pip install pygame
▶️ How to Run
python main.py
🎮 Controls
Key	Action
⬅️ Left Arrow	Move Left

➡️ Right Arrow	Move Right

⬇️ Down Arrow	Move Down

⬆️ Up Arrow	Rotate Block
ESC	Quit Game
🧱 Game Architecture

The game is designed using object-oriented programming principles:

Position → Stores row and column values.

Block → Parent class for all shapes.

Blocks → Defines each Tetromino.

Grid → Handles board logic and row clearing.

Game → Controls game mechanics.

Main → Runs the game loop and handles rendering.

🔊 Sounds

The sounds/ folder contains sound effects used for:

Block movement

Rotation

Row clearing

Game over

📈 Future Improvements

Add ghost piece feature

Add hold block functionality

Add difficulty levels

Add high score saving

Add pause menu

🏗️ Built With

Python 3

Pygame

👨‍💻 Author

Mazen Younes 
