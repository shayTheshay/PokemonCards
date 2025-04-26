# Pokémon Memory Game 🃏

This is a basic Memory Card Game ("Pokémon Memory Game") project, created as part of the **Appleseeds AWS re/Start** course, while learning **Python** and **Tkinter**.

---

## 📚 About the Project

The goal of the game is simple:
- You are presented with cards faced down.
- Click two cards to flip them.
- If they match, they stay face up.
- If not, they flip back after a short delay.
- The objective is to find all matching pairs!

---

## 🎯 Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **PIL** (Python Imaging Library) for image handling
- Basic principles of:
  - Functions and event handling
  - OOP (Object-Oriented Programming) with a simple `cardPokemon` class
  - Code modularity (splitting into multiple files: `screen.py`, `window_config.py`, `logic.py`, etc.)

---

## 🛠 Project Structure

| File | Purpose |
|:-----|:--------|
| `main.py` | Starting point — initializes the window and runs the game |
| `window_config.py` | Handles window and mainframe creation |
| `screen.py` | Handles card grid, game logic, card clicking |
| `logic.py` | Organizes game flow and user messages |
| `data.py` | Manages card data and image paths |

---

## 🧠 Purpose of the Assignment

This project was done as a **basic assignment** in the Appleseeds **AWS re/Start** course,  
focused on practicing:

- Python programming fundamentals
- Building GUIs using Tkinter
- Organizing larger projects into modules
- Handling user interaction events
- Using external libraries like PIL for image manipulation

---

## 🎉 How to Play

1. Run `main.py`.
2. Click on two cards to reveal them.
3. If the two cards match, they stay revealed.
4. If they don't match, they will automatically flip back after a short delay.
5. Match all pairs to win the game!

---

## ⚙️ How to Run

Make sure you have the following installed:
- Python 3.x
- Pillow library (`pip install Pillow`)

Then simply run:

```bash
python main.py