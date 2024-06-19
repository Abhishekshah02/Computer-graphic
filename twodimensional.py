import pygame 
import sys
import math

pygame.init()

#width, height = 800, 900
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Two dimensional transformation")

pink=(255, 192, 203)
yellow=(255,255,0)
black= (0, 0, 0)
violet=(238, 130, 238)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
purple=(128, 0, 128)

def draw_line(x,y,x1,y1,dx,dy,sx,sy):
    pygame.draw.line(screen,white, (x,y),(x1,y1) ,1)
    translated_x = x + dx
    translated_y = y + dy
    translated_x1 = x1 + dx
    translated_y1 = y1 + dy
    pygame.draw.line(screen,red, (translated_x,translated_y),(translated_x1,translated_y1) ,1)

    scaled_x=x*sx
    scaled_y=y*sy
    scaled_x1=x1*sx
    scaled_y1=y1*sy

    pygame.draw.line(screen,green, (x,y),(scaled_x1,scaled_y1) ,1)
    # pygame.draw.line(screen,violet, (scaled_x,scaled_y),(scaled_x1,scaled_y1) ,1)

    angle=30
        # x2=x*math.cos(math.radians(angle))
        # y2=y*math.cos(math.radians(angle))
        # pygame.draw.line(screen,violet, (x,y),(x2,y2) ,1)
    rad_angle = math.radians(angle)
    rotated_x = x * math.cos(rad_angle) - y * math.sin(rad_angle)
    rotated_y = x * math.sin(rad_angle) + y * math.cos(rad_angle)
    rotated_x1 = x1 * math.cos(rad_angle) - y1 * math.sin(rad_angle)
    rotated_y1 = x1 * math.sin(rad_angle) + y1 * math.cos(rad_angle)
    
    pygame.draw.line(screen, violet, (x, y), (rotated_x, rotated_y), 1)
    pygame.draw.line(screen, violet, (x1, y1), (rotated_x1, rotated_y1), 1)
    pygame.draw.line(screen, violet, (rotated_x,rotated_y), (rotated_x1, rotated_y1), 1)

def main():
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

       
        screen.fill(black)
        
        draw_line(200,200,450,450,10,10,0.75,0.75)

        pygame.display.flip()

if __name__=="__main__":
    main()

