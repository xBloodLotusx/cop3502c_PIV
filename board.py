from cell import Cell

import pygame, sys

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []

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
        pass

    def click(self, x, y):
        pass

    def clear(self):
        Cell.set_cell_value(Cell, None)
        Cell.set_sketched_value(Cell, None)