# Sudoku Solver

This Python application is a simple Sudoku solver implemented using the Tkinter library. The solver generates Sudoku puzzles of varying difficulty levels (Easy, Medium, and Hard) and provides functionality to check whether the user's solution is correct.

## Features
- **Grid Generation:** The application can generate new Sudoku grids with different difficulty levels.
- **Grid Solving:** The solver employs a backtracking algorithm to find a solution to the generated Sudoku grid.
- **Solution Checking:** Users can check whether their entered solution is correct.

## Usage
1. Run the script `main.py`.
2. The application window will appear with an initially generated Sudoku grid.
3. To generate a new grid, click on the "Easy," "Medium," or "Hard" buttons.
4. To check the solution, click on the "Check Solution" button.
5. The status of the solution will be displayed at the bottom of the window.

## How to Play
1. Click on the empty cells to select them.
2. Enter a number from 1 to 9 using the keyboard.
3. To clear a cell, click on it and press the 'Delete' key or backspace.
4. The solution status will be updated accordingly.

## Implementation Details
- The main logic is implemented in the `SudokuGrid` class, which inherits from Tkinter's `Tk` class.
- The solver logic is encapsulated in the `Solve` class, which utilizes a backtracking algorithm to find the solution.
- Different difficulty levels are achieved by hiding a certain percentage of cells in the initial grid.

## Dependencies
- Python 3.11.4
- Tkinter

## Author
Luigi Emiliandra

Feel free to use and modify this Sudoku solver for your own projects! If you have any suggestions or improvements, please let me know.