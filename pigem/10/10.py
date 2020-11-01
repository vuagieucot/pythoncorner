import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600  # easier to modify later

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
gray=(100,100,100)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_yellow = (255,255,200)

block_color = (53, 115, 225)

gameDisplay = pygame.display.set_mode((display_width, display_height))  # create a 800x600 window
pygame.display.set_caption("Dodging car")  # window title
clock = pygame.time.Clock()  # create game time

carImg = pygame.image.load('im/myCar.png')
car2Img = pygame.image.load('im/myCar2.png')
planeImg = pygame.image.load('im/plane.png')
(car_width, car_height) = carImg.get_rect().size  # get size of car image


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color, a):
    for i in a:
        pygame.draw.rect(gameDisplay, color, [thingx + i, thingy, thingw, thingh])


def car(img,x, y):
    """
    Display car image into the given position of the game

    :param img: image of the car
    :param x: x-cordinator
    :param y: y-cordinator
    """
    gameDisplay.blit(img, (x, y))  # blit display the image


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont('comicsansms', 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_intro()

def game_quit():
    pygame.quit()
    quit()

def crash():
    message_display('You Crashed! Idiot!')

def round_rect(x,y,w,h, i):
    """
    Create a round rectangle.

    :param x: x_cor
    :param y: y_cor
    :param w: width
    :param h: height
    :param i: color
    :return:  nothing
    """
    X,Y,W,H=x+10,y+10,w-20,h-20

    pygame.draw.rect(gameDisplay, i, (x,Y, w, H))
    pygame.draw.rect(gameDisplay, i, (X,y, W, h))

    pygame.draw.circle(gameDisplay, i, (X,Y), 10)
    pygame.draw.circle(gameDisplay, i, (X+W,Y), 10)
    pygame.draw.circle(gameDisplay, i, (X,Y+H), 10)
    pygame.draw.circle(gameDisplay, i, (X+W,Y+H), 10)

    pygame.draw.rect(gameDisplay, i, (X,Y,W,H))

def button(msg, x,y,w,h, i, a, com=None):
    """
    Create a button.

    Parameter(s):
    :param msg: message
    :param x: x_cordinator
    :param y: y-cordinator
    :param w: width
    :param h: height
    :param i: inactive color
    :param a: active color
    :param com: command
    """
    round_rect(x,y,w,h, i)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if (x+w) > mouse_pos[0] > x and (y+h) > mouse_pos[1] > y:
        if mouse_click[0]==1 and com is not None:
            com()
        round_rect(x-1, y-1, w+2, h+2, gray)
        round_rect(x,y,w,h, a)

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+w/2), (y+h/2))
    gameDisplay.blit(textSurf, textRect)

def choose_car(img, position):
    """
    Blitting the car image to the choosing vehicle window.

    :param img: image
    :param position (int): 1 or 2 or 3
    """
    mouse_hover = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()

    smallx = display_width/6
    car_pos = (display_width*position/3-smallx - car_width / 2, display_height / 2 - car_height / 2)

    if display_width*(position-1)/3<mouse_hover[0]<display_width*position/3:
        pygame.draw.rect(gameDisplay, bright_yellow, (display_width*(position-1)/3, 0, display_width/3, display_height))
        gameDisplay.blit(img, car_pos)
    else:
        gameDisplay.blit(img, car_pos)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects("Dodging car", largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #button(msg, x,y,w,h, i, a)
        button("START", 150,450,100,50,green, bright_green, game_chooseCar)
        button("QUIT", 550,450, 100,50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)

def game_chooseCar():
    chooseCar=True
    while chooseCar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # i do not like this way though
                if 0<mouse_pos[0]<display_width*1/3:
                    game_loop(carImg)
                elif display_width*1/3<mouse_pos[0]<display_width*2/3:
                    game_loop(car2Img)
                elif display_width*2/3<mouse_pos[0]<display_width*3/3:
                    game_loop(planeImg)

        gameDisplay.fill(white)

        choose_car(carImg, 1)
        choose_car(car2Img, 2)
        choose_car(planeImg, 3)

        carText = pygame.font.SysFont('comicsansms', 40)
        textSurf, textRect = text_objects("Choose your car", carText)
        textRect.center = ((display_width/2), 100)
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)

def game_loop(img):
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

    count=0

    gameExit = False
    while not gameExit:
        # list of event happening in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close window (hit X)
                game_quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            x = x + car_speed
        if pressed[pygame.K_LEFT]:
            x = x - car_speed

        gameDisplay.fill(white)

        count += 1

        things(thing_startx, thing_starty, thing_width, thing_height, block_color, a)
        thing_starty += thing_speed
        car(img, x, y)
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

        if thing_starty < y < thing_starty+thing_height or thing_starty < y+car_height < thing_starty+thing_height:
            for i in a:
                if (thing_startx + i < x < thing_startx + i + thing_width
                        or thing_startx + i < x + car_width < thing_startx + i + thing_width):
                    crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_quit()
