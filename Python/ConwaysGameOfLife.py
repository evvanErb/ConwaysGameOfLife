#!/usr/bin/python
import random
import time
import simpleguitk

def initializeBoard():
	mySeed = raw_input("Enter a seed value:\n>>> ")
	
	if(mySeed == "acorn"):
		#initialize board
		for r in range(100):
			board.append([])
			currentGen.append([])
			for c in range(100):
				board[r].append(dead)
				currentGen[r].append(dead)

		board[44][74] = alive
		board[44][75] = alive
		board[42][75] = alive
		board[43][77] = alive
		board[44][78] = alive
		board[44][79] = alive
		board[44][80] = alive
		
		currentGen[44][74] = alive
		currentGen[44][75] = alive
		currentGen[42][75] = alive
		currentGen[43][77] = alive
		currentGen[44][78] = alive
		currentGen[44][79] = alive
		currentGen[44][80] = alive
		
	else:
		random.seed(mySeed)
		#initialize board
		for r in range(100):
			board.append([])
			currentGen.append([])
			for c in range(100):
				if(random.randint(0,9) == 0):
					board[r].append(alive)
					currentGen[r].append(alive)
				else:
					board[r].append(dead)
					currentGen[r].append(dead)

#update curent gen board		
def updateCurrentGen():
	for r in range(100):
		for c in range(100):
			currentGen[r][c] = board[r][c]

#sum adjacent cells
def sum(r, c):
	cellSum = 0
	
	#corners
	if((r == 0) and (c == 0)):
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		if(currentGen[r+1][c+1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
			
	elif((r == 99) and (c == 0)):
		if(currentGen[r-1][c] == alive):
			cellSum += 1
		if(currentGen[r-1][c+1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
			
	elif((r == 0) and (c == 99)):
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r+1][c-1] == alive):
			cellSum += 1
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		
	elif((r == 99) and (c == 99)):
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c] == alive):
			cellSum += 1
		
	#sides
	elif(r == 0):
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
		if(currentGen[r+1][c-1] == alive):
			cellSum += 1
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		if(currentGen[r+1][c+1] == alive):
			cellSum += 1
			
	elif(r == 99):
		if(currentGen[r-1][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c] == alive):
			cellSum += 1
		if(currentGen[r-1][c+1] == alive):
			cellSum += 1
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
			
	elif(c == 0):
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		if(currentGen[r+1][c+1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
		if(currentGen[r-1][c] == alive):
			cellSum += 1
		if(currentGen[r-1][c+1] == alive):
			cellSum += 1
			
	elif(c == 99):
		if(currentGen[r+1][c-1] == alive):
			cellSum += 1
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c] == alive):
			cellSum += 1
	
	#center
	else:
		if(currentGen[r-1][c-1] == alive):
			cellSum += 1
		if(currentGen[r-1][c] == alive):
			cellSum += 1
		if(currentGen[r-1][c+1] == alive):
			cellSum += 1
		if(currentGen[r][c-1] == alive):
			cellSum += 1
		if(currentGen[r][c+1] == alive):
			cellSum += 1
		if(currentGen[r+1][c-1] == alive):
			cellSum += 1
		if(currentGen[r+1][c] == alive):
			cellSum += 1
		if(currentGen[r+1][c+1] == alive):
			cellSum += 1
			
	return cellSum
	
#rules of game
def rules(r, c, current):
	cellSum = sum(r, c)
	#Underpopulation
	if(cellSum < 2):
		return False
	#Overpopulation
	elif(cellSum > 3):
		return False
	#Reproduction and same
	elif(cellSum == 3):
		return True
	#Same
	elif(cellSum == 2 and current):
		return True
	#Dead and only 2
	else:
		return False

		
#***MAIN***

board = []
currentGen = []
alive = "X"
dead = " "

initializeBoard()

#main loop	
def draw_handler(canvas):
	#print board
	for r in range(len(board)):
			for c in range(len(board[r])):
				if (board[r][c] == alive):
					y = r*10
					x = c*10
					canvas.draw_polygon([(x,y),(x,y+10),(x+10,y+10),(x+10,y)], 0 ,"Black","Black")
		
	#loop through board
	for r in range(len(board)):
		for c in range(len(board[r])):
			#run rules on cell
			if(currentGen[r][c] == alive):
				current = True
			else:
				current = False
			status = rules(r,c,current)
			#Change status
			if(status):
				board[r][c] = alive
			else:
				board[r][c] = dead
				
	#Update currentGen board
	updateCurrentGen()
	time.sleep(0.001)
	
frame = simpleguitk.create_frame('Conway\'s Game of Life', 1000, 1000)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()