import tkinter as tk

GRID = 9

main_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

class SudokuGrid(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")

        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.create_grid()

    def create_grid(self):

        for row in range(GRID):
            for column in range(GRID):

                if (row < 3 or row > 5) and (column < 3 or column > 5):
                    color = 'light sky blue'
                elif row in [3,4,5] and column in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'
                
                main_grid[row][column] = tk.StringVar()
                self.grid[row][column] = tk.Entry(self, width = 2, font = ('Arial', 18), bg = color, cursor = 'arrow', borderwidth = 0, highlightcolor = 'red', highlightthickness = 1, highlightbackground = 'black', textvar = main_grid[row][column])
                # self.grid[row][column].bind('<Motion>', self.ammend_grid)
                # self.grid[row][column].bind('<FocusIn>', self.ammend_grid)
                # self.grid[row][column].bind('<Button-1>', self.ammend_grid)
                self.grid[row][column].grid(row=row, column=column)
                

        solve_button = tk.Button(self, text="Solve", command=self.solve_sudoku, font=("Arial", 18))
        solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        # Implement Sudoku solving logic here
        pass

if __name__ == "__main__":
    app = SudokuGrid()
    app.mainloop()
