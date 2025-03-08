# Number Board Game 🎲

This is a grid-based number matching game where players select a cell, and all adjacent cells with the same value disappear. The grid shifts accordingly, and the game continues until no more moves are possible.

📌 How It Works

The game reads an initial board configuration from an input file (input.txt).

Players select a cell (row and column).

If the selected cell has at least one neighboring cell with the same value, all matching cells disappear, and the board updates.

If no valid move exists, the game ends.

🚀 Running the Game

Execute the game with:

python3 numberboardgame.py input.txt

The board will be displayed at the start.

Players enter row and column numbers (1-based index) to make a move.

If an invalid move is made, an error message will appear.

The game continues until no more valid moves are available.

🏆 Scoring System

Each move's score is calculated as:

score = (selected cell value) * (number of removed cells)

For example, selecting a cell with value 1 that removes 13 cells adds 1 * 13 = 13 points.

📄 Example Gameplay

Initial Board:
[Displayed grid]

Enter row and column: 2 3
Updated Board:
[Displayed grid]

Current Score: 20
