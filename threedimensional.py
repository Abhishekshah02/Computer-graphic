import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame 3D Transformation Demo')

# Function to perform 3D rotation around the y-axis
def rotate_y(points, angle):
    rotated_points = []
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = x * math.sin(angle) + z * math.cos(angle)
        rotated_points.append((new_x, y, new_z))
    return rotated_points

# Define a cube (vertices and edges)
cube_vertices = [
    (-50, -50, -50),
    (-50, 50, -50),
    (50, 50, -50),
    (50, -50, -50),
    (-50, -50, 50),
    (-50, 50, 50),
    (50, 50, 50),
    (50, -50, 50)
]

cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Initial rotation angle
angle_y = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Rotate cube around y-axis
    cube_vertices_rotated = rotate_y(cube_vertices, angle_y)
    angle_y += 0.001

    # Project 3D points to 2D (simple perspective projection)
    projected_points = []
    for vertex in cube_vertices_rotated:
        distance = 200
        scale = distance / (distance - vertex[2])
        x = vertex[0] * scale + SCREEN_WIDTH / 2
        y = -vertex[1] * scale + SCREEN_HEIGHT / 2
        projected_points.append((x, y))

    # Draw edges of the cube
    for edge in cube_edges:
        point1 = projected_points[edge[0]]
        point2 = projected_points[edge[1]]
        pygame.draw.line(screen, WHITE, point1, point2, 2)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit() 
