# Snake Game - Requirements Specification

## Project Overview
A classic Snake game implementation in Python using Pygame where the player controls a snake to eat food, grow longer, and avoid collisions.

## Functional Requirements (EARS Notation)

### FR-1: Game Initialization
**WHEN** the game starts, **THE SYSTEM SHALL** initialize an 800x600 pixel game window with a black background.

### FR-2: Snake Movement
**WHILE** the game is running, **THE SYSTEM SHALL** continuously move the snake in its current direction at 15 FPS.

### FR-3: Player Input
**WHEN** the player presses an arrow key, **THE SYSTEM SHALL** change the snake's direction accordingly (UP/DOWN/LEFT/RIGHT).

### FR-4: Food Spawning
**WHEN** the game starts **OR** food is eaten, **THE SYSTEM SHALL** spawn food at a random valid position on the grid.

### FR-5: Food Consumption
**IF** the snake's head position equals the food position, **THEN THE SYSTEM SHALL** increase the snake's length by 1 and spawn new food.

### FR-6: Collision Detection - Boundaries
**IF** the snake's head moves outside the game window boundaries, **THEN THE SYSTEM SHALL** trigger game over state.

### FR-7: Collision Detection - Self
**IF** the snake's head collides with any part of its body, **THEN THE SYSTEM SHALL** trigger game over state.

### FR-8: Score Display
**WHILE** the game is running, **THE SYSTEM SHALL** display the current score (snake length - 1) at the top-left corner.

### FR-9: Game Over Screen
**WHEN** game over is triggered, **THE SYSTEM SHALL** display "You Lost! Press Q-Quit or C-Play Again" message.

### FR-10: Game Restart
**WHEN** the player presses 'C' on the game over screen, **THE SYSTEM SHALL** restart the game with initial state.

### FR-11: Game Exit
**WHEN** the player presses 'Q' on game over screen **OR** closes the window, **THE SYSTEM SHALL** terminate the game.

## Non-Functional Requirements

### NFR-1: Performance
The game SHALL maintain a consistent frame rate of 15 FPS without lag.

### NFR-2: Responsiveness
The game SHALL respond to player input within 100ms.

### NFR-3: Visual Clarity
- Snake SHALL be rendered in green color
- Food SHALL be rendered in red color
- Grid block size SHALL be 10x10 pixels

### NFR-4: Code Quality
The implementation SHALL use Object-Oriented Programming with separate classes for Snake, Food, and Game entities.

## Constraints
- Python version: 3.11.6
- Library: Pygame 2.6.1
- Platform: Cross-platform (macOS, Windows, Linux)

## Out of Scope
- Multiple difficulty levels
- Sound effects
- High score persistence
- Multiplayer mode
- Power-ups or special items
