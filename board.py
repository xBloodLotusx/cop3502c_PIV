from cell import Cell
from sudoku_generator import SudokuGenerator as SG
import pygame
import copy


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_2D_array = []
        self.cell_row = []
        self.selected_cell = None
        self.sudoku_array = None
        self.sudoku_values = None
        self.tru_board = None
        self.board = []

        if self.difficulty == "Easy":
            self.sudoku_array = SG(9, 30)
            self.sudoku_array.fill_values()
            self.tru_board = copy.deepcopy(self.sudoku_array.get_board())
            self.sudoku_array.remove_cells()
            self.sudoku_values = self.sudoku_array.get_board()

        if self.difficulty == "Medium":
            self.sudoku_array = SG(9, 40)
            self.sudoku_array.fill_values()
            self.tru_board = copy.deepcopy(self.sudoku_array.get_board())
            self.sudoku_array.remove_cells()
            self.sudoku_values = self.sudoku_array.get_board()

        if self.difficulty == "Hard":
            self.sudoku_array = SG(9, 50)
            self.sudoku_array.fill_values()
            self.tru_board = copy.deepcopy(self.sudoku_array.get_board())
            self.sudoku_array.remove_cells()
            self.sudoku_values = self.sudoku_array.get_board()

        for i in range(1, 10):
            for j in range(1, 10):
                self.cell_row.append(Cell(self.sudoku_values[i - 1][j - 1], 0, i, j, self.screen))
            self.cell_2D_array.append(self.cell_row)
            self.cell_row = []

    def draw(self):
        # Horizontal lines

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height / 3)), (self.width, (self.height / 3)), 12)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 2) / 3)), (self.width, ((self.height * 2) / 3)), 12)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 3) / 3)), (self.width, ((self.height * 3) / 3)), 12)

        pygame.draw.line(self.screen, (245, 152, 66), (0, self.height / 9), (self.width, self.height / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 2) / 9), (self.width, (self.height * 2) / 9), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 4) / 9), (self.width, (self.height * 4) / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 5) / 9), (self.width, (self.height * 5) / 9), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 7) / 9), (self.width, (self.height * 7) / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 8) / 9), (self.width, (self.height * 8) / 9), 4)
        # VERTICAL LINES

        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=(self.width / 3, 0), end_pos=(self.width / 3, self.height), width=14)
        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=((self.width * 2) / 3, 0), end_pos=((self.width * 2) / 3, self.height), width=14)

        pygame.draw.line(self.screen, (245, 152, 66), (self.width / 9, 0), (self.width / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 2) / 9, 0), ((self.width * 2) / 9, self.height), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 4) / 9, 0), ((self.width * 4) / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 5) / 9, 0), ((self.width * 5) / 9, self.height), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 7) / 9, 0), ((self.width * 7) / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 8) / 9, 0), ((self.width * 8) / 9, self.height), 4)
        pass

    def select(self, row, col):
        if self.selected_cell is not None:
            self.draw()
        self.selected_cell = None
        # Highlights selected cell in red
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * row),
                             ((self.width / 9) * col, (self.height / 9) * row), 3)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * (row - 1)),
                             ((self.width / 9) * col, (self.height / 9) * (row - 1)), 3)

        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * (row - 1)),
                             ((self.width / 9) * (col - 1), (self.height / 9) * row), 3)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * col, (self.height / 9) * (row - 1)),
                             ((self.width / 9) * col, (self.height / 9) * row), 3)

        try:
            self.selected_cell = self.cell_2D_array[row - 1][col - 1]
        except IndexError:
            pass

    def click(self, x, y):
        if 0 < y < 500:
            row = (y // int(500 // 9)) + 1
            col = (x // int(600 // 9)) + 1
            tuple_1 = (col, row)
            return tuple_1
        else:
            return None

    def clear(self):
        self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        if self.selected_cell.value == 0:
            if self.selected_cell.sketched_value != 0:
                self.selected_cell.clear_sketch()
                self.selected_cell.set_sketched_value(value)
                self.selected_cell.draw_sketched()
            if self.selected_cell.sketched_value == 0:
                self.selected_cell.set_sketched_value(value)
                self.selected_cell.draw_sketched()
        if self.selected_cell.value != 0:
            pass

    def place_number(self, sketched_value):
        self.selected_cell.clear_sketch()
        self.selected_cell.set_cell_value(sketched_value)
        self.selected_cell.draw_true()

    def reset_to_original(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.cell_2D_array[i][j].sketched_value != 0:
                    self.cell_2D_array[i][j].clear_sketch()
                    self.cell_2D_array[i][j].set_sketched_value(0)

                    self.cell_2D_array[i][j].clear_input_value()
                    self.cell_2D_array[i][j].set_cell_value(0)
        pass

    def is_full(self):
        capacity = 0
        for rows in range(0, 9):
            for cols in range(0, 9):
                if self.cell_2D_array[rows][cols].value != 0:
                    capacity += 1
                else:
                    pass
        if capacity == 81:
            return True
        else:
            return False

    def update_board(self):
        pass

    def find_empty(self):
        for rows in self.cell_2D_array:
            for cols in rows:
                if cols.value == 0:
                    tuple_2 = (cols.row, cols.col)
                    return tuple_2
                else:
                    pass

    def check_board(self):
        values_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        curr_board = []
        row_list = []
        # Checking each row for winner by using the all function
        for rows in range(0, 9):
            for cols in range(0, 9):
                row_list.append(self.cell_2D_array[rows][cols].value)
            curr_board.append(row_list)

        for i in range(0, 9):
            for j in range(0, 9):
                if curr_board[i][j] == str(self.tru_board[i][j]) or int(self.tru_board[i][j]):
                    pass
                else:
                    return False
        return True

        # if any row or col returns false it means it's not a solution and is an automatic False
