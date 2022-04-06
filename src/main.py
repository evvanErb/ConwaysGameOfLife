#!/usr/bin/python3
import simpleguitk
import numpy as np
from Board import *

def draw_handler(canvas):
    global board, currentGen
    printBoard(board, canvas) 
    board = updateBoard(board, currentGen)
    currentGen = np.copy(board)

board = initializeBoard()
currentGen = np.copy(board)

frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()