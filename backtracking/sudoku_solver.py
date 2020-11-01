import pygame
import sys
import random
import datetime

from pygame.locals import *
from board import boards

w, h = 540,600
rows, cols = 9, 9
grid= w//9

board = random.choice(boards)

class Cube:
    def __init__(self,screen, grid, pos, num, default = False):
        self._screen = screen
        self._grid = grid
        self._x, self._y = pos[0]*grid, pos[1]*grid
        self._col, self._row = pos
        self._choose = False
        self._num = num
        self._temp_num = self._num
        if num == 0:
            self._num = None
            self._temp_num = None
        if self._num:
            self._surf, self._rect = text_object(self._num)
        else:
            self._surf, self._rect = text_object('')
        self._rect.x,self._rect.y,self._rect.width,self._rect.height=(self._x+20,
                                                                      self._y+15,
                                                                      self._grid,
                                                                      self._grid)
        self._real_rect = pygame.Rect((self._x,self._y,self._grid,self._grid))
        self._default = default
        self._change = False
        self._valid = True

    def val(self, bol):
        self._valid = bol

    def change(self):
        return self._change

    def reset(self):
        self._change=False

    def num(self):
        if self._num is None:
            return 0
        else:
            return self._num

    def colnrol(self):
        return self._col, self._row

    def process(self, bol):
        if bol:
            if self._num != self._temp_num:
                self._change = True
            self._num = self._temp_num
        if self._num:
            self._surf, self._rect = text_object(self._num)
        else:
            self._surf, self._rect = text_object('')
        self._rect.x, self._rect.y, self._rect.width, self._rect.height = (self._x+20,
                                                                           self._y+15,
                                                                           self._grid,
                                                                           self._grid)
        self._temp_num = self._num

    def inp(self, num):
        self._temp_num = num
        if self._temp_num:
            self._surf, _ = text_object(self._temp_num)
        else:
            self.blit()

    def mouse_in(self):
        mouse=pygame.mouse.get_pos()
        return self._real_rect.collidepoint(mouse[0],mouse[1])

    def choose(self, bol):
        if not self._default:
            self._choose = bol

    def blit(self, color=None):
        if self._num:
            num = self._num
        else:
            num = ''
        if color is not None:
            self._surf, self._rect = text_object(num, color=color)
        else:
            self._surf, self._rect = text_object(num)

        self._rect.x, self._rect.y, self._rect.width, self._rect.height = (self._x + 20,
                                                                           self._y + 15,
                                                                           self._grid,
                                                                           self._grid)

    def chose(self):
        return self._choose

    def update(self):
        if self._choose:
            pygame.draw.rect(self._screen, (50,50,50),
                             (self._x, self._y, self._grid, self._grid))

        if not self._choose:
            if not self._valid:
                    self.blit((255,0,0))
            else:
                self.blit()

        self._screen.blit(self._surf, self._rect)


class Btn:
    def __init__(self, screen, text, pos):
        self._screen = screen
        font = pygame.font.SysFont('comicsans', 30)
        self._text = font.render(text, 1, (255,200,30))
        self._rect = self._text.get_rect()
        self._rect.x, self._rect.y = int(pos[0]-self._rect.w/2), pos[1]
        self._hover=False

    def btn(self):
        if self._hover:
            pygame.draw.rect(self._screen, (200,200,200),
                             (self._rect.x-5, self._rect.y-5,self._rect.w+10, self._rect.h+10))
        pygame.draw.rect(self._screen, (0,0,0),
                         (self._rect.x-3, self._rect.y-3, self._rect.w+6, self._rect.h+6))

    def mouse(self):
        mouse=pygame.mouse.get_pos()
        return self._rect.collidepoint(mouse)

    def update(self):
        self.btn()
        self._screen.blit(self._text, self._rect)
        self._hover = self.mouse()


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo,  i, (row, col)):
            bo[row][col] = i
            #recursive move
            if solve(bo):
                return True
            # backtrack if solve doesn't return True
            bo[row][col] = 0
    return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)  # row, column
    return None

def valid(bo, num, pos):
    for i in range(len(bo[0])):
        # if num in pos doesn't appear in another slot on same row
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        # if num in pos doesn't appear in another slot on same column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # check the 3x3 box containing position
    # row = (3box_row, 3box_row + 3)
    # row = (3box_col, 3box_col + 3)
    box_row, box_col = pos[0] // 3, pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def text_object(num, color = (255,255,0)):
    text=str(num)
    font = pygame.font.SysFont('comicsans', 50)
    surf = font.render(text, 1, color)
    rect = surf.get_rect()
    return surf, rect

def draw_lines(scrn):
    for row in range(rows+1):
        for col in range(cols+1):
            if row%3 ==0:
                pygame.draw.line(scrn,(200,200,200),(0, row*grid),(w, row*grid), 4)
            else:
                pygame.draw.line(scrn,(255,255,255),(0, row*grid),(w, row*grid), 1)
            if col%3 ==0:
                pygame.draw.line(scrn,(200,200,200),(col*grid, 0),(col*grid, w), 4)
            else:
                pygame.draw.line(scrn,(255,255,255),(col*grid, 0),(col*grid, w), 1)

def make_cube(screen):
    result = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 0:
                result.append(Cube(screen,grid, (col, row), board[row][col], default = True))
            else:
                result.append(Cube(screen, grid, (col, row), board[row][col]))
    return result

def take_board(cubes):
    result = [[],[],[],[],[],[],[],[],[]]
    for cube in cubes:
        _, row = cube.colnrol()
        result[row].append(cube.num())
    return result

def main():
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption('Sudoku Solver')
    clock = pygame.time.Clock()
    btn = Btn(screen, 'Solve', (w/2, h-40))
    cubes = make_cube(screen)
    key = None
    pick = 0
    cur = take_board(cubes)
    lastmove = None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_1:
                    key = 1
                if event.key == K_2:
                    key = 2
                if event.key == K_3:
                    key = 3
                if event.key == K_4:
                    key = 4
                if event.key == K_5:
                    key = 5
                if event.key == K_6:
                    key = 6
                if event.key == K_7:
                    key = 7
                if event.key == K_8:
                    key = 8
                if event.key == K_9:
                    key = 9
                if event.key == K_BACKSPACE:
                    key = None
                if event.key == K_ESCAPE:
                    key = None
                    pick = 0
                    for cube in cubes:
                        cube.choose(False)
                        cube.process(False)
                if event.key == K_RETURN:
                    key = None
                    pick = 0
                    for cube in cubes:
                        cube.choose(False)
                        cube.process(True)
                        if cube.change():
                            lastmove = cube
                        cube.reset()
                    cur = take_board(cubes)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if btn.mouse():
                        curtime = datetime.datetime.now()
                        solve(board)
                        print(datetime.datetime.now()-curtime)
                        cubes = make_cube(screen)
                    else:
                        for cube in cubes:
                            if cube.mouse_in() and pick == 0:
                                pick = 1
                                cube.choose(True)

        screen.fill((0,0,0))
        for cube in cubes:
            cube.update()
            if cube.chose():
                cube.inp(key)
        if lastmove:
            if lastmove.num() != 0:
                col, row = lastmove.colnrol()
                lastmove.val(valid(cur, lastmove.num(), (row,col)))
            lastmove = None
        if find_empty(cur) is None:
            print('Solved')
        btn.update()
        draw_lines(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    sys.exit(main())