import tkinter as tk
import random

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
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class SudokuGrid(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Sudoku Solver')

        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.ans = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.solved_msg, self.not_solved_msg, self.incorrect_msg = 'Solved', 'Not Solved', 'Incorrect'
        self.status = tk.StringVar()

        self.width, self.height = 270, 340
        self.geometry(f'{self.width}x{420}')

        self.create_grid()

        self.new_grid_easy()

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
                

        tk.Label(self, text = 'Generate New Grid', font = ('Helvetica 11 bold')).place(x = 60, y = 290)
        tk.Button(self, text = 'Easy', command = self.new_grid_easy, bg = 'black', fg = 'white' ).place(x = 20, y = 320)
        tk.Button(self, text = 'Medium', command = self.new_grid_med, bg = 'black', fg = 'white').place(x = 103, y = 320)
        tk.Button(self, text = 'Hard', command = self.new_grid_hard, bg = 'black', fg = 'white').place(x = 210, y = 320)
        tk.Button(self, text = 'Check Solution', command = self.check, bg = 'black', fg = 'white').place(x = 85, y = 360)
        tk.Label(self, textvariable = self.status, fg='grey', font = ('Helvetica 9 bold')).place(x = self.width/3.5, y = self.height+50)

    def worst_case(self, event):
        for row in range(GRID):
            for col in range(GRID):
                if main_grid[row][col].get() == '':
                    continue
                if len(main_grid[row][col].get()) > 1 or main_grid[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_grid[row][col].set('')

    def new_grid_easy(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solution_easy()
        self.status.set(f'Status: {self.not_solved_msg}')

    def new_grid_med(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solution_med()
        self.status.set(f'Status: {self.not_solved_msg}')

    def new_grid_hard(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solution_hard()
        self.status.set(f'Status: {self.not_solved_msg}')

    def check(self):
        if self.grid_correct():
            self.status.set(f'Status: {self.solved_msg}')
        else:
            self.status.set(f'Status: {self.incorrect_msg}')

    def grid_correct(self):
        for row in range(GRID):
            for col in range(GRID):
                if main_grid[row][col].get() != self.ans[row][col]:
                    return False
        return True

    def clear_grid(self):
        for row in range(GRID):
            for col in range(GRID):
                main_grid[row][col].set('')

    def randomize_top_row(self):
        numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        randomize = random.sample(numbs, len(numbs))

        for i in range(GRID):
            main_grid[0][i].set(randomize[i])

    def solve_grid(self):
        solve = Solve()

    def save_grid(self):
        for row in range(GRID):
            for col in range(GRID):
                self.ans[row][col] = main_grid[row][col].get()

    def hide_solution_easy(self):
        cc = 63
        for col in range(GRID):
            for row in range(GRID):
                r = random.randint(0, 100)
                if r < cc:
                    main_grid[row][col].set('')

    def hide_solution_med(self):
        cc = 77
        for col in range(GRID):
            for row in range(GRID):
                r = random.randint(0, 100)
                if r < cc:
                    main_grid[row][col].set('')

    def hide_solution_hard(self):
        cc = 87
        for col in range(GRID):
            for row in range(GRID):
                r = random.randint(0, 100)
                if r < cc:
                    main_grid[row][col].set('')


class Solve():

    def __init__(self):
        self.set_all_zero()
        self.game_solve()

    def set_all_zero(self):
        for row in range(GRID):
            for col in range(GRID):
                if main_grid[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_grid[row][col].set(0)

    def game_solve(self, i=0, j=0):
        i, j =  self.load_cell(i, j)

        if i == -1:
            return True
        for n in range(1, 10):
            if self.valid(i, j, n):
                main_grid[i][j].set(n)
                if self.game_solve(i, j):
                    return True
                
                main_grid[i][j].set(0)
        return False
    
    def load_cell(self, i, j):
        for row in range(i, GRID):
            for col in range(j, GRID):
                if main_grid[row][col].get() == '0':
                    return row, col
                
        for row in range(0, GRID):
            for col in range(0, GRID):
                if main_grid[row][col].get() == '0':
                    return row, col
                
        return -1, -1

    def valid(self, row, col, n):
        for i in range(GRID):
            if main_grid[row][i].get() == str(n):
                return False
            
        for i in range(GRID):
            if main_grid[i][col].get() == str(n):
                return False

        sec_top_x, sec_top_y = 3*int((row/3)), 3*int((col/3))
        for row in range(sec_top_x, sec_top_x+3):
            for col in range(sec_top_y, sec_top_y+3):
                if main_grid[row][col].get() == str(n):
                    return False
        
        return True

if __name__ == '__main__':
    app = SudokuGrid()
    app.mainloop()
