import pygame
import sys

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

# game variable
line_width = 5
grid = []
player = 1
winner = 0
game_over = False

# define font
font = pygame.font.SysFont(None, 40)

# define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# create play again rect
again_rect = pygame.Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

def draw_grid():
    bg_color = (255, 255, 200)
    grid_color = (50, 50, 50)
    screen.fill(bg_color)
    
    for x in range(1, 3):
        pygame.draw.line(screen, grid_color, (0, 100 * x), (300, 100 * x), line_width)
    for y in range(1, 3):
        pygame.draw.line(screen, grid_color, (100 * y, 0), (100 * y,300), line_width)
        
def draw_mark():
    x_pos = 0
    for x in grid:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 35, line_width)
            y_pos += 1
        x_pos += 1
        
def check_winner():
    
    global winner
    global game_over
    
    y_pos = 0
    for x in grid:
        # check column
        if sum(x) == 3:
            winner = 1
            game_over = True
        elif sum(x) == -3:
            winner = 2
            game_over = True
        #check row
        if grid[0][y_pos] + grid[1][y_pos] + grid[2][y_pos] == 3:
            winner = 1
            game_over = True
        if grid[0][y_pos] + grid[1][y_pos] + grid[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1 
        
        # check diagonal
        if (grid[0][0] + grid[1][1] + grid[2][2] == 3) or (grid[2][0] + grid[1][1] + grid[0][2] == 3):
            winner = 1
            game_over = True  
                # check diagonal
        if (grid[0][0] + grid[1][1] + grid[2][2] == -3) or (grid[2][0] + grid[1][1] + grid[0][2] == -3):
            winner = 2
            game_over = True  

def display_winner(winner):
    win_text = "Player " + str(winner) + " wins!"
    win_image = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_image, (screen_width // 2 - 100, screen_height // 2 - 50))
    
    again_text = "Play Again?"
    again_image = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_image, (screen_width // 2 - 80, screen_height // 2 + 10))

def initialize_grid():
    for x in range(3):
        row = [0] * 3
        grid.append(row)

initialize_grid()

while True:
    
    draw_grid()
    draw_mark()
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if grid[cell_x][cell_y] == 0:
                    grid[cell_x][cell_y] = player
                    player *= -1
                    check_winner()
    
    if game_over:
        display_winner(winner)
        # check for mouseclick for play again
        if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        if event.type == pygame.MOUSEBUTTONUP:
                click = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    # reset variable
                    grid = []
                    player = 1
                    winner = 0
                    game_over = False
                    # reset grid
                    initialize_grid()
     
    pygame.display.update()