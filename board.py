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
        self.curr_board = []
        # Initializes sudoku solution and values depending on difficulty
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

        # Initializes 81 cell objects in a 2d array, with cell values determined by the generated sudoku
        for i in range(1, 10):
            for j in range(1, 10):
                self.cell_row.append(Cell(self.sudoku_values[i - 1][j - 1], 0, i, j, self.screen))
            self.cell_2D_array.append(self.cell_row)
            self.cell_row = []

    # Draws board outline with every cell
    def draw(self):
        # HORIZONTAL LINES

        # Bolded lines
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height / 3)), (self.width, (self.height / 3)), 12)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 2) / 3)), (self.width, ((self.height * 2) / 3)), 12)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 3) / 3)), (self.width, ((self.height * 3) / 3)), 12)

        # Lines for inner 3by3 grids
        pygame.draw.line(self.screen, (245, 152, 66), (0, self.height / 9), (self.width, self.height / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 2) / 9), (self.width, (self.height * 2) / 9), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 4) / 9), (self.width, (self.height * 4) / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 5) / 9), (self.width, (self.height * 5) / 9), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 7) / 9), (self.width, (self.height * 7) / 9), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height * 8) / 9), (self.width, (self.height * 8) / 9), 4)

        # VERTICAL LINES

        # Bolded lines
        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=(self.width / 3, 0), end_pos=(self.width / 3, self.height), width=14)
        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=((self.width * 2) / 3, 0), end_pos=((self.width * 2) / 3, self.height), width=14)

        # Lines for inner 3by3 grids
        pygame.draw.line(self.screen, (245, 152, 66), (self.width / 9, 0), (self.width / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 2) / 9, 0), ((self.width * 2) / 9, self.height), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 4) / 9, 0), ((self.width * 4) / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 5) / 9, 0), ((self.width * 5) / 9, self.height), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 7) / 9, 0), ((self.width * 7) / 9, self.height), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((self.width * 8) / 9, 0), ((self.width * 8) / 9, self.height), 4)
        pass

    # Creates a selected drawing around cell that was clicked based on row and col provided by the click function, with
    # exception for index error if a click is out of the boards bounds, and whenever the function is called it assigns
    # a selected cell for use in other functions, and re draws the board outline so that the previous selected outlines
    # cannot be seen
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

    # takes x and y coordinates of a click and converts them to a tuple of the column and row the click is located at
    # for the selected function to use.
    def click(self, x, y):
        if 0 < y < 500:
            row = (y // int(500 // 9)) + 1
            col = (x // int(600 // 9)) + 1
            tuple_1 = (col, row)
            return tuple_1
        else:
            return None
    # Calls the sketch function and changes the sketch value when the cell value is not already entered and if there's
    # already a sketch then it clears the previous sketch first which uses the previous sketch values before setting the
    # new sketch value

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

    # Calls when a sketched value is entered and clears the previous sketch and draws the true value.
    def place_number(self, sketched_value):
        self.selected_cell.clear_sketch()
        self.selected_cell.set_cell_value(sketched_value)
        self.selected_cell.draw_true()

    # Resets the entire board back to the original by taking every cell that has a non-zero sketched value being a cell
    # that was interacted by the player and is the only cells that need to be reset
    def reset_to_original(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.cell_2D_array[i][j].sketched_value != 0:
                    self.cell_2D_array[i][j].clear_sketch()
                    self.cell_2D_array[i][j].set_sketched_value(0)

                    self.cell_2D_array[i][j].clear_input_value()
                    self.cell_2D_array[i][j].set_cell_value(0)
        pass

    # Creates a local capacity variable and checks the true value of each cell and waits until all 81 cells are counted
    # up to declare as full, with a boolean value
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

    # Checks if board is solved correctly by comparing every value in the current board to the solution board and
    # returning a boolean value depending on if it's a correct or incorrect board
    def check_board(self):
        self.curr_board = []
        row_list = []
        for rows in range(0, 9):
            for cols in range(0, 9):
                row_list.append(self.cell_2D_array[rows][cols].value)
            self.curr_board.append(row_list)
            row_list = []

        for i in range(0, 9):
            for j in range(0, 9):
                if int(self.curr_board[i][j]) == self.tru_board[i][j]:
                    pass
                else:
                    return False
        return True

