import pygame
import sys

from samples.network import Network

pygame.init()
width,height = 500,500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('client')
clock = pygame.time.Clock()

def redraw(win,p,p2,p3):
    win.fill((255,255,255))
    p3.draw(win)
    p2.draw(win)
    p.draw(win)
    pygame.display.update()
    clock.tick(60)

def main():
    n=Network()
    p = n.getData()
    while True:
        p2, p3 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        p.move()
        redraw(win, p, p2, p3)


sys.exit(main())