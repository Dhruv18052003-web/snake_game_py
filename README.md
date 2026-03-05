# 🐍 Snake Game

A classic Snake game implementation in Python using Pygame with clean Object-Oriented architecture.

## 🎮 Game Preview

Control a snake to eat food, grow longer, and avoid collisions with walls and yourself!

## ✨ Features

- **Classic Gameplay**: Navigate the snake using arrow keys
- **Score Tracking**: Real-time score display based on snake length
- **Collision Detection**: Boundary and self-collision mechanics
- **Game Over & Restart**: Quick restart with 'C' or quit with 'Q'
- **Smooth Performance**: Consistent 15 FPS gameplay

## 🏗️ Architecture

### Project Structure
```
Snake-Game/
├── venv/                   # Virtual environment
├── src/
│   ├── game.py            # Main game loop & Snake class
│   ├── food.py            # Food entity class
│   └── snake.py           # (deprecated procedural version)
├── requirements.md        # EARS notation specifications
├── design.md             # Architecture & design details
└── README.md             # This file
```

### Class Diagram
```
┌─────────────────┐
│     Game        │
│─────────────────│
│ - display       │
│ - clock         │
│ - width/height  │
│─────────────────│
│ + run()         │
│ + show_score()  │
│ + show_message()│
└────────┬────────┘
         │ uses
         ├──────────────┬──────────────┐
         │              │              │
    ┌────▼─────┐   ┌────▼─────┐       │
    │  Snake   │   │   Food   │       │
    │──────────│   │──────────│       │
    │ - body   │   │ - position│      │
    │ - length │   │──────────│       │
    │──────────│   │ + spawn()│       │
    │ + move() │   │ + draw() │       │
    │ + grow() │   └──────────┘       │
    │ + draw() │                      │
    └──────────┘                      │
```

### Game Loop Flow
```
┌─────────────────────────────────────┐
│         Initialize Game             │
│   (Window, Snake, Food, Clock)      │
└──────────────┬──────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│         Event Handling               │
│  • Arrow Keys → Change Direction     │
│  • Q/C Keys → Quit/Restart           │
│  • Window Close → Exit               │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│         Update Game State            │
│  • Move Snake                        │
│  • Check Collisions (walls/self)     │
│  • Check Food Consumption            │
│  • Grow Snake if food eaten          │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│         Render Frame                 │
│  • Clear Screen (Black)              │
│  • Draw Food (Red)                   │
│  • Draw Snake (Green)                │
│  • Draw Score                        │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│      Control Frame Rate (15 FPS)     │
└──────────────┬───────────────────────┘
               │
               └──────► Loop back
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11.6
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dhruv18052003-web/snake_game_py.git
   cd snake_game_py
   ```

2. **Create virtual environment**
   ```bash
   python3.11 -m venv venv
   ```

3. **Activate virtual environment**
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install pygame
   ```

### Running the Game

```bash
python src/game.py
```

Or with virtual environment:
```bash
venv/bin/python src/game.py
```

## 🎯 How to Play

- **Arrow Keys**: Control snake direction (↑ ↓ ← →)
- **Objective**: Eat red food to grow longer
- **Avoid**: Hitting walls or your own body
- **Game Over**: Press `C` to restart or `Q` to quit

## 🛠️ Technical Details

### Core Classes

#### **Snake Class**
Manages snake entity behavior:
- Movement and direction control
- Growth mechanics
- Collision detection (boundaries and self)
- Rendering

#### **Food Class**
Manages food entity:
- Random grid-aligned spawning
- Rendering
- Position tracking

#### **Game Class**
Orchestrates gameplay:
- Game loop management
- State transitions (Running → Game Over → Restart)
- Input handling
- Display and UI rendering
- FPS control

### Game Configuration
- **Window Size**: 800x600 pixels
- **Block Size**: 10x10 pixels (grid-aligned)
- **Frame Rate**: 15 FPS
- **Initial Snake Length**: 1 segment
- **Colors**: Green (Snake), Red (Food), Black (Background)

## 📋 Requirements

See [requirements.md](requirements.md) for detailed functional requirements using EARS notation.

## 📐 Design

See [design.md](design.md) for comprehensive architecture and design decisions.

## 🧪 Development

### Code Style
- Object-Oriented Programming (OOP)
- Clean separation of concerns
- Minimal, efficient implementations

### Future Enhancements
- [ ] Prevent 180° direction reversal
- [ ] Add pause functionality
- [ ] Multiple difficulty levels
- [ ] Sound effects
- [ ] High score persistence
- [ ] Obstacles and power-ups

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Dhruv - [GitHub Profile](https://github.com/Dhruv18052003-web)

Email: dhruv.imsd@gmail.com

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Classic Snake game mechanics
- Coursera Python Game Development Project

---

**Enjoy the game! 🐍🎮**
