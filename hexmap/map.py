import pygame
from Hexagon import HexagonGrid
from Hexagon import BLACK, DARK_GREY, OFF_WHITE, DARK_BEIGE, DARK_MAGENTA, MAROON, FOREST_GREEN

RADIUS = 20
HEXAGON_SIZE = 10

def update_hexagon_state(hexagon):
    # Update the state of a hexagon in pygame
    # Your code here to update the state of the hexagon
    pass

def update_screen(screen, hexagons):
    screen.fill(DARK_GREY)  # Clear the screen with white color
    for hexagon in hexagons.values():
        vertices = hexagon.get_vertices(HEXAGON_SIZE)
        shifted_vertices = [(x + screen.get_width() / 2, y + screen.get_height() / 2) for x, y in vertices]
        pygame.draw.polygon(screen, hexagon.color, shifted_vertices, 0)
        pygame.draw.polygon(screen, BLACK, shifted_vertices, 1)
        
    return screen

def main():
    grid = HexagonGrid(RADIUS)
    hexagons = grid.hexagons

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the clicked hexagon and update its state
                mouse_pos = pygame.mouse.get_pos()
                for hexagon in hexagons:
                    if hexagon.contains_point(mouse_pos):                        
                        update_hexagon_state(hexagon)
                        break
        
        screen = update_screen(screen, hexagons)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()

