# ConwaysGameOfLife
A Python 3 implementation of Conway's Game Of Life

## How to Run

To install dependancies run: `pip3 install -r requirements.txt`

To run: `python3 src/main.py`

Uses simpleguitk for graphics

## Game Rules

### Underpopulation

Dies if less than two neighbors
    
### Overpopulation
Dies if more than three neighbors
    
### Reproduction

If exactly three neighbors and cell is dead it comes alive or stays alive if already alive

### Stays Alive / Dead

If exactly two neighbors stays alive if alive or dead if dead
