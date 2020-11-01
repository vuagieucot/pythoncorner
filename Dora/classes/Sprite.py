class Sprite:
    def __init__(self, Id = None, x=None, y=None, r = None):
        self._id = None
        self._x = x
        self._y = y
        self._r = r

    @staticmethod
    def collide(player, ball):
        if player.get_pos() and ball.get_pos():
            x1, y1, r1 = player.get_pos()
            x2, y2, r2 = ball.get_pos()
            if not ball.hit():
                if x1 and y1 and r1 and x2 and y2 and r2:
                    if r1 < r2:
                        if x2-r2 <= x1 <= x2+r2 and y2-r2 <= y1 <= y2+r2:
                            return True
                        else: return False
                    else:
                        if x1 -r1 <= x2 <= x1 + r1 and y1 -r1 <= y2 <= y1+r1:
                            return True
                        else: return False
            else: return False

    def get_id(self):
        return self._id

    def get_pos(self):
        if self.get_id() == 'suneo':
            return self._x+8, self._y +12, self._r
        else:
            return self._x, self._y, self._r