import pygame

pygame.init()

frame = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255,0)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def spot(x, y, r):
    pygame.draw.circle(screen, green, (x, y), r)

def main():
    num_spot = 100
    mouse_hold = False
    r = 10
    mouse_moves = []
    max_countdown = 2
    countdown = max_countdown
    while True:
        screen.fill(black)
        countdown -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_hold = True
                x, y = event.pos
                mouse_moves = [(x, y)]
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_hold = False
            if event.type == pygame.MOUSEMOTION:
                if mouse_hold:
                    x, y = event.pos
                    mouse_moves = [(x, y)] + mouse_moves

        if countdown == 0:
            countdown = max_countdown
            if len(mouse_moves) > 1:
                mouse_moves.remove(mouse_moves[-1])

        if len(mouse_moves) == num_spot:
            mouse_moves.remove(mouse_moves[-1])

        if mouse_moves:
            for i in range(len(mouse_moves)):
                x, y = mouse_moves[i]
                spot(x, y, int(r-i/(num_spot/r)))

        if len(mouse_moves) == 1 and mouse_hold == False:
            mouse_moves = []

        pygame.display.update()
        clock.tick(frame)

if __name__ == "__main__":
    main()