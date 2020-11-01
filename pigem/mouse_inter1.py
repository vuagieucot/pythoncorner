import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

def draw_rect(x, y, w, h):
    pygame.draw.rect(screen, white, (x, y, w, h))

def main():
    thing_x, thing_y = 400, 300
    thing_w, thing_h = 40, 40
    gap_x = 0
    gap_y = 0
    mouse_hold = False
    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if (thing_x <= x <= thing_x + thing_w
                            and thing_y <= y <= thing_y + thing_h):
                        gap_x = x-thing_x
                        gap_y = y-thing_y
                        mouse_hold = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_hold = False
                    gap_x = 0
                    gap_y = 0
            if event.type == pygame.MOUSEMOTION and mouse_hold:
                mo_x, mo_y = event.pos
                thing_x, thing_y = mo_x - gap_x, mo_y - gap_y

        draw_rect(thing_x, thing_y, thing_w, thing_h)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()