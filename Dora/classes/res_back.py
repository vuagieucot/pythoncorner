from classes.Nobihit import Nobihit

class Res_back(Nobihit):
    def update(self):
        self._rect.bottomright = (self._x, self._y)
        if self._x < self._limit_x and int(1 / 10 * (self._limit_x - self._x)) != 0:
            self._x += int(1 / 15 * (self._limit_x - self._x))
        if self._x > 800:
            self._stay = True
        super().update()

    def stay(self):
        return self._stay