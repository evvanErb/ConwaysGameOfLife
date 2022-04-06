#!/usr/bin/python3
import simpleguitk
from Board import *

def draw_handler(canvas):
    global currentGen
    printBoard(board, canvas) 
    updateBoard(board, currentGen)
    currentGen = updateCurrentGen(board, currentGen)

boardAndCurrentGen = initializeBoard()
board = boardAndCurrentGen[0]
currentGen = boardAndCurrentGen[1]

frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()