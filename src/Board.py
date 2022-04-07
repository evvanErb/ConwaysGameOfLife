#!/usr/bin/python3
import random
import numpy as np
from CellStatus import CellStatus

def initializeBoard():

    seedValue = input("Enter a seed value:\n>>> ")
    board = np.full((100, 100), CellStatus.DEAD)
    
    if (seedValue == "acorn"):
        board[44, 80] = board[44, 79] = board[44, 78] = board[43, 77] = board[42, 75] = board[44, 75] = board[44, 74] = CellStatus.ALIVE

    else:
        random.seed(seedValue)
        for row in range(100):
            for column in range(100):
                if(random.randint(0,9) == 0):
                    board[row, column] = CellStatus.ALIVE
    
    return board

def sumAliveNeighbors(row, column, board):

    numAliveNeighbors = 0
    
    for rowModifier in range(-1,2):
        for columnModifier in range(-1,2):

            if (not (row + rowModifier < 0 or row + rowModifier > 99 or column + columnModifier < 0 or column + columnModifier > 99)):
                    if ((board[(row+rowModifier), (column+columnModifier)] == CellStatus.ALIVE) and (rowModifier != 0 or columnModifier != 0)):
                        numAliveNeighbors += 1

    return numAliveNeighbors
    
#rules of game
def rules(row, column, board):

    numAliveNeighbors = sumAliveNeighbors(row, column, board)

    if (numAliveNeighbors == 3 or (numAliveNeighbors == 2 and board[row, column] == CellStatus.ALIVE)):
        return CellStatus.ALIVE
    else:
        return CellStatus.DEAD

def updateBoard(board):

    boardCopy = np.copy(board)

    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row, column] = rules(row, column, boardCopy)

    return board

def drawBoard(board, canvas):

    for row in range(len(board)):
        for column in range(len(board[row])):

            if (board[row, column] == CellStatus.ALIVE):
                y = row*10
                x = column*10
                canvas.draw_polygon([(x,y),(x,y+10),(x+10,y+10),(x+10,y)], 0 ,"Black","Black")

