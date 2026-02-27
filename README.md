# 🎮 Python Tetris Game

## 📌 Project Description
This project is a classic implementation of the Tetris Game developed using Python and the Pygame library.  
The game follows Object-Oriented Programming (OOP) principles and is structured into multiple modules to ensure clean code organization, scalability, and maintainability.

The objective of the game is to control falling Tetromino blocks, arrange them strategically, and clear complete horizontal rows to score points.

---

## 🧠 Game Features

- Classic Tetris Gameplay  
- Seven Different Tetromino Shapes (I, J, L, O, S, Z, T)  
- Block Rotation System  
- Collision Detection  
- Grid-Based Movement  
- Row Clearing Functionality  
- Score Tracking  
- Sound Effects  
- Modular and Clean Code Structure  

---

## 🗂️ Project File Structure

Tetris-Game/
│
├── sounds/            → Contains sound effects used in the game  
│
├── block.py           → Base Block class  
├── blocks.py          → Tetromino shape definitions  
├── colors.py          → RGB color configurations  
├── game.py            → Core game logic and mechanics  
├── grid.py            → Grid system and row clearing logic  
├── main.py            → Game loop and rendering  
├── position.py        → Position class for grid cells  
│
└── README.md          → Project documentation  

---

## ⚙️ System Requirements

- Python 3.x  
- Pygame Library  

---

## 📦 Installation

### 1️⃣ Install Python
Download and install Python from:
https://www.python.org/

### 2️⃣ Install Pygame
Open your terminal or command prompt and run:

pip install pygame

---

## ▶️ Running the Game

Navigate to the project directory and run:

python main.py

---

## 🎮 Game Controls

| Key              | Function            |
|------------------|---------------------|
| ← Left Arrow     | Move Block Left     |
| → Right Arrow    | Move Block Right    |
| ↓ Down Arrow     | Move Block Down     |
| ↑ Up Arrow       | Rotate Block        |
| ESC              | Exit Game           |

---

## 🧱 Game Architecture Overview

position.py  
→ Stores row and column positions.

block.py  
→ Parent class for all block types.

blocks.py  
→ Defines each Tetromino shape.

grid.py  
→ Manages the board and clears completed rows.

game.py  
→ Controls gameplay logic and interactions.

main.py  
→ Runs the main game loop and handles rendering.

---

## 🔊 Sound Effects

The sounds/ directory includes sound effects for:

- Block movement  
- Block rotation  
- Row completion  
- Game over  

---

## 🚀 Future Improvements

- Ghost Piece Feature  
- Hold Block Functionality  
- Difficulty Levels  
- Pause Menu  
- High Score Saving System  

---

## 🏗️ Built With

- Python  
- Pygame  

---

## 👨‍💻 Author

Developed by: Mazen Younes
