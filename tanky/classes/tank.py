import pygame
import glob
import random

tank_imgs = glob.glob('img/tanks/tank*.png')
tanks = [pygame.image.load(tank_addr) for tank_addr in tank_imgs]
bullets = {
    'beam_bullet': [pygame.image.load('img/beam_bullet.png'), pygame.image.load('img/explosion.png')]
}

class Tank:
    def __init__(self, screen, id, x=0, y=0):
        self._screen = screen
        self._ori_img = tanks[id]
        self._an = 0
        self._i = 1
        self._del_rot = 1
        self._cur_del = self._del_rot
        self._img = self._ori_img
        self._x = x
        self._y = y
        self._rect = self._img.get_rect()
        self._vel = 3
        self._bullet = []
        self._Modes = ['beam_bullet', 'flame_carpet', 'multi_beam']
        self._mode = 0
        self._tars = [pygame.image.load('img/target.png'),
                      pygame.image.load('img/carpettarget.png'),
                      pygame.image.load('img/multitarget.png')]
        self._tar = self._tars[0]
        self._tar_rect = self._tar.get_rect()

    def change_mode(self):
        self._mode += 1
        if self._mode == len(self._Modes):
            self._mode = 0

    def shoot(self, target):
        self._bullet.append(Beam(self._screen, self.get_center(), target))

    def get_center(self):
        return self._x+40, self._y+40

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self._x -= self._vel
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self._x += self._vel
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self._y -= self._vel
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self._y += self._vel
        self._rect.center = (self._x+40, self._y+40)

    def targetsign(self):
        self._tar = self._tars[self._mode]
        self._tar_rect = self._tar.get_rect()
        mouse = pygame.mouse.get_pos()
        self._tar_rect.center = mouse
        self._screen.blit(self._tar, self._tar_rect)

    def update(self):
        self.move()
        self._cur_del -= 1
        if self._cur_del == 0:
            self._an += 2*self._i
            if self._an >= 360 or self._an <= -360:
                self._i = random.choice([1,-1])
                self._an = 0
            self._cur_del = self._del_rot
            x, y = self._rect.center
            self._img = pygame.transform.rotate(self._ori_img, self._an)
            self._rect = self._img.get_rect(center = (x,y))

        self._screen.blit(self._img, self._rect)

        if self._bullet:
            for bullet in self._bullet:
                bullet.update()
                if bullet.reach():
                    self._bullet.remove(bullet)

        self.targetsign()

class Bullet:
    _id = None
    def __init__(self, screen, tank):
        self._screen = screen
        self._x, self._y = tank

    def blit(self):
        pass

class Beam(Bullet):
    _id = 'beam_bullet'
    def __init__(self, screen, tank, target):
        super().__init__(screen, tank)
        self._img, self._explode = bullets[self._id]
        self._vel = 15
        self._tar_x, self._tar_y = target
        if self._tar_y != self._y:
            self._diry = (self._tar_y - self._y) / abs(self._tar_y - self._y)
        else:
            self._diry = 0
        if self._tar_x != self._x:
            self._dirx = (self._tar_x - self._x) / abs(self._tar_x - self._x)
        else:
            self._dirx = 0
        self._rect = self._img.get_rect(center = (self._x, self._y))
        self._reach = False
        self._after = 10

    def blit(self):
        self._screen.blit(self._img, self._rect)

    def reach(self):
        return self._reach

    def update(self):
        if abs(self._x - self._tar_x)>=10:
            self._x += self._vel*self._dirx
        if abs(self._y - self._tar_y)>=10:
            self._y +=self._vel*self._diry
        if abs(self._x - self._tar_x)<=10 and abs(self._y - self._tar_y)<=10:
            self._img=self._explode
            self._after -= 1
        if self._after == 0:
            self._reach = True
        self._rect = self._img.get_rect(center = (self._x, self._y))
        self.blit()