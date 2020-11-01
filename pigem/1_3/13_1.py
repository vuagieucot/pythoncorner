import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from r2r import R2r
from math import pi, cos, sin
from random import choice

# vertices = (
#     (-5, 0.5, 0.5), (-5, 0.5, -0.5), (-5, -0.5, -0.5), (-5, -0.5, 0.5),
#     (-1, 0.5, 0.5), (-1, 0.5, -0.5), (-1, -0.5, -0.5), (-1, -0.5, 0.5),
#     (-1, 1, -2), (-1, -1, -2), (-1, -1, 2), (-1, 1, 2),
#     (0, 1, -2), (0, -1, -2), (0, -1, 2), (0, 1, 2),
#     (0, 0, -1), (0, 0, 1), (10, 0, 1), (11, 0, 0), (10, 0, -1),
#     (0.5, 0, 0))
#
# edges =(
#     (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 6),
#     (5, 1), (5, 4), (5, 6), (7, 3), (7, 4), (7, 6),
#     (8, 9), (8, 11), (8, 12), (10, 9), (10, 11), (10, 14),
#     (13, 9), (13, 12), (13, 14), (15, 11), (15, 12), (15, 14),
#     (16, 17), (16, 20), (19, 20), (19, 18), (17, 18),
#     (19, 21), (16, 21), (17, 21))
#
# surfaces = (
#     (0 ,1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
#     (1, 5, 6, 2), (2, 6, 7, 3), (0, 4, 7, 3),
#     (8, 9, 10, 11), (12, 13, 14, 15), (10, 11, 15, 14),
#     (8, 11, 15, 12), (8, 9, 13, 12), (9, 10, 14, 13),
#     (16, 17, 18, 19), (16, 18, 19, 20))

colors = (
    (0, 0, 0),
    (1, 1, 1)
)

original = (0, 0, 0)

def sword():
    glBegin(GL_POINTS)
    max = 50
    r=1
    lat = R2r((0, max-1), (-pi, pi))
    lon = R2r((0, max-1), (-pi, pi))
    color = (1, 1, 1)
    for i in range(0, max):
        for j in range(0,max):
            x = r*sin(lon(i))*cos(lat(j))
            y = r*sin(lon(i))*sin(lat(j))
            z = r*cos(lon(i))
            glColor3fv(color)
            glVertex3fv((x, z, y))
            j+=1
        i+=1
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(150, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 1, 0)
                if event.button == 5:
                    glTranslatef(0, -1, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sword()

        glRotatef(1, 0, 1, 0)
        glRotatef(1, 1, 0.0, 0)
        pressed = pygame.key.get_pressed()
        if pressed[K_LSHIFT]:
            if pressed[K_UP]:
                glRotatef(1, 0, 1, 0)
            if pressed[K_DOWN]:
                glRotatef(1,0, -1, 0)
            if pressed[K_RIGHT]:
                glRotatef(1, 1, 0.0, 0)
            if pressed[K_LEFT]:
                glRotatef(1, -1, 0.0, 0)
        else:
            if pressed[K_UP]:
                glTranslatef(0, 0, 1)
            if pressed[K_DOWN]:
                glTranslatef(0, 0, -1)
            if pressed[K_RIGHT]:
                glTranslatef(1, 0.0, 0)
            if pressed[K_LEFT]:
                glTranslatef(-1, 0.0, 0)

        pygame.display.flip()
        pygame.time.wait(10)

main()