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

        self.solved_msg, self.not_solved_msg, self.incorrect_msg = "Solved", "Not Solved", "Incorrect"
        self.status = tk.StringVar()

        self.width, self.height = 270, 340
        self.geometry(f'{self.width}x{420}')

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
                self.grid[row][column].bind('<Motion>', self.worst_case)
                self.grid[row][column].bind('<FocusIn>', self.worst_case)
                self.grid[row][column].bind('<Button-1>', self.worst_case)
                self.grid[row][column].grid(row=row, column=column)
                

        tk.Label(self, text = "Generate New Grid", font = ('Helvetica 11 bold')).place(x = 60, y = 290)
        tk.Button(self, text = 'Easy', command = self.new_grid_easy, bg = 'black', fg = 'white' ).place(x = 20, y = 320)
        tk.Button(self, text = 'Medium', command = self.new_grid_med, bg = 'black', fg = 'white').place(x = 103, y = 320)
        tk.Button(self, text = 'Hard', command = self.new_grid_hard, bg = 'black', fg = 'white').place(x = 210, y = 320)
        tk.Button(self, text = 'Check Solution', command = self.check, bg = 'black', fg = 'white').place(x = 85, y = 360)
        tk.Label(self, textvariable = self.status, fg='grey', font = ('Helvetica 9 bold')).place(x = self.width/4-5, y = self.height+50)

    def worst_case(self, event):
        for row in range(GRID):
            for col in range(GRID):
                if main_grid[row][col].get() == '':
                    continue
                if len(main_grid[row][col].get()) > 1 or main_grid[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_grid[row][col].set('')

    def solve_sudoku(self):
        pass

    def new_grid_easy(self):
        pass

    def new_grid_med(self):
        pass

    def new_grid_hard(self):
        pass

    def check(self):
        pass

if __name__ == "__main__":
    app = SudokuGrid()
    app.mainloop()
