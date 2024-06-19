import pygame 
import sys

pygame.init()

#width, height = 800, 900
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Midpoint Ellipse drawing Algorithm")

pink=(255, 192, 203)
yellow=(255,255,0)
black= (0, 0, 0)
violet=(238, 130, 238)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
purple=(128, 0, 128)


def draw_ellipse_midpoint(xc,yc,rx,ry):

    x=0
    y=ry
    p1=pow(ry,2)-pow(rx,2)*ry+1/4*pow(rx,2)

    while(2*pow(ry,2)*x<=2*pow(rx,2)*y):
        screen.set_at((xc+x,yc+y),violet)
        screen.set_at((xc-x,yc+y),red)
        screen.set_at((xc-x,yc-y),green)
        screen.set_at((xc+x,yc-y),white)
       

        
        if(p1<0):
            x=x+1
            y=y
            p1=p1+2*pow(ry,2)*x+pow(ry,2)
        else:
            x=x+1
            y=y-1
            p1=p1+2*pow(ry,2)*x-2*pow(rx,2)*y+pow(ry,2)
    
    p2=round(pow(ry,2)*pow((x+1/2),2)+pow(rx,2)*pow((y-1),2)-pow(rx,2)*pow(ry,2))
    
    while(y>0):

        screen.set_at((xc+x,yc+y),blue)
        screen.set_at((xc+x,yc-y),yellow)
        screen.set_at((xc-x,yc-y),purple)
        screen.set_at((xc-x,yc+y),pink)
        if(p2>0):
            x=x
            y=y-1
            p2=p2-2*pow(rx,2)*y+pow(rx,2)
        else:
            x=x+1
            y=y-1
            p2=p2+2*pow(ry,2)*x-2*pow(rx,2)*y+pow(rx,2)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(black)

        draw_ellipse_midpoint(200,200,100,50)

        pygame.display.flip()

if __name__=="__main__":
    main()

