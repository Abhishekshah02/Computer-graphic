import pygame 
import sys

pygame.init()

#width, height = 800, 900
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Midpoint circle drawing Algorithm")

pink=(255, 192, 203)
yellow=(255,255,0)
black= (0, 0, 0)
violet=(238, 130, 238)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
purple=(128, 0, 128)


def draw_circle_midpoint(x1,y1,r):

    x=0
    y=r
    p=1-r

    while(x<=y):
        screen.set_at((x1+y,y1+x),violet)
        screen.set_at((x1+x,y1+y),red)
        screen.set_at((x1-x,y1+y),green)
        screen.set_at((x1+y,y1-x),white)
        screen.set_at((x1-x,y1-y),blue)
        screen.set_at((x1-y,y1-x),yellow)
        screen.set_at((x1+x,y1-y),purple)
        screen.set_at((x1-y,y1+x),pink)

        x=x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1
        


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(black)

        draw_circle_midpoint(200,200,100)

        pygame.display.flip()

if __name__=="__main__":
    main()

