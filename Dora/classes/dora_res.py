from classes.Nobihit import Nobihit

class Dora_res(Nobihit):
    def __init__(self, previous, screen, img_path, x_right_start, y_bottom_start, limitx, limity):
        super().__init__(screen, img_path, x_right_start, y_bottom_start, limitx, limity)
        self._prev = previous
        self.id = "Dorarescue"

    def reset(self):
        super().reset()

    def update(self):
        if self._prev.stay():
            self._rect.bottomright = (self._x, self._y)
            if self._x > self._limit_x:
                self._x -= 20
            else:
                self._stay = True
            super().update()

class Bullet(Nobihit):
    def __init__(self, prev, screen, img_path, x_centerstart, y_centerstart, limitx, limity):
        super().__init__(screen, img_path, x_centerstart, y_centerstart, limitx, limity)
        self._prev = prev
        self._ori = self._img
        self._rect  = self._img.get_rect(center = (self._x, self._y))
        self._w, self._h = self._rect.width, self._rect.height
        self._ori_rect = self._w, self._h
        self._vel = 0
        self._lim = 2500
        self._incr = 40
        self._del = 2
        self._cur = self._del

    def reset(self):
        super().reset()
        self._vel = 0
        self._cur = self._del
        self._w, self._h = self._ori_rect

    def update(self):
        if self._prev.stop():
            super().update()
            if self._x <= self._limit_x and self._y <= self._limit_y:
                self._stay = True
            if not self._stay:
                self._cur -= 1
                if self._cur == 0:
                    self._cur = self._del
                    self._vel += 1
                self._x -= self._vel
                self._y -= self._vel
            if self._w < self._lim and self._h < self._lim:
                self._w = self._w+self._incr
                self._h = self._h+self._incr
                self._img = self.scale(self._ori, self._w, self._h)
            self._rect = self._img.get_rect(center = (self._x, self._y))

