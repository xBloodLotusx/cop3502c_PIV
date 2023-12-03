import pygame, sys


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        if self.value == 0:
            pass
        else:
            black = (0, 0, 0)
            font = pygame.font.Font(None, 66)
            current_value = str(self.value)
            text_surface = font.render(current_value, True, black)
            self.screen.blit(text_surface, ((self.row - 1) * 600 / 9 + 15, (self.col - 1) * 500 / 9 + 3))

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        # The highlight selected cell drawing is in board file, still need to be able to display value in the cell
        black = (0, 0, 0)
        font = pygame.font.Font(None, 66)
        text_surface = font.render(self.value, True, black)
        self.screen.blit(text_surface, ((self.row - 1) * 600 / 9 + 15, (self.col - 1) * 500 / 9 + 3))
        pass

