import math,random

class Sudoku:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
	    self.board
	    self.box_length = int(sqrt(row_length))

    def get_board(self)
'''Returns a 2D python list of numbers, which represents the board'''
    def print_board(self)
        print(curr_board)
'''Displays the board to the console.
This is not strictly required, but it may be useful for debugging purposes.'''
    def valid_in_row(self, row, num):
        for i in curr_board[row]:
            if num == i:
                return False
        return True
'''Determines if num is contained in the given row of the board.'''
    def valid_in_col(self, col, num):
        for i in range(0, curr_board)
            for j in curr_board[col]
                if num == j:
                return False
        return True
'''Determines if num is contained in the given column of the board.'''
    def valid_in_box(self, row_start, col_start, num)
        if  
'''Returns a Boolean value.
Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)'''
    def is_valid(self, row, col, num)
        if curr_board[row][col] != real_board[row][col]:
            return False
        else:
            return True
'''Returns if it is valid to enter num at (row, col) in the board.
This is done by checking the appropriate row, column, and box.'''
    def fill_box(self, row_start, col_start)
'''Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
Uses unused_in_box to ensure no value occurs in the box more than once.'''
    def fill_diagonal(self)
'''Fills the three boxes along the main diagonal of the board.
This is the first major step in generating a Sudoku.
See the Step 1 picture in Sudoku Generation for further explanation'''.
    def fill_remaining(self, row, col)
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self)
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self)
        while self.removed_cells > 0:
            self.removed_cells -= 1
            col = random.randint(0, 9)
            row = random.randrange(10)
            if board[col][row] != 0:
                board[col][row] = 0
            else:
                self.removed_cells += 1
        return board
'''This method removes the appropriate number of cells from the board.
It does so by randomly generating (row, col) coordinates of the board and setting the value to 0.
Note: Be careful not to remove the same cell multiple times. A cell can only be removed once.
This method should be called after generating the Sudoku solution.'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board