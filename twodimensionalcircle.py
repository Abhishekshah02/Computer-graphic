import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Circle Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
yellow=(255,255,0)
black= (0, 0, 0)
violet=(238, 130, 238)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
purple=(128, 0, 128)

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Calculate circle position
    radius = 100
    center = (width // 2, height // 2)
    x = center[0] + int(radius * math.cos(math.radians(angle)))
    y = center[1] + int(radius * math.sin(math.radians(angle)))

    # Draw the circle
    pygame.draw.circle(screen, BLACK, (x, y), 20)
    pygame.draw.circle(screen, red, (x, y), 30,1)
    pygame.draw.circle(screen, green, (x, y), 40,1)
    pygame.draw.circle(screen, blue, (x, y), 50,1)

    # Update the display
    pygame.display.flip()

    # Rotate the circle
    angle += 1
    if angle >= 360:
        angle = 0

    # Control the frame rate
    pygame.time.Clock().tick(90)

# Quit Pygame
pygame.quit()
sys.exit()


