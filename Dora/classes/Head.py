from classes.Sprite import Sprite
import pygame
import random
from Bas_value import *

heads = {'goda': [pygame.image.load('img/goda.png'), pygame.image.load('img/godahit.png'), 2],
         'dora': [pygame.image.load('img/dora.png'), pygame.image.load('img/dorahit.png'), -2],
         'nobi': [pygame.image.load('img/nobi.png'), pygame.image.load('img/nobihit.png'), 0],
         'suneo': [pygame.image.load('img/suneo.png'), pygame.image.load('img/suneohit.png'), 1],
         'mouse': [pygame.image.load('img/mouse.png'), None, 0]}

specialHeads = {
    'dorami': [pygame.image.load('img/dorami.png'), None, 0]
}

class Head(Sprite):
    def __init__(self, screen, Id, r):
        super().__init__()
        self._screen = screen
        self._id = Id
        self._img, self._hit_img, self._score = heads[Id]
        # self._is = glob.glob('img/{}_*.png'.format(self._id))
        # self._imgs = [pygame.image.load(i) for i in self._is]
        self._rect = self._img.get_rect()
        self._radius = r
        self._r = self._radius
        self._x = random.randrange(200,600)
        self._y = HEIGHT
        self._vx = random.randrange(-8,8)
        self._vy = - random.randrange(28,31)
        self._max_count = 120
        self._count = self._max_count
        self._hit = False
        self._ani = 0
        self._max_del = random.randrange(2,4)
        self._del = self._max_del

    def score(self):
        return self._score

    def hit(self):
        return self._hit

    def get_hit(self):
        self._hit = True
        if not self._id == 'mouse':
            self._img = self._hit_img
        self._vy = -10
        if self._id == 'nobi':
            self._vx = int((WIDTH/2 - self._x)/40)
            self._vy = int((HEIGHT/5 - self._y)/40)

    def update(self):
        # if self._vx < 0:
        #     self._imgs = self._imgs[::-1]
        if not (self._hit and self._id == 'nobi'):
            self._count -= 1
            if self._count == 0:
                self._count = self._max_count
            if self._x - self._radius <= 0 or self._x + self._radius >= WIDTH:
                self._vx = -self._vx
            self._x += self._vx
            self._y += self._vy
            if self._vy < 0:
                self._vy += 1
            else:
                self._del -= 1
                if self._del == 0:
                    self._del = self._max_del
                    self._vy += 1
        else:
            if self._x != WIDTH/2:
                self._x += self._vx
            if abs(WIDTH/2 - self._x) < abs(self._vx):
                self._x = WIDTH/2
            elif self._x != WIDTH/2:
                self._x += abs(WIDTH/2 - self._x)/(WIDTH/2 - self._x)
            if self._y != HEIGHT/5:
                self._y += self._vy
            if abs(HEIGHT/5 - self._y) < abs(self._vy):
                self._y = HEIGHT/5
            elif self._y != HEIGHT/5:
                self._y += abs(HEIGHT/5 - self._y)/(HEIGHT/5 - self._y)
            # print(self._x, self._y)
        self._rect.center = (self._x, self._y)
        # if self._hit:
        self._screen.blit(self._img, self._rect)
        # else:
        #     self._screen.blit(self._imgs[self._ani], self._rect)
        #     self._ani += 1
        #     if self._ani >= len(self._imgs):
        #         self._ani = 0

class SpecialHead(Sprite):
    def __init__(self, screen, Id):
        super().__init__()
        self._screen = screen
        self._img, self._hit_img, self._score = specialHeads[Id]
        self._rect = self._img.get_rect()
    def draw(self):
        self._screen.blit(self._img, self._rect)

class Dorami(SpecialHead):
    def __init__(self, screen, Id='dorami'):
        super().__init__(screen, Id)
        self._right = self._img
        self._left = pygame.transform.flip(self._right, True, False)
        self._x = random.choice([0-self._rect.width, WIDTH])
        if self._x > WIDTH/2:
            self._velx = -10
            self._img = self._right
        else:
            self._velx = 10
            self._img = self._left
        self._y = 0 - self._rect.height
        self._vely = 15
        self._res_del = 3
        self._del = self._res_del

    def collide_mouse(self):
        x, y = pygame.mouse.get_pos()
        return self._rect.collidepoint((x,y))

    def update(self):
        self._y += self._vely
        self._del -= 1
        if self._del == 0:
            self._del = self._res_del
            self._vely -= 1
        self._x += self._velx
        self._rect.x, self._rect.y = self._x, self._y
        self.draw()