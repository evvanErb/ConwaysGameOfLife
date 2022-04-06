#!/usr/bin/python3
import time
import simpleguitk
from CellStatus import CellStatus
from Board import *

def draw_handler(canvas):
    global currentGen
    
    printBoard(board, canvas)
        
    updateBoard(board, currentGen)
                
    #Update currentGen board
    currentGen = updateCurrentGen(board, currentGen)
    time.sleep(0.001)

boardAndCurrentGen = initializeBoard()
board = boardAndCurrentGen[0]
currentGen = boardAndCurrentGen[1]

frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()