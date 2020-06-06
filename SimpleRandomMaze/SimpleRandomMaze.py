# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:34:08 2020
@author: CodeAndQuarks
Desc: A simple random maze generator that randomly creates a maze of size
      in the range of (3x3-20x20).
      There are modules I could have used to randomise the range,
      but I wanted to see if I could randomise it myself, 
      to generalise its use for future projects where 
      implementation is dependent on user input. 
"""
#imports
import numpy as np
import random as rd
#define functions
def randomdraw(array):
    """Randomly select a integer"""
    const=len(array)
    evenprob=(100.0/(const))
    probs=[evenprob]*(const)
    draw=np.random.choice(array,1,probs)
    number=int(draw)
    return number
def createpath(xf, yf, maze, row, col):
    """Create a useable path through the maze"""
    neighbourhood = [(xf - 1, yf), (xf + 1, yf), (xf, yf - 1), (xf, yf + 1)]
    maze[yf][xf] = 1
    #each time createpath is called, neighbour will shuffle
    rd.shuffle(neighbourhood)
    for (xt, yt) in neighbourhood:
        if maze[yt][xt]:
            continue
        if xt == xf: 
            row[max(yf, yt)][xf] = "+  "
        if yt == yf:
            col[yf][max(xf, xt)] = "   "
        #keep iterating 
        createpath(xt, yt, maze, row, col)
def GenMaze(width, height):
    """Generate a random text-based maze with backtracking"""
    mymaze = ""  
    xf=rd.randrange(width)
    yf=rd.randrange(height)
    maze = [[0] * width + [1] for _ in range(height)] + [[1] * (width + 1)]
    col = [["|  "] * width + ['|'] for _ in range(height)] + [[]]
    row = [["+--"] * width + ['+'] for _ in range(height + 1)]
    #iterate
    createpath(xf,yf,maze,row,col)
    #convert to string    
    for (r, c) in zip(row, col):
        mymaze += ''.join(r + ['\n'] + c + ['\n'])
    #return maze
    return mymaze
def createfile(Maze):
    print('Opening file....')
    file = open("RandomMaze.txt", "w") 
    print('Writing Maze to text-file....')
    file.write(Maze) 
    file.close() 
    print('Maze sucessfully re-configured')
def main():
    arr=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #randomise the width and the height
    width=randomdraw(arr)
    height=randomdraw(arr)
    Maze=GenMaze(width, height)
    #examine maze
    print(Maze)
    #Create a new randommaze text file.
    createfile(Maze)
#create maze
main()
