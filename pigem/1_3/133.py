import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Classes.Cube import Cube

display = (800, 600)

class CubeGame:
    """
    Cube game.
    """
    def __init__(self):
        """
        Construct a new game
        """
        pygame.init()
        self._screen = None
        self._passed = False

        self._max_distance = 100
        self._min_distance = -20

        self._current = (0, 0)

        self._cube = []
        for _ in range(30):
            self._cube.append(Cube(self._max_distance, self._min_distance))

        self._camera_x, self._camera_y, self._camera_z = None, None, None

    def launch(self):
        """
        launch game.

        :return:
        """
        self._screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, self._max_distance)
        glTranslatef(0.0, 0.0, -60)
        self.main()

    def draw(self):
        """
        draw the cube.

        :return:
        """
        for cube in self._cube:
            cube.draw()

    def game_quit(self):
        """
        quit game

        :return:
        """
        pygame.quit()
        quit()

    def _get_pressed(self):
        """
        Reponse to player's pressing

        :return:
        """
        move_x = 0
        move_y = 0
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            move_y = -0.3
        if pressed[K_DOWN]:
            move_y = 0.3
        if pressed[K_RIGHT]:
            move_x = -0.3
        if pressed[K_LEFT]:
            move_x = 0.3
        self._current = (self._current[0] + move_x, self._current[1] + move_y)
        glTranslatef(move_x, move_y, 0)

    def update(self):
        """
        update every game moment.

        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit()

        self._get_pressed()

        view =  glGetDoublev(GL_MODELVIEW_MATRIX)

        [self._camera_x, self._camera_y, self._camera_z, _] = view[3]

        for cube_object in self._cube:
            cube = cube_object.get_cube()
            if cube[0][2] >= self._camera_z:
                cube_object.redraw(self._camera_z, self._max_distance,
                                   self._min_distance, self._current)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glTranslatef(0, 0, 1.5)

        self.draw()

        pygame.display.flip()

    def main(self):
        """
        game main run function.

        :return:
        """
        while True:
            self.update()

if __name__ == "__main__":
    game = CubeGame()
    game.launch()
    game.game_quit()
