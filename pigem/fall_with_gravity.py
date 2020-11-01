import pygame
from math import sin, cos, pi
import random

pygame.init()

frame = 120 #per second

sec = 1/(frame) #1 second time in this world

g = 9.8

equations = {
    'x': 'x-axis',
    'y': 'y-axis',
    't': 'time',
    'py': 'y - (v0 * t * sin(a) - 1/2 * g * t**2)',
    'px': 'x + (v0 * t * cos(a))'
}

WIDTH, HEIGHT = 800, 600

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def add_thing(x, y, r):
    pygame.draw.circle(screen, white, (x, y), r)

def main():
    thing_x, thing_y, r = random.choice([-15, 815]), random.randrange(300, 600), 5
    t = 0
    if thing_x <0:
        v = 8
        a = pi * 7 / 18
    else:
        v = -8
        a = - pi * 7 / 18
    while True:
        screen.fill(black)
        t += sec
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        thing_x += int((v*t*cos(a)))
        thing_y -= int((v*t*sin(a)-1/2*g*t**2))
        print(v*t*sin(a)-1/2*g*t**2)

        add_thing(thing_x, thing_y, r)

        if thing_y > 630:
            thing_x, thing_y = random.choice([-15, 815]), random.randrange(300, 600)
            if thing_x < 0:
                v = 8
                a = pi * 7 / 18
            else:
                v = -8
                a = - pi * 7 / 18
            t = 0

        pygame.display.update()
        clock.tick(frame)

if __name__ == "__main__":
    main()
