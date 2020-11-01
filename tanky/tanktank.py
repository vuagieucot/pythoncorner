import pygame
import sys
import random

from pygame.locals import *
from classes.tank import Tank
from VALUES import *

class Game:
    def __init__(self, width=w, height=h):
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Tanky Tank')
        self._clock = pygame.time.Clock()

        self._p = Tank(self._screen, random.choice([0,1,2,3,4]))

    def redrawScreen(self):
        self._screen.fill(colors['white'])
        self._p.update()

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self._p.shoot((event.pos))
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        pass
                if event.type == KEYDOWN:
                    if event.key == K_LSHIFT:
                        self._p.change_mode()

            self.redrawScreen()

            pygame.display.update()
            self._clock.tick(60)

def main():
    game = Game()
    game.mainloop()

if __name__ == '__main__':
    main()

