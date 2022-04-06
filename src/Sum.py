from CellStatus import CellStatus

def sum(row, column, currentGen):
    cellSum = 0
    
    #corners
    if((row == 0) and (column == 0)):
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    elif((row == 99) and (column == 0)):
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    elif((row == 0) and (column == 99)):
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        
    elif((row == 99) and (column == 99)):
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
        
    #sides
    elif(row == 0):
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    elif(row == 99):
        if(currentGen[row-1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    elif(column == 0):
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    elif(column == 99):
        if(currentGen[row+1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
    
    #center
    else:
        if(currentGen[row-1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row-1][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row][column+1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column-1] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column] == CellStatus.ALIVE):
            cellSum += 1
        if(currentGen[row+1][column+1] == CellStatus.ALIVE):
            cellSum += 1
            
    return cellSum