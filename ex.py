import pygame
import sys

pygame.init()

# Set up display
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Box Drawing Example")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK) # Fill the screen with black

    # Draw a rectangle (surface, color, rect, width)
    # Rect format: (x, y, width, height)
    pygame.draw.rect(screen, RED, pygame.Rect(100, 100, 200, 100), 2)

    pygame.display.flip() # Update the display
