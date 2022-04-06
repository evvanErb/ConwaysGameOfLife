#!/usr/bin/python3
import random
import numpy as np
from CellStatus import CellStatus

def initializeAcorn():

    board = np.full((100, 100), CellStatus.DEAD)

    board[44, 74] = CellStatus.ALIVE
    board[44, 75] = CellStatus.ALIVE
    board[42, 75] = CellStatus.ALIVE
    board[43, 77] = CellStatus.ALIVE
    board[44, 78] = CellStatus.ALIVE
    board[44, 79] = CellStatus.ALIVE
    board[44, 80] = CellStatus.ALIVE
    
    return board

def initializeRandom(seedValue):

    board = np.full((100, 100), CellStatus.DEAD)
    random.seed(seedValue)

    for row in range(100):
        for column in range(100):
            if(random.randint(0,9) == 0):
                board[row, column] = CellStatus.ALIVE

    return board

def initializeBoard():

    seedValue = input("Enter a seed value:\n>>> ")
    
    if(seedValue == "acorn"):
        #initialize board
        return initializeAcorn()
        
    else:
        return initializeRandom(seedValue)

def sum(row, column, currentGen):
    cellSum = 0
    for rowModifier in range(-1,2):
        for columnModifier in range(-1,2):

            if (not (row + rowModifier < 0 or row + rowModifier > 99 or column + columnModifier < 0 or column + columnModifier > 99)):
                    if ((currentGen[(row+rowModifier), (column+columnModifier)] == CellStatus.ALIVE) and (rowModifier != 0 or columnModifier != 0)):
                        cellSum += 1

    return cellSum
    
#rules of game
def rules(row, column, current, currentGen):
    cellSum = sum(row, column, currentGen)
    #Underpopulation
    if(cellSum < 2):
        return CellStatus.DEAD
    #Overpopulation
    elif(cellSum > 3):
        return CellStatus.DEAD
    #Reproduction and same
    elif(cellSum == 3):
        return CellStatus.ALIVE
    #Same
    elif(cellSum == 2 and current == CellStatus.ALIVE):
        return CellStatus.ALIVE
    #Dead and only 2
    else:
        return CellStatus.DEAD

def updateBoard(board, currentGen):
    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row, column] = rules(row, column, currentGen[row][column], currentGen)
    return board

def printBoard(board, canvas):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row, column] == CellStatus.ALIVE):
                y = row*10
                x = column*10
                canvas.draw_polygon([(x,y),(x,y+10),(x+10,y+10),(x+10,y)], 0 ,"Black","Black")

