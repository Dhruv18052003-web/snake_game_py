# Snake Game - Design Document

## Architecture Overview
The game follows an Object-Oriented Programming (OOP) architecture with three main classes:
- **Snake**: Manages snake entity (movement, growth, collision)
- **Food**: Manages food entity (spawning, rendering)
- **Game**: Manages game loop, state, input, and display

## Class Design

### 1. Snake Class
**Responsibility**: Snake entity behavior and state

**Attributes:**
- `block_size`: Size of each snake segment (10px)
- `body`: List of [x, y] coordinates representing snake segments
- `length`: Current length of the snake
- `x_change`, `y_change`: Movement direction deltas

**Methods:**
- `move()`: Updates snake position based on current direction
- `grow()`: Increases snake length by 1
- `set_direction(x, y)`: Changes movement direction
- `check_collision(width, height)`: Detects boundary and self-collision
- `draw(surface, color)`: Renders snake on display
- `get_head()`: Returns head position for collision checks

### 2. Food Class
**Responsibility**: Food entity spawning and rendering

**Attributes:**
- `width`, `height`: Game window dimensions
- `block_size`: Size of food block (10px)
- `position`: Current [x, y] coordinates of food

**Methods:**
- `spawn()`: Generates random valid position aligned to grid
- `draw(surface, color)`: Renders food on display

### 3. Game Class
**Responsibility**: Game loop, state management, and orchestration

**Attributes:**
- `width`, `height`: Window dimensions (800x600)
- `block_size`: Grid cell size (10px)
- `speed`: Frame rate (15 FPS)
- `display`: Pygame display surface
- `clock`: Pygame clock for FPS control
- `font`: Font for text rendering
- Color constants: `white`, `black`, `red`, `green`

**Methods:**
- `show_score(score)`: Displays current score
- `show_message(msg, color)`: Displays text messages
- `run()`: Main game loop

## Game Loop Design

```
INITIALIZE game, snake, food

WHILE NOT game_over:
    
    IF game_close:
        DISPLAY game over message
        HANDLE restart/quit input
        CONTINUE
    
    HANDLE input events:
        - Arrow keys → set snake direction
        - Quit event → exit game
    
    UPDATE game state:
        - Move snake
        - Check collisions → set game_close if collision
        - Check food consumption → grow snake, spawn new food
    
    RENDER:
        - Clear screen (black)
        - Draw food (red)
        - Draw snake (green)
        - Draw score
        - Update display
    
    CONTROL frame rate (15 FPS)

QUIT pygame
```

## State Management

### Game States
1. **Running**: Normal gameplay, snake moving, accepting input
2. **Game Close**: Collision detected, showing game over screen
3. **Game Over**: Player chose to quit, exit application

### State Transitions
- `Running` → `Game Close`: Collision detected
- `Game Close` → `Running`: Player presses 'C' (restart)
- `Game Close` → `Game Over`: Player presses 'Q' (quit)

## Input Handling
- **Arrow Keys**: Change snake direction (no 180° reversal allowed implicitly by game mechanics)
- **C Key**: Restart game (only in game close state)
- **Q Key**: Quit game (only in game close state)
- **Window Close**: Exit application

## Collision Detection

### Boundary Collision
```
IF head.x < 0 OR head.x >= width OR head.y < 0 OR head.y >= height:
    COLLISION = True
```

### Self Collision
```
FOR each segment in body[1:]:
    IF segment == head:
        COLLISION = True
```

### Food Collision
```
IF head == food.position:
    CONSUME food
```

## Rendering Pipeline
1. Fill screen with black background
2. Draw food (red rectangle at food position)
3. Draw snake (green rectangles for each body segment)
4. Draw score text (white, top-left corner)
5. Update display

## Grid System
- Grid-aligned movement: All positions are multiples of 10
- Food spawns on grid: `round(random / 10.0) * 10.0`
- Snake moves in block_size increments (10px)

## Module Structure
```
Snake-Game/
├── venv/                  # Virtual environment
├── src/
│   ├── food.py           # Food class
│   ├── game.py           # Snake + Game classes
│   └── snake.py          # (deprecated procedural version)
├── requirements.md       # This document
└── design.md            # This document
```

## Performance Considerations
- Fixed frame rate (15 FPS) ensures consistent gameplay
- Minimal rendering: Only necessary elements drawn each frame
- Efficient collision detection: O(n) where n = snake length
- Grid-aligned positions: Simplifies collision checks

## Future Enhancements (Not Implemented)
- Prevent 180° direction reversal explicitly
- Add pause functionality
- Implement difficulty levels (speed adjustment)
- Add sound effects
- Persist high scores
- Add obstacles or walls
