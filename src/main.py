#!/usr/bin/python3
import simpleguitk
import numpy as np
from Board import *

def draw_handler(canvas):
    global board
    printBoard(board, canvas) 
    board = updateBoard(board)

board = initializeBoard()

frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()