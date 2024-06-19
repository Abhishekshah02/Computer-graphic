import pygame 
import sys

pygame.init()

#width, height = 800, 900
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Bresenham line drawing Algorithm")

White=(255,255,255)
BLACK=(0,0,0)

def draw_line_dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if (x2>x1):
        ls=1
    else:
        ls=-1
    if (y2>y1):
        ly=1
    else:
        ly=-1
    x ,y =x1, y1
    if(dx>dy):
        p=2*dy-dx
        while(x!=x2):
            if(p<0):
                x=x+ls
                p=p+2*dy
            else:
                p=p+2*dx-2*dy
                x=x+ls
                y=y+ly
            screen.set_at((x,y),"black")
    
    else:
        p=2*dx-dy
        while(y!=y2):
            if(p<0):
                y=y+ly
                p=p+2*dx
            else:
                y=y+ly
                x=x+ls
                p=p+2*dx-2*dy
            screen.set_at((x,y),"black")


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill("white")

        draw_line_dda(100,100,700,500)

        pygame.display.flip()

if __name__=="__main__":
    main()

