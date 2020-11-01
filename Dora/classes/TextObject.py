import pygame

class TextObject:
    def __init__(self, screen, text, size, font, color, position, acolor= (200,200,200)):
        self._text = text
        self._ifont = pygame.font.Font(font, size)
        self._afont = pygame.font.Font(font, size+5)
        self._surf = self._ifont.render(text, True, color)
        self._rect = self._surf.get_rect()
        self._rect = position
        self._screen = screen
        self._i = color
        self._a = acolor
        self._hover = False
        self.id = None

    def blit(self):
        if self._a:
            if self._hover:
                self._surf = self._afont.render(self._text, True, self._a)
            else:
                self._surf = self._ifont.render(self._text, True, self._i)
        self._screen.blit(self._surf, self._rect)

    def update_text(self, text):
        self._surf = self._ifont.render(text, True, self._i)
        self._screen.blit(self._surf, self._rect)

    def hover(self, bol):
        self._hover = bol

    def get_hover(self):
        return self._hover

class midText(TextObject):
    def __init__(self, screen, text, size, font, color, position, acolor=None, func=None):
        super().__init__(screen, text, size, font, color, position, acolor = acolor)
        self._rect = self._surf.get_rect(center = position)
        self.func=func

    def mouse_in(self):
        mouse = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse):
            return True
        else:
            return False

class RunningText(TextObject):
    def __init__(self, screen, text, size, font, color, position, prev = None):
        super().__init__(screen, text, size, font, color, position)
        self._pos = position
        self._ori_text = self._text
        self._text = ''
        self._font = self._ifont
        self._count = len(self._ori_text)
        self._cur = 0
        self._stop = False
        self._prev = prev

    def setup(self, text):
        self._text = text
        self._surf = self._font.render(text, True, self._i)

    def reset(self):
        self._cur = 0
        self._stop = False

    def stop(self):
        return self._stop

    def update(self):
        if (not self._prev) or (self._prev.stop()):
            self.setup(self._ori_text[:self._cur])
            self._screen.blit(self._surf, self._rect)
            if self._cur < self._count:
                 self._cur += 1
            else:
                self._stop = True

class BlinkText(RunningText):
    def __init__(self, screen, text, size, font, color, prev = None):
        super().__init__(screen, text, size, font, color, position=(0,0))
        self._prev = prev
        self._rect = self._surf.get_rect()
        self._num = 0
        self._trans = 5
        self._count = 60*3
        self._skip = False

    def reset(self):
        super().reset()
        self._count = 60*3
        self._skip = False

    def stop(self):
        return self._stop

    def value(self, pos, num):
        self._num = num
        self._rect.x, self._rect.y = pos

    def blink(self):
        if self._i[2] <= 50 or self._i[1] <=50:
            self._trans = 5
        elif self._i[2] >= 250 or self._i[1] >= 250:
            self._trans = -5
        self._i = self._i[0], self._i[1]+self._trans, self._i[2]+self._trans
        self._surf = self._font.render(self._ori_text, True, self._i)

    def wait(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_m]:
            self._count = 0
            self._skip = True
            self._stop = False

    def use(self):
        return self._skip

    def update(self):
        if self._prev.stop():
            if self._num > 0 and self._count > 0:
                self._count -= 1
                self._screen.blit(self._surf, self._rect)
                self.blink()
                self.wait()
            elif not self._skip:
                self._stop = True