Tactical Espionage

Tactical Espionage is a 2D side-scrolling tactical shooter game developed using Python and Pygame.
The game features player and enemy AI, shooting mechanics, grenades, explosions, health and ammo systems, level progression, and a tile-based world loaded from CSV files.

This project demonstrates core game-development concepts such as physics, animation handling, AI behavior, collision detection, and resource management.

🎮 Game Features

2D side-scrolling shooter gameplay

Player and enemy characters with animations

Enemy AI with vision and patrol behavior

Shooting system with bullets and cooldown

Grenades with physics, timer, and explosion damage

Health, ammo, and grenade pickup items

Tile-based level system loaded from CSV files

Multiple levels with level progression

Parallax scrolling background

Sound effects and background music

Start menu, restart option, and fade effects

Death screen and level completion logic

🛠 Technologies Used

Python 3

Pygame

pygame.mixer (for sound and music)

CSV (for level data)

Object-Oriented Programming (OOP)

📁 Project Structure
.
├── final.py                  # Main game file
├── button.py                 # Button UI logic
├── level0_data.csv           # Level 0 tile map
├── level1_data.csv           # Level 1 tile map
├── img/
│   ├── Background/
│   ├── Tiles/
│   ├── player/
│   ├── enemy/
│   ├── explosion/
│   └── icons/
├── audio/
│   ├── music2.mp3
│   ├── jump.wav
│   ├── shot.wav
│   └── grenade.mp3
└── README.md

⚙️ Installation & Setup
1. Install Python

Make sure Python 3.9 or higher is installed.

2. Install Required Libraries
pip install pygame

3. Run the Game
python final.py

🎹 Controls
Key	Action
A	Move left
D	Move right
W	Jump
SPACE	Shoot
G	Throw grenade
ESC	Exit game
🧠 Game Mechanics Overview
Player

Has health, ammo, and grenades

Can run, jump, shoot, and throw grenades

Dies when health reaches zero or falls off the map

Enemies

Patrol platforms automatically

Detect the player using a vision rectangle

Shoot when the player is in sight

Can be killed by bullets or explosions

Weapons

Bullets: Fast, limited by ammo and cooldown

Grenades: Affected by gravity, explode after a timer

Items

Health Box: Restores player health

Ammo Box: Adds bullets

Grenade Box: Adds grenades

🗺 Level System

Levels are defined using CSV files

Each number represents a tile, object, or entity

The game supports multiple levels and transitions automatically

🎨 Graphics & Audio

Sprite-based animations for characters

Parallax background for depth effect

Sound effects for jumping, shooting, and explosions

Background music loop using pygame.mixer

🔄 Future Improvements

More enemy types and smarter AI

Boss fights

Weapon variety

Save/load system

Settings menu

Improved UI and HUD

Better performance optimization

📜 License

This project is created for learning and educational purposes.
You are free to modify and extend it.

👤 Author

Developed by Armin Maleki
Python & Game Development Enthusiast 🎮🐍
