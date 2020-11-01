import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600  # easier to modify later

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

block_color = (53, 115, 225)

gameDisplay = pygame.display.set_mode((display_width, display_height))  # create a 800x600 window
pygame.display.set_caption("Whatever")  # window title
clock = pygame.time.Clock()  # create game time

carImg = pygame.image.load('im/myCar.png')
(car_width, car_height) = carImg.get_rect().size  # get size of car image


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color, a):
    for i in a:
        pygame.draw.rect(gameDisplay, color, [thingx + i, thingy, thingw, thingh])


def car(x, y):
    """
    Display car image into the given position of the game
    """
    gameDisplay.blit(carImg, (x, y))  # blit display the image


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed! Idiot!')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    car_speed = 5

    thing_speed = 5
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_count = 1

    dodged = 0

    a = [0]

    gameExit = False
    while not gameExit:
        # list of event happening in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close window (hit X)
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: x += car_speed
        if pressed[pygame.K_LEFT]: x += -car_speed

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color, a)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        # group of logics of the game
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.3
            car_speed += 0.3
            if dodged % 5 == 0:
                if thing_count < 4:
                    thing_count += 1
                a = []
                for i in range(0, thing_count):
                    a.append(random.randrange(-display_width / 2, display_width / 2))

        if y < thing_starty + thing_height:
            for i in a:
                if x > thing_startx + i and x < thing_startx + i + thing_width or x + car_width > thing_startx + i and x + car_width < thing_startx + i + thing_width:
                    crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
