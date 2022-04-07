#!/usr/bin/python3
import simpleguitk
import numpy as np
from Board import *

def main(canvas):

    global board
    drawBoard(board, canvas) 
    board = updateBoard(board)


def init():

    global board
    board = initializeBoard()

    frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
    frame.set_canvas_background("White")
    frame.set_draw_handler(main)
    frame.start()
  
  
if __name__=="__main__":
    init()
