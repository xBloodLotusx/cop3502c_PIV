import pygame, sys
# Need to determine constants for each part of the game display

from board import Board

pygame.init()
screen = pygame.display.set_mode(size=(600, 600))
pygame.display.set_caption("Welcome to Sudoku")

screen.fill(color=(255, 255, 245))

board = Board(width=600, height=500, screen=screen, difficulty="Hard")
board.draw()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


