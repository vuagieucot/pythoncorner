class R2r:
    """
    Mapping 2 range to a linear function
    """
    def __init__(self, range1, range2):
        """
        Set up a new linear handler
        f(x) = range2 = a*range1 + b.
        Domain value(x) in range1 only

        :param range1 (tuple(2)): Domain
        :param range2 (tuple(2)): Range
        """
        self._range1 = tuple(range1)
        self._range2 = tuple(range2)
        self._gradient = None
        self._y_tercept = None
        self._build()

    def _build(self):
        x1, x2 = self._range1
        y1, y2 = self._range2
        self._gradient = (y1-y2)/(x1-x2)
        self._y_tercept = y1 - self._gradient*x1

    def __call__(self, value: float):
        x1, x2 = self._range1
        if x1 <= value <= x2:
            return self._gradient * value + self._y_tercept
        else:
            raise ValueError('Value out of range.')

    def __repr__(self):
        return 'y = {}x + {}'.format(self._gradient, self._y_tercept)


