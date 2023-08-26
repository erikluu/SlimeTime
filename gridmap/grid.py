import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 100  # Number of rows and columns in the grid
GRID_WIDTH = 10  # Width of each grid cell
GRID_HEIGHT = 10  # Height of each grid cell
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH + 150
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BEIGE = (200, 173, 127)
DARK_BEIGE = (150, 123, 77) 

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Painting Grid")

# Create a 2D array to store the colors of the grid cells
grid_colors = [[LIGHT_BEIGE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Color selector
color_selector = pygame.Surface((200, SCREEN_HEIGHT))
color_selector.fill(DARK_BEIGE)

color_options = [BLACK, WHITE, RED, GREEN, BLUE]
current_color = WHITE
color_buttons = [
    pygame.Rect(SCREEN_WIDTH - 130, 50 + i * 60, 40, 40) for i in range(len(color_options))
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(color_buttons):
                    if button.collidepoint(mouse_pos) and i != 4:
                        current_color = color_options[i]

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            x, y = event.pos
            row = y // GRID_HEIGHT
            col = x // GRID_WIDTH
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                grid_colors[row][col] = current_color

    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(
                screen,
                grid_colors[row][col],
                (col * GRID_WIDTH, row * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT),
            )

    # Draw color selector
    for i, button in enumerate(color_buttons):
        pygame.draw.rect(screen, color_options[i], button)

    pygame.draw.rect(screen, WHITE, color_buttons[color_options.index(current_color)], 3)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
