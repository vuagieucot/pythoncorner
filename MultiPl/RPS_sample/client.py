import pygame
import sys

try:
    from RPS_sample.network import Network
except:
    from network import Network

pygame.init()
width = 700
height = 700
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Rock Scissors Paper')

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.c = color
        self.w = 150
        self.h = 100
        font = pygame.font.SysFont('comicsans', 40)
        self._text = font.render(self.text, 1, (255,255,255))
        self._rect = self._text.get_rect()
        self._rect.x = self.x + round(self.w/2)-round(self._rect.width/2)
        self._rect.y = self.y + round(self.h/2)-round(self._rect.height/2)
        self._clickRect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))
        win.blit(self._text, self._rect)

    def click(self, pos):
        return self._clickRect.collidepoint(pos[0],pos[1])

btns = [Button('Rock', 50,500,(0,0,0)),
       Button('Scissors', 250, 500, (255,0,0)),
       Button('Paper', 450, 500, (0,255,0))]

def print_text(result, font, color):
    text = font.render(result, 1, color)
    rect = text.get_rect()
    win.blit(text, (int(width/2-rect.width/2), int(height/2-rect.height/2-50)))

def print_text2(text, font, color, pos):
    text = font.render(text, 1, color)
    win.blit(text, pos)

redrawFont = pygame.font.SysFont('comicsans', 60)
redrawFont2 = pygame.font.SysFont('comicsans', 80)
font = pygame.font.SysFont('comicsans', 90)
def redraw(win, game, p, result):
    win.fill((120, 230, 160))

    if not(game.connected()):
        print_text('Waiting for player...', redrawFont2, (255, 0,255))
    else:
        print_text2('Your Move', redrawFont, (0,255,255),(80,200))
        print_text2('Opponent', redrawFont, (0,255,255),(380,200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothPick():
            text1 = move1
            text2 = move2
        else:
            if game.move1 and p == 0:
                text1 = move1
            elif game.move1:
                text1 = 'Locked In'
            else:
                text1 = 'Waiting'

            if game.move2 and p == 1:
                text2 = move2
            elif game.move2:
                text2 = 'Locked In'
            else:
                text2 = 'Waiting'

        if p == 1:
            print_text2(text2, redrawFont,(120, 140, 250),(100,350))
            print_text2(text1, redrawFont,(120, 140, 250),(400,350))
        else:
            print_text2(text1, redrawFont,(120, 140, 250),(100,350))
            print_text2(text2, redrawFont,(120, 140, 250),(400,350))

        for btn in btns:
            btn.draw(win)

    if result[0]:
        print_text(result[1], font, (120,0,60))

    pygame.display.update()


def main():
    n = Network()
    p = int(n.get_data())
    print('You are player {}'.format(p))
    result = [False, None]
    run = True
    while run:
        clock.tick(60)
        try:
            game = n.send('get')
        except:
            print('Couldn\'t get the game...')
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for btn in btns:
                        if btn.click(pos) and game.connected():
                            if p == 0:
                                if not game.move1:
                                    n.send(btn.text)
                            else:
                                if not game.move2:
                                    n.send(btn.text)

        if game.bothPick():
            if game.winner()>=0:
                if game.winner()==p:
                    result = [True, 'You Won']
                else:
                    result = [True, 'You Lose']
            else:
                result = [True, 'Tie Game']
            redraw(win, game, p, result)
            pygame.time.delay(1500)
            try:
                game=n.send('reset')
                result = [False, None]
            except:
                print('Couldn\'t get the game...')
                run = False

        redraw(win, game, p, result)

def menu():
    font = pygame.font.SysFont('comicsans', 60)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    main()
        win.fill((120, 230, 160))
        print_text('Click to play',font, (235, 140, 50))
        pygame.display.update()

while True:
    sys.exit(menu())
