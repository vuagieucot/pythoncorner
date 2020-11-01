import pygame

class Nobihit:
    def __init__(self, screen, img_path, x_right_start, y_bottom_start, limitx = None, limity = None):
        self._screen = screen
        self._ori = pygame.image.load(img_path)
        self._img = self._ori
        self._rect = self._img.get_rect()
        self._startx = x_right_start
        self._starty = y_bottom_start
        self._x = x_right_start
        self._y = y_bottom_start
        self._limit_x, self._limit_y = limitx, limity
        self._stay = False
        self.id = None

    def change_img(self, img_path):
        self._img = pygame.image.load(img_path)
        self._x, self._y = 750,550
        self._rect = self._img.get_rect(bottomright = (self._x, self._y))

    def reset(self):
        self._x = self._startx
        self._y = self._starty
        self._stay = False
        self._img = self._ori
        self._rect = self._img.get_rect()

    def update(self):
        if self._img and self._rect:
            self._screen.blit(self._img, self._rect)

    def scale(self, sur, w, h):
        return pygame.transform.scale(sur, (w,h))

    def stop(self):
        return self._stay