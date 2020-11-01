import pygame

pygame.init()

white =(255,255,255)
black = (0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("drawing stuff")
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, blue, (100,200),(300,450),1)

pygame.draw.rect(gameDisplay, red, (400,400, 50, 20))

pygame.draw.circle(gameDisplay, white, (150,150), 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
