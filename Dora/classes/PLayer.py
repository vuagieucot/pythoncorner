from classes.Sprite import Sprite
import pygame
from Bas_value import *

class FlashyPlayer(Sprite):
    def __init__(self, screen, l = 10):
        super().__init__(Id = 'player')
        self._r = 30
        self._moves = []
        self._screen =  screen
        self._l = l
        self._max_count = 1
        self._countdown = self._max_count
        self._health = 5
        self._score = 0

    def get_score(self):
        return self._score

    def change_score(self, change):
        self._score += change
        if self._score <= 0:
            self._score = 0

    def reset(self):
        self._moves = []

    def get_health(self):
        return self._health

    def change_health(self, change):
        self._health += change
        if self._health <= 0:
            self._health = 0

    def update(self):
        self._x, self._y = pygame.mouse.get_pos()
        self._moves = [(self._x, self._y)] + self._moves
        if len(self._moves) > self._l:
            self._moves.remove(self._moves[-1])
        self._countdown -= 1
        if self._countdown ==0 and len(self._moves) > 1:
            self._countdown = self._max_count
            self._moves.remove(self._moves[-1])
        self.draw()

    def draw(self):
        for i in range(len(self._moves)):
            x, y = self._moves[i]
            pygame.draw.circle(self._screen, c['red'], (x, y), int(10-i/(self._l/10)))