from OpenGL.GL import *

import random

vertices = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    (0.25, -0.75, 1),
    (0, 0.2, 1),
    (-0.25, -0.75, 1),
    (0.12, 0.3, 1),
    (0.75, 0.6, 1),
    (-0.12, 0.3, 1),
    (-0.75, 0.6, 1),
    (0.3, 1, 1),
    (-0.3, 1, 1),
    (0.6, 1.5, 1),
    (-0.6, 1.5, 1))
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 6),
    (5, 1),
    (5, 4),
    (5, 6),
    (7, 3),
    (7, 4),
    (7, 6),
    (8, 9),
    (9, 10),
    (11, 12),
    (13, 14),
    (0, 17),
    (17, 15),
    (16, 18),
    (18, 4))

surfaces = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 3, 7, 4),
    (1, 2, 6, 5))

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0.5, 0.5, 0.5),
    (1, 1, 1),
    (0, 1, 1),
)

class Cube:
    """
    build a 3d cube.
    """
    def __init__(self, max_distance, min_distance):
        """
        Construct a new cube

        :param screen: pygame screen
        """
        self._pos_camera = (0, 0)
        self._max_distance = max_distance
        self._min_distance = min_distance
        self._cube = self.set_cube()

    def redraw(self, camera_z, max_distance, min_distance, current_position):
        self._pos_camera = current_position
        self._max_distance = int(-(camera_z - max_distance))
        self._min_distance = int((camera_z + min_distance))
        self._cube = self.set_cube()

    def get_cube(self):
        return self._cube

    def set_cube(self):
        x, y = -int(self._pos_camera[0]), -int(self._pos_camera[1])
        x_change = random.randrange(x-10, x+10)
        y_change = random.randrange(y-10, y+10)
        z_change = random.randrange(-1*self._max_distance, self._min_distance)

        result = []

        for vertex in vertices:
            x = x_change + vertex[0]
            y = y_change + vertex[1]
            z = z_change + vertex[2]
            result.append((x, y, z))

        return tuple(result)

    def draw(self):
        glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                glColor3fv(colors[x])
                glVertex3fv(self._cube[vertex])
                x += 1
        glEnd()
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv((1, 1, 1))
                glVertex3fv(self._cube[vertex])
        glEnd()