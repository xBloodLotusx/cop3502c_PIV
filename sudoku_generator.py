import math, random
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board
        # Returns 2D board
    def print_board(self):
        for i in self.board:
            print(i)
        # Prints board
    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if num == i:
                return False
        return True
        # checks if num is in row of board
    def valid_in_col(self, col, num):
        for i in range(0, 9):
            if num == self.board[i][col]:
                return False
        return True
        # checks if num is in col of board
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if num == self.board[i][j]:
                    return False
        return True
        # checks if num is in box
    def is_valid(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row_start, col_start, num):
            return True
        return False
        # checks if input value is correct
    def fill_box(self, row_start, col_start):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][j + col_start] = num.pop(random.randrange(len(num)))
        # fills box.

    def fill_diagonal(self):
        for i in range(3):
            self.fill_box(i*3, i*3)
        # fills diagnol boxes from top left to bottom right

    def fill_remaining(self, row, col):
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

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        while self.removed_cells > 0:
            self.removed_cells -= 1
            col = random.randrange(9)
            row = random.randrange(9)
            if self.board[col][row] != 0:
                self.board[col][row] = 0
            else:
                self.removed_cells += 1
        return self.board
        # Removes cells based on difficulty
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board