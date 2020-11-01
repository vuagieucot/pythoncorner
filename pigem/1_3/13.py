import pygame
from pygame.locals import *
import random
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, -1),
    (-1, -1, 1))
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
    (7, 6))

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

# ground_vertices = (
#     (-20, -0.5, 20),
#     (20, -0.5, 20),
#     (-20, -0.5, -300),
#     (20, -0.5, -300))
#
# def ground():
#     glBegin(GL_QUADS)
#     for vertex in ground_vertices:
#         glColor3fv((0, 0.5, 0.5))
#         glVertex3fv(vertex)
#     glEnd()

def set_vertices(max_distance, min_distance = -20, camera_x = 0, camera_y = 0):

    camera_x = -1*int(camera_x)
    camera_y = -1*int(camera_y)

    x_value_change = random.randrange(camera_x-10, camera_x+10)
    y_value_change = random.randrange(camera_y-10, camera_y+10)
    z_value_change = random.randrange(-1*max_distance, min_distance)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change
        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    return tuple(new_vertices)

def cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x += 1
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 0 , 0))
            glVertex3fv(vertices[vertex])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #.

    max_distance = 100

    gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)

    glTranslatef(random.randrange(-5, 5), 0, -40)

    cur_x = 0
    cur_y = 0

    cube_dict = {}
    for x in range(40):
        cube_dict[x] = set_vertices(max_distance)

    while True:
        x_move = 0
        y_move = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslatef(0, 0.0, 1)
            #     if event.button == 5:
            #         glTranslatef(0, 0.0, -1)
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            y_move = -0.3
        if pressed[K_DOWN]:
            y_move = 0.3
        if pressed[K_RIGHT]:
            x_move = -0.3
        if pressed[K_LEFT]:
            x_move = 0.3

        glTranslatef(x_move, y_move, 0)

        view = glGetDoublev(GL_MODELVIEW_MATRIX)

        # camera_x = view[3][0]
        # camera_y = view[3][1]
        camera_z = view[3][2]

        cur_x += x_move
        cur_y += y_move

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glTranslatef(0, 0, 1)

        # ground()

        for each in cube_dict:
            cube(cube_dict[each])


        delete_list = []

        for each in cube_dict:
            if camera_z <= cube_dict[each][0][2]:
                new_max = int(-1*(camera_z - max_distance))

                cube_dict[each] = set_vertices(new_max, int(camera_z - 50), cur_x, cur_y)


        pygame.display.flip()

main()
pygame.quit()
quit()
