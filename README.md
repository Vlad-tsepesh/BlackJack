
# 🃏 Blackjack (OOP Edition)

---
A terminal-based Blackjack game implemented in Python using Object-Oriented Programming (OOP) and SOLID principles.

This project builds upon the first capstone from the [100 Days of Code: Python Bootcamp by Angela Yu](https://www.udemy.com/course/100-days-of-code/), enhancing it with professional design practices such as separation of concerns, encapsulation, and clean architecture.

It provided an excellent opportunity to apply OOP principles I mastered in Java within Python, reinforcing concepts like inheritance, encapsulation, and design patterns. Developing this Blackjack game strengthened my architectural thinking, with a focus on maintainability and clean code. I enjoyed translating ideas across languages and refining my coding style. Moving forward, I plan to expand this project and deepen my knowledge of Pythonic idioms and advanced features.


---
## 📌 Features

- Fully playable Blackjack game in the terminal

---

## 🗂️ Project Structure

```
.
├── main.py              # Game entry point
├── game.py              # Game engine and flow
├── game_ui.py           # User interface (terminal display and input)
├── evaluator.py         # Game result logic and outcome evaluation
├── player.py            # Player class
├── dealer.py            # Dealer (inherits Player)
├── deck.py              # Deck and card generation
├── card.py              # Card object
├── game_constants.py    # Constants and card symbols
└── README.md            # Project documentation
```


---

## ▶️ Run the Game

```bash
python main.py
```

---

## ✅ Example Gameplay

```
♥  ♠  Black Jack ♦  ♣    Bank: $1000

Dealer's hand: 7♤|4♤ - ??
Player's hand: Q♢|A♡ - 21

🎉 Player has Blackjack!
✅ Player wins!
```

---

## 🧠 What I Learned

- Designing extensible OOP programs
- Separating game flow from UI and logic
- Managing game state and user input
- Applying SOLID design principles in a real project


---

## 📄 License

This project is for educational purposes only.

