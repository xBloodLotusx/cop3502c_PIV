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

        pygame.draw.line(self.screen, (245, 152, 66), (0, (500 / 3)), (600, (500 / 3)), 14)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (1000 / 3)), (600, (1000 / 3)), 14)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (1500 / 3)), (600, (1500 / 3)), 14)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (500 / 3) / 3), (600, (500 / 3) / 3), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (1000 / 3) / 3), (600, (1000 / 3) / 3), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (2000 / 3) / 3), (600, (2000 / 3) / 3), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (2500 / 3) / 3), (600, (2500 / 3) / 3), 4)

        pygame.draw.line(self.screen, (245, 152, 66), (0, (3500 / 3) / 3), (600, (3500 / 3) / 3), 4)
        pygame.draw.line(self.screen, (245, 152, 66), (0, (4000 / 3) / 3), (600, (4000 / 3) / 3), 4)
        # VERTICAL LINES

        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=(200, 0), end_pos=(200, 500), width=14)
        pygame.draw.line(self.screen, color=(245, 152, 66), start_pos=(400, 0), end_pos=(400, 500), width=14)

        pygame.draw.line(self.screen, (245, 152, 66), ((600 / 3) / 3, 0), ((600 / 3) / 3, 500), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((1200 / 3) / 3, 0), ((1200 / 3) / 3, 500), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((2400 / 3) / 3, 0), ((2400 / 3) / 3, 500), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((3000 / 3) / 3, 0), ((3000 / 3) / 3, 500), 4)

        pygame.draw.line(self.screen, (245, 152, 66), ((4200 / 3) / 3, 0), ((4200 / 3) / 3, 500), 4)
        pygame.draw.line(self.screen, (245, 152, 66), ((4800 / 3) / 3, 0), ((4800 / 3) / 3, 500), 4)

        pass

    def select(self, row, col):
        self.cell_2D_array[row][col].draw()
        self.selected_cell = self.cell_2D_array[row][col]

    def click(self, x, y):
        if 0 < x < 600 and 0 < y < 600:
            x = x // (600 / 9) + 1
            y = y // (600 / 9) + 1
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
        pass

    def check_board(self):
        pass
