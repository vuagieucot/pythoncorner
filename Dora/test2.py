import sys
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util


def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = (50, 150)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    return shape


def add_floor(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (0, 0)
    target = pymunk.Segment(body, (0, 5), (600, 5), 5)
    space.add(target)
    return target


def add_target(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (700, 300)
    target = pymunk.Segment(body, (-150, 0), (-150, 50), 5)
    space.add(target)
    return target

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    target = add_target(space)
    floor = add_floor(space)
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ball_count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        if ball_count < 1:
            ball_shape = add_ball(space)
            balls.append(ball_shape)
            ball_count += 1

        space.step(1/50.0)

        screen.fill((255,255,255))
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    main()