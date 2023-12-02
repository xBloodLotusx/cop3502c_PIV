import pygame, sys

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 60)

    screen.fill((255, 255, 255))

    title_surface = start_title_font.render("Sudoku", 0, (0, 0, 255))
    title_rectangle = title_surface.get_rect(
        center=(800 // 2, 120))
    screen.blit(title_surface, title_rectangle)

    mode_surface = mode_font.render("Select Game Mode:", 0, (0, 0, 255))
    mode_rectangle = mode_surface.get_rect(
        center=(400, 320))
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
        center=(200, 450))
    medium_rectangle = medium_surface.get_rect(
        center=(400, 450))
    hard_rectangle = hard_surface.get_rect(
        center=(600, 450))
    
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    return
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
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    board = [[1 for i in range(9)] for j in range(9)]
    print(board)
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)
    
    screen.fill((255, 255, 255))

    draw_board(board, screen)
    pygame.display.flip()

    pygame.time.delay(500)

    board = [[5 for i in range(9)] for j in range(9)]
    draw_board(board, screen)
    pygame.display.flip()
    pygame.time.delay(500)