# Tag Game
## Description
A local two-player tag-style platformer written with Pygame. Player 1 uses the ARROW keys, Player 2 uses WASD. The project uses rectangular platforms (drawn at runtime) and simple physics (gravity + jump impulse).

## Requirements
- Python 3.8+ (Windows)
- `pygame` (install via pip)
- `tkinter` (usually included with Python on Windows)

## Install
- Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Install Pygame:

```powershell
pip install pygame
```

## Run
- From the project directory (where `main.py` is located):

```powershell
python .\main.py
```

The game opens fullscreen using your primary display resolution.

## Controls
- Player 1 (arrow keys): `LEFT`, `RIGHT`, `UP` (jump)
- Player 2 (WASD): `A`, `D`, `W` (jump)
- `ESC`: return to the main menu or quit

## Gameplay
- One player is "it" (indicated by a small arrow above the character). When the players are near each other the tag will switch after a short cooldown.
- Platforms are drawn as rectangles based on the `platformlist` in `main.py`.
- A simple timer counts down the round (30 seconds by default).

## Configuration & Tuning
- Physics constants are defined near the top of the `gameloop()` function in `main.py`:
  - `GRAVITY` – gravity applied each frame
  - `JUMP_VELOCITY` – the upward impulse applied when jumping (negative value)
  - `MOVE_SPEED` – horizontal movement speed

If jumps feel too floaty or too snappy, tweak `GRAVITY` and `JUMP_VELOCITY` to taste.

## Platforms
- Platforms are defined by tuples in `platformlist`: `(x, y, width, height)`.
- Platforms are rendered with `platform_color` and an optional `platform_border` in `main.py`.
- To change platform placement or size, edit the `platformlist` values.

## Assets
- Skins: images are expected in `images/skins`.
- Backgrounds and UI images are in `images/` (menu assets, arrow icon, etc.).

## Troubleshooting
- If Pygame fails to initialize audio on your system, either install appropriate audio backends or comment out `pygame.mixer` usage in `main.py`.
- If the game briefly shows a Tk window (used to read screen resolution), it is normal. If you'd prefer no visible Tk window, modify the initial screen-size detection to withdraw the root window: `root.withdraw()` after creating `root`.

