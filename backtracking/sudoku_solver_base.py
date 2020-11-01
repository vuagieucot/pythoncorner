from board import board

def solve(bo):
    print_board(board)
    print('='*25)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            #backtrack if solve doesn't return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    for i in range(len(bo[0])):
        #if num in pos doesn't appear in another slot on same row
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(bo)):
        #if num in pos doesn't appear in another slot on same column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #check the 3x3 box containing position
    #row = (3box_row, 3box_row + 3)
    #row = (3box_col, 3box_col + 3)
    box_row, box_col = pos[0]//3, pos[1]//3

    for i in range(box_row*3, box_row*3+3):
        for j in range(box_col*3, box_col*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
            

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('-'*24)
        for j in range(len(bo[0])):
            if j%3 == 0 and j != 0:
                print(' | ', end = '')
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end = ' ')

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j) #row, column
    return None
    
print_board(board)
print('='*25)
solve(board)
print_board(board)
                   
