import pygame
import random
import glob

from classes.PLayer import FlashyPlayer
from classes.Sprite import Sprite
from classes.Head import Head, Dorami
from classes.TextObject import TextObject, RunningText, BlinkText, midText
from classes.res_back import Res_back
from classes.dora_res import Dora_res, Bullet
from Bas_value import *

class Game:
    def __init__(self, w = WIDTH, h = HEIGHT, frame = 60):
        pygame.init()
        self._w = w
        self._h = h
        self._frame = frame
        #self._sec = 1 / frame

        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        pygame.display.set_caption('Doradora slash')

        pygame.display.set_icon(pygame.image.load('img/icon.png'))

        self._sfx_nobihit = pygame.mixer.Sound('sfx/dora_call.wav')

        self._player = FlashyPlayer(self._screen)
        self._gameOver = False

        self._max_count = 120
        self._count_down = self._max_count
        self._balls=[]
        self._specials = []
        self._heart = pygame.image.load('img/life.png')
        self._heart_w = self._heart.get_rect().width
        self._mouseicon = pygame.image.load('img/mouseicon.png')
        self._mouseicon_w = self._mouseicon.get_rect().width
        self._mouses = 0
        self._mouse_hold = False
        self._nobihit = False
        self._nobi_rescue = glob.glob('img/dorarescue*.png')
        self._res_back = Res_back(self._screen, self._nobi_rescue[0], 0, HEIGHT, limitx=WIDTH+100, limity = None)
        self._dora_res = Dora_res(self._res_back, self._screen, self._nobi_rescue[1],
                                  WIDTH+300, HEIGHT, limitx=WIDTH, limity = None)
        self._dora_txt = RunningText(self._screen, 'Nobitaaaaaaa!!!!',
                                     30, 'fonts/comic.ttf', c['red'], (30, 2/3*HEIGHT), prev = self._dora_res)
        self._use_mouse = BlinkText(self._screen, 'M to use Mouse',
                                     20, 'fonts/comic.ttf', c['red'], prev = self._dora_txt)
        self._use_mouse.value((self._mouses * self._mouseicon_w + 10, HEIGHT - 40), self._mouses)
        self._bullet_res = Bullet(self._use_mouse, self._screen, 'img/bullet.png',
                                  620, 470, limitx = WIDTH/2, limity = HEIGHT/2)
        self._res = [self._res_back, self._dora_res, self._dora_txt, self._use_mouse, self._bullet_res]
        self._mousesummon = pygame.image.load("img/summon_mouse.png")
        self._cd = 90
        self._ccd = self._cd

        self._score = TextObject(self._screen, 'Score: ', 25, 'fonts/comic.ttf', c['black'], (10, 45))

        self._menu_bg = pygame.image.load('img/menubg.png')
        self._cur_bg = 20
        self._bg_pos = (0, 600)
        self._background_text = TextObject(self._screen, 'Play', 120, 'fonts/comic.ttf', c['white'], (145, 375))

        self._pos_test = []
        self._test_img = pygame.image.load('img/test.png')
        self._test_img2 = pygame.image.load('img/eye.png')

        self._gOverText = midText(self._screen, "Game Over", 100, "fonts/comic.ttf", c["red"], (400, 200))
        self._gOscore = None
        self._gObtns = {
            "restart": midText(self._screen, "Restart", 40, "fonts/comic.ttf", c["yellow"], (400, 350)),
            "menu": midText(self._screen, "Menu", 40, "fonts/comic.ttf", c["green"], (400, 400)),
            "quit": midText(self._screen, "Quit", 40, "fonts/comic.ttf", c["red"], (400, 450))
        }

        self._mode = 'Menu'

        self.update()

    def menu(self):
        self._screen.fill(c['white'])

        self._screen.blit(self._menu_bg, self._bg_pos)

        if int(self._bg_pos[1]) != 0:
            x, y = self._bg_pos
            self._bg_pos = x, y*5/6
        else:
            self._bg_pos = (0,0)
            self._background_text.blit()

    def reset(self):
        self._gameOver = False
        self._player = FlashyPlayer(self._screen)
        self._mouses = 0
        self._max_count = 120
        self._count_down = self._max_count
        self._ccd = self._cd
        self._balls=[]
        self._nobihit = 0
        for c in self._res:
            c.reset()

    def over(self):
        self._screen.fill(c["white"])
        self._gOverText.blit()
        self._gOscore.blit()
        for key in self._gObtns:
            self._gObtns[key].blit()

    def play(self):
        if not self._gameOver:
            self._screen.fill(c['white'])
            if self._bullet_res.stop():
                gOscore = "Your score: {}".format(self._player.get_score())
                self._gOscore = midText(self._screen, gOscore, 20, "fonts/comic.ttf", c["dark_red"], (400, 300))
                self._gameOver = True
                self._mode = 'Over'

            if self._balls:
                for ball in self._balls:
                    ball.update()
                    _, y, r = ball.get_pos()
                    if y - r > HEIGHT:
                        self._balls.remove(ball)
                        if not ball.hit():
                            if ((not (ball.get_id() == 'dora' or ball.get_id() == 'nobi' or ball.get_id() == 'mouse'))
                                    and not self._nobihit):
                                self._player.change_health(-1)

            if not self._nobihit and self._cd == self._ccd:
                self._count_down -= 1
                if self._count_down == 0:
                    total_limit = 4
                    decision = random.randrange(100)
                    if decision < 30:
                        self._balls.append(Head(self._screen, 'dora', 40))
                        total_limit -= 1
                    if decision < 10:
                        self._balls.append(Head(self._screen, 'nobi', 40))
                        total_limit -= 1
                    self._count_down = self._max_count
                    if decision < 5 and self._mouses<3:
                        self._balls.append(Head(self._screen, 'mouse', 40))
                        total_limit -= 1
                    if total_limit > 0:
                        for _ in range(random.randrange(1, total_limit + 1)):
                            self._balls.append(Head(self._screen, random.choice(['goda', 'suneo']), 40))

                    if self._player.get_health() < 5:
                        choice = random.randrange(100)
                        if choice < 5:
                            if not self._specials:
                                self._specials.append(Dorami(self._screen))
                # else:
                #     print('ok')

                if self._specials:
                    for spec in self._specials:
                        spec.update()
                        _, y, _ = spec.get_pos()
                        if y <= -200:
                            self._specials.remove(spec)

                if self._mouse_hold:
                    self._player.update()
                    for ball in self._balls:
                        if Sprite.collide(self._player, ball):
                            ball.get_hit()
                            if ball.get_id() == 'dora':
                                self._player.change_health(-2)
                                self._player.change_score(ball.score())
                            elif ball.get_id() in ['goda', 'suneo']:
                                self._player.change_score(ball.score())
                            elif ball.get_id() == 'nobi':
                                self._nobihit = True
                                pygame.mixer.Sound.play(self._sfx_nobihit)
                            else:
                                self._balls.remove(ball)
                                self._mouses += 1
                                self._use_mouse.value((self._mouses * self._mouseicon_w + 10, HEIGHT - 40), self._mouses)
                    for spec in self._specials:
                        if spec.collide_mouse():
                            self._specials.remove(spec)
                            self._player.change_health(1)

            if self._nobihit or self._ccd < self._cd:
                for obj in self._res:
                    obj.update()
                if self._use_mouse.use() and self._ccd == self._cd:
                    self._nobihit = False
                    for obj in self._res:
                        if obj.id == "Dorarescue":
                            obj.change_img("img/dora_scared.png")
                    self._balls = []
                    self._mouses -= 1
                    self._use_mouse.value((self._mouses * self._mouseicon_w + 10, HEIGHT - 40), self._mouses)
                if not self._nobihit:
                    self._ccd -= 1
                    self._screen.blit(self._mousesummon, self._mousesummon.get_rect(bottomleft=(400,550)))
                    if self._ccd <= 0:
                        self._ccd = self._cd
                        for obj in self._res:
                            obj.reset()

            health = self._player.get_health()
            if health > 0:
                for i in range(health):
                    self._screen.blit(self._heart, (10 + (2 + self._heart_w) * i, 10))
            else:
                gOscore = "Your score: {}".format(self._player.get_score())
                self._gOscore = midText(self._screen, gOscore, 20, "fonts/comic.ttf", c["dark_red"], (400, 300))
                self._mode = "Over"
                self._gameOver = True

            self._score.update_text('Score: {}'.format(self._player.get_score()))

            if self._mouses:
                for i in range(self._mouses):
                    self._screen.blit(self._mouseicon, (self._mouseicon_w*i, HEIGHT - 54))

    def test(self):
        self._screen.fill(c['white'])
        self._screen.blit(self._test_img, (0,0))
        if self._pos_test:
            for x,y in self._pos_test:
                self._screen.blit(self._test_img2, (x-10,y-10))
        else:
            self._screen.blit(self._test_img2, (311 - 7, 210 - 10))
            self._screen.blit(self._test_img2, (455 - 7, 210 - 10))

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if self._mode == "Play":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self._mouse_hold = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            self._mouse_hold = False
                            self._player.reset()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.reset()
                            self._mode = 'Menu'
                elif self._mode == 'Menu':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self._background_text.get_hover():
                                self.reset()
                                self._mode = 'Play'
                            if 351 <= event.pos[0] <= 411 and 236 <= event.pos[1] <= 291:
                                self._mode = 'Test'
                    if event.type == pygame.MOUSEMOTION:
                        if 145 <= event.pos[0] <= 365 and 414 <= event.pos[1] <= 544:
                            # if (self._screen.get_at(event.pos) == (255,255,255,255) or
                            #         self._screen.get_at(event.pos) == (200,200,200,255)):
                            self._background_text.hover(True)
                        else:
                            self._background_text.hover(False)
                elif self._mode == 'Test':
                    if event.type == pygame.MOUSEMOTION:
                        ratio = 50/500
                        x1, y1 = int(event.pos[0]*ratio+271), int(event.pos[1]*ratio+180)
                        x2, y2 = int(event.pos[0]*ratio+415), int(event.pos[1]*ratio+180)
                        self._pos_test = [(x1, y1), (x2, y2)]
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 351 <= event.pos[0] <= 411 and 236 <= event.pos[1] <= 291:
                            self._mode = 'Menu'
                elif self._mode == "Over":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self._gObtns["restart"].mouse_in():
                                self.reset()
                                self._mode = "Play"
                            elif self._gObtns["menu"].mouse_in():
                                self._mode = "Menu"
                            elif self._gObtns["quit"].mouse_in():
                                self.quit()

            if self._mode == 'Play':
                self.play()
            elif self._mode == 'Menu':
                self.menu()
            elif self._mode == 'Test':
                self.test()
            elif self._mode == 'Over':
                self.over()

            pygame.display.update()
            self._clock.tick(self._frame)

    def quit(self):
        pygame.quit()
        quit()

def main():
    Game()

if __name__ == '__main__':
    main()

