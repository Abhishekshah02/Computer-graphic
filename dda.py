import pygame 
import sys

pygame.init()

#width, height = 800, 900
screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("DDA line drawing Algorithm")

White=(255,255,255)
BLACK=(0,0,0)

def draw_line_dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2=y1
    steps=max(abs(dx),abs(dy))
    x_increment=dx/ steps
    y_increment=dy/ steps
    x=x1
    y=y1
    for i in range(steps):
        screen.set_at((round(x),round(y)),BLACK)
        x+=x_increment
        y+=y_increment

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(White)

        draw_line_dda(20,20,100,100)

        pygame.display.flip()

if __name__=="__main__":
    main()

    
    #conclusion floating point error-   pygame ko bare ma aani process ko bare ma 