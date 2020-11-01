import pygame

class Player:
    def __init__(self, x, y, w, h, c):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=c
        self.vel=3

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.y -= self.vel
        if pressed[pygame.K_DOWN]:
            self.y += self.vel
        if pressed[pygame.K_RIGHT]:
            self.x += self.vel
        if pressed[pygame.K_LEFT]:
            self.x -= self.vel
