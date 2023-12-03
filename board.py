from cell import Cell

import pygame, sys

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_2D_array = []
        self.cell_row = []
        self.selected_cell = None

        for i in range(1, 10):
            for j in range(1, 10):
                self.cell_row.append(Cell(0, i, j, self.screen))
            self.cell_2D_array.append(self.cell_row)
            self.cell_row = []

    def draw(self):
        # Horizontal lines

        pygame.draw.line(self.screen, (245, 152, 66), (0, (self.height / 3)), (self.width, (self.height / 3)), 14)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 2) / 3)), (self.width, ((self.height * 2) / 3)), 14)
        pygame.draw.line(self.screen, (245, 152, 66), (0, ((self.height * 3) / 3)), (self.width, ((self.height * 3) / 3)), 14)

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
        self.selected_cell = None
        # Highlights selected cell in red
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * row),
                         ((self.width / 9) * col, (self.height / 9) * row), 7)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * (row - 1)),
                         ((self.width / 9) * col, (self.height / 9) * (row - 1)), 7)

        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * (col - 1), (self.height / 9) * (row - 1)),
                         ((self.width / 9) * (col - 1), (self.height / 9) * row), 7)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.width / 9) * col, (self.height / 9) * (row - 1)),
                         ((self.width / 9) * col, (self.height / 9) * row), 7)

        self.selected_cell = self.cell_2D_array[row][col]

    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            x = x // (self.width / 9) + 1
            y = y // (self.height / 9) + 1
            tuple_1 = (x, y)
            return tuple_1
        else:
            return None

    def clear(self):
        self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.selected_cell.draw()

    def place_number(self, value):
        self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        pass

    def is_full(self):
        capacity = 0
        for rows in self.cell_2D_array:
            for cols in rows:
                if self.cell_2D_array[rows][cols] != 0:
                    capacity += 1
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
        list_of_cell_values = []
        # Checking each row for winner by using the all function
        for rows in range(0, 9):
            for cols in range(0, 9):
                list_of_cell_values.append(self.cell_2D_array[rows][cols].value)
            if all(value in list_of_cell_values for value in values_to_check):
                pass
            else:
                return False
            list_of_cell_values = []

        # checking each col for winner by using the all function
        for cols in range(0, 9):
            for rows in range(0, 9):
                list_of_cell_values.append(self.cell_2D_array[rows][cols].value)
            if all(value in list_of_cell_values for value in values_to_check):
                pass
            else:
                return False
        # if any row or col returns false it means it's not a solution and is an automatic False
        return True
