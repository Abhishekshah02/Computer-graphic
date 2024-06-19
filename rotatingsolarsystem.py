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

screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Rotating solar system")

angle=0

font = pygame.font.SysFont(None, 24)

def draw_solar_system():
    
    screen.fill(black)

    pygame.draw.circle(screen, white, (280, 250), 100, 1)
    pygame.draw.circle(screen, white, (280, 250), 120, 1)
    pygame.draw.circle(screen, white, (280, 250), 140, 1)
    pygame.draw.circle(screen, white, (280, 250), 160, 1)
    pygame.draw.circle(screen, white, (280, 250), 180, 1)
    pygame.draw.circle(screen, white, (280, 250), 200, 1)
    pygame.draw.circle(screen, white, (280, 250), 220, 1)
    pygame.draw.circle(screen, white, (280, 250), 240, 1)
    
    pygame.draw.circle(screen, yellow, (280, 250), 50) 
    
def draw_planet(angle,radius,color,name):

    center = (280,250)
    x = center[0] + int(radius * math.cos(math.radians(angle)))
    y = center[1] + int(radius * math.sin(math.radians(angle)))
    
    pygame.draw.circle(screen, color, (x, y), 10)
     
    planet_name = font.render(name, True, white)
    screen.blit(planet_name, (x - planet_name.get_width() // 2, y + 15))


def main():
    global angle
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        draw_solar_system()
        draw_planet(angle, 100, red,"Mercury")
        draw_planet(angle + 45, 120, pink,"Venus")
        draw_planet(angle + 90, 140, white,"Earth")
        draw_planet(angle + 135, 160, blue,"March")
        draw_planet(angle + 180, 180, green,"Jupiter")
        draw_planet(angle + 225, 200, purple,"Saturn")
        draw_planet(angle + 270, 220, violet,"Uranus")
        draw_planet(angle + 315, 240, red,"Neptun8")

        pygame.display.flip()
        
        # Rotate the circle
        angle += 1
        if angle >= 360:
            angle = 0

        # Control the frame rate
        pygame.time.Clock().tick(120)

main()


