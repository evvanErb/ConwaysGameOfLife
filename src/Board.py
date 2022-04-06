#!/usr/bin/python3
import random
from CellStatus import CellStatus
from Sum import sum

def initializeAcorn():
    board = []
    currentGen = []
    #initialize board
    for row in range(100):
        board.append([])
        currentGen.append([])
        for column in range(100):
            board[row].append(CellStatus.DEAD)
            currentGen[row].append(CellStatus.DEAD)

    board[44][74] = CellStatus.ALIVE
    board[44][75] = CellStatus.ALIVE
    board[42][75] = CellStatus.ALIVE
    board[43][77] = CellStatus.ALIVE
    board[44][78] = CellStatus.ALIVE
    board[44][79] = CellStatus.ALIVE
    board[44][80] = CellStatus.ALIVE
    
    currentGen[44][74] = CellStatus.ALIVE
    currentGen[44][75] = CellStatus.ALIVE
    currentGen[42][75] = CellStatus.ALIVE
    currentGen[43][77] = CellStatus.ALIVE
    currentGen[44][78] = CellStatus.ALIVE
    currentGen[44][79] = CellStatus.ALIVE
    currentGen[44][80] = CellStatus.ALIVE
    
    return [board, currentGen]

def initializeRandom(seedValue):

    board = []
    currentGen = []
    random.seed(seedValue)

    for row in range(100):
        board.append([])
        currentGen.append([])
        for column in range(100):
            if(random.randint(0,9) == 0):
                board[row].append(CellStatus.ALIVE)
                currentGen[row].append(CellStatus.ALIVE)
            else:
                board[row].append(CellStatus.DEAD)
                currentGen[row].append(CellStatus.DEAD)

    return [board, currentGen]

def initializeBoard():

    seedValue = input("Enter a seed value:\n>>> ")
    boardAndCurrentGen = []
    
    if(seedValue == "acorn"):
        #initialize board
        boardAndCurrentGen = initializeAcorn()
        
    else:
        boardAndCurrentGen = initializeRandom(seedValue)

    return [boardAndCurrentGen[0], boardAndCurrentGen[1]]

#update curent gen board		
def updateCurrentGen(board, currentGen):
    for row in range(100):
        for column in range(100):
            currentGen[row][column] = board[row][column]
    return currentGen
    
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
            board[row][column] = rules(row, column, currentGen[row][column], currentGen)
    return board

def printBoard(board, canvas):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row][column] == CellStatus.ALIVE):
                y = row*10
                x = column*10
                canvas.draw_polygon([(x,y),(x,y+10),(x+10,y+10),(x+10,y)], 0 ,"Black","Black")
