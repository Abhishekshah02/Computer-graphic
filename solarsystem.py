import pygame
import sys
import math

pygame.init()

RED=(255,0,0)
Black=(0,0,0)
White=(255,255,255)
pink=(255, 192, 203)
yellow=(255,255,0)
black= (0, 0, 0)
violet=(238, 130, 238)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
purple=(128, 0, 128)


screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Solar syatem")


def draw_solar_system():

    pygame.draw.circle(screen, white, (200, 200), 80, 1)
    pygame.draw.circle(screen, white, (200, 200), 90, 1)
    pygame.draw.circle(screen, white, (200, 200), 100, 1)
    pygame.draw.circle(screen, white, (200, 200), 110, 1)
    pygame.draw.circle(screen, white, (200, 200), 120, 1)
    pygame.draw.circle(screen, white, (200, 200), 140, 1)
    pygame.draw.circle(screen, white, (200, 200), 160, 1)
    
    
    pygame.draw.circle(screen, yellow, (200, 200), 50) 
    
    
    pygame.draw.circle(screen, red, (200 + 80, 200), 5)  
    pygame.draw.circle(screen, pink, (200 + 90, 200), 5)
    pygame.draw.circle(screen, white, (200 + 100, 200), 5)
    pygame.draw.circle(screen, blue, (200 + 110, 200), 5)
    pygame.draw.circle(screen, green, (200 + 120, 200), 5)
    pygame.draw.circle(screen, purple, (200 + 140, 200), 5)
    
    


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_solar_system()

        pygame.display.flip()

main()