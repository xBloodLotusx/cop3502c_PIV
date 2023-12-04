import pygame, sys
from board import Board as BD

global difficulty_var
global restart_rectangle
global reset_rectangle
global exit_rectangle


def draw_game_start(screen, height, width):
    start_title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 60)

    screen.fill((255, 255, 255))

    title_surface = start_title_font.render("Sudoku", 0, (0, 0, 255))
    title_rectangle = title_surface.get_rect(
        center=(width // 2, 120))
    screen.blit(title_surface, title_rectangle)

    mode_surface = mode_font.render("Select Game Mode:", 0, (0, 0, 255))
    mode_rectangle = mode_surface.get_rect(
        center=(width // 2, 320))
    screen.blit(mode_surface, mode_rectangle)

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill((0, 0, 255))
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill((0, 0, 255))
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill((0, 0, 255))
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(width // 2 - 200, 450))
    medium_rectangle = medium_surface.get_rect(
        center=(width // 2, 450))
    hard_rectangle = hard_surface.get_rect(
        center=(width // 2 + 200, 450))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    global difficulty_var
                    difficulty_var = "Easy"
                    return difficulty_var
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty_var = "Medium"
                    return difficulty_var
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty_var = "Hard"
                    return difficulty_var
        pygame.display.update()


def draw_game_buttons(screen, height, width):
    button_font = pygame.font.Font(None, 40)

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((0, 0, 255))
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((0, 0, 255))
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((0, 0, 255))
    exit_surface.blit(exit_text, (10, 10))

    global restart_rectangle
    global reset_rectangle
    global exit_rectangle

    reset_rectangle = reset_surface.get_rect(
        center=(width // 2 - 200, 550))
    restart_rectangle = restart_surface.get_rect(
        center=(width // 2, 550))
    exit_rectangle = exit_surface.get_rect(
        center=(width // 2 + 200, 550))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()


def draw_board(board, screen):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    HEIGHT = 80
    WIDTH = 80
    MARGIN = 8
    font = pygame.font.Font(None, 100)

    screen.fill(BLACK)

    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                color = GREEN
            x_cord = (MARGIN + WIDTH) * column + MARGIN
            y_cord = (MARGIN + HEIGHT) * row + MARGIN
            pygame.draw.rect(screen, WHITE, (x_cord, y_cord, WIDTH, HEIGHT))
            cell_value = str(board[row][column])
            text_surface = font.render(cell_value, True, BLACK)
            screen.blit(text_surface, (x_cord + 20, y_cord + 10))


if __name__ == '__main__':
    while True:
        pygame.init()
        height = 600
        width = 600
        screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption("Sudoku")

        draw_game_start(screen, height, width)

        screen.fill((255, 255, 255))

        board = BD(600, 500, screen, difficulty_var)
        board.draw()
        pygame.display.update()
        draw_game_buttons(screen, height, width)

        loop_var = True
        while loop_var:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rectangle.collidepoint(event.pos):
                        pass
                    elif restart_rectangle.collidepoint(event.pos):
                        loop_var = False
                        break
                    elif exit_rectangle.collidepoint(event.pos):
                        sys.exit()
                    else:
                        board.click()
                        pass

            pygame.display.update()
