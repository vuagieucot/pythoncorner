import pygame
from pygame.locals import *
from classes.TextObject import RunningText

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
text = RunningText(screen, 'I am Iron Man. I will be and always be Iron Man',
                   25, 'fonts/comic.ttf', (255,0,0), (10,300))

def main():
    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        text.blit()

        pygame.display.update()
        clock.tick(60)

main()