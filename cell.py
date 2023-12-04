import pygame, sys


class Cell:
    def __init__(self, value, sketched_value, row, col, screen):
        self.value = value
        self.sketched_value = sketched_value
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
            self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw_true(self):
        # The highlight selected cell drawing is in board file, still need to be able to display value in the cell
        black = (0, 0, 0)
        font = pygame.font.Font(None, 66)
        text_surface = font.render(str(self.value), True, black)
        self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))
        pass

    def draw_sketched(self):
        grey = (129, 129, 129)
        font = pygame.font.Font(None, 33)
        current_value = str(self.sketched_value)
        text_surface = font.render(current_value, True, grey)
        self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))

    def clear_sketch(self):
        white = (255, 255, 255)
        font = pygame.font.Font(None, 33)
        current_value = str(self.sketched_value)
        text_surface = font.render(current_value, True, white)
        self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))

    def clear_input_value(self):
        white = (255, 255, 255)
        font = pygame.font.Font(None, 66)
        text_surface = font.render(str(self.value), True, white)
        self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))
        pass
"""
      if self.color == 1:
            grey = (129, 129, 129)
            font = pygame.font.Font(None, 33)
            current_value = str(self.value)
            text_surface = font.render(current_value, True, grey)
            self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))
        if self.color == 2:
            white = (255, 255, 255)
            font = pygame.font.Font(None, 33)
            current_value = str(self.value)
            text_surface = font.render(current_value, True, white)
            self.screen.blit(text_surface, ((self.col - 1) * 600 / 9 + 15, (self.row - 1) * 500 / 9 + 3))
"""


