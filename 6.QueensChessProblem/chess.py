#Solve how many queens can fit on a chess board without attacking each other
#using Djikstra's backtracking algorithm

import copy

def solve(n):
    #prepare a board
    board = [[0 for x in range(n)] for x in range(n)]
    #set initial positions
    solutions = list()
    return place_queen(4)

def place_queen(n):
    board = [[0 for x in range(n)] for x in range(n)]
    solutions = []
    row = column = 0

    while True: # loop unconditionally
        if len(board) in (row, column):
            if row == 0:
                return solutions
            elif row == len(board):
                solutions.append(copy.deepcopy(board))

            for c in range(len(board)):
                if board[row-1][c] == 1:
                    board[row-1][c] = 0

                    row -= 1     # directly change row and column, rather than recursing
                    column = c+1
                    break        # break out of the for loop (not the while)

        elif is_safe(board, row, column):   # need "elif" here
            board[row][column] = 1

            row += 1      # directly update row and column
            column = 0

        else:             # need "else" here
            column += 1   # directly increment column value

def is_safe(board, row, column):
    """ if no other queens threaten a queen at (row, queen) return True """
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                queen = (r,c)
                queens.append(queen)
    for queen in queens:
        qr, qc = queen
        #check if the pos is in the same column or row
        if row == qr or column == qc:
            return False
        #check diagonals
        if (row + column) == (qr+qc) or (column-row) == (qc-qr):
            return False
    return True


print(solve(4))