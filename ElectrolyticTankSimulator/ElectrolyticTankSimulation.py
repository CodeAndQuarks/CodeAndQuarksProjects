# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:04:32 2020

@author: CodeAndQuarks
Desc: This is a simple program to demonstrate the formation of lines 
      of epipotential for an Electrolytic Tank.*
      *Still work-in-progress
      Python 3.7.1
"""
#imports
import numpy as np
from matplotlib import pyplot as plt
#constants
levels = np.arange(0, 100, 10)
#von-neumann neighbourhood boundary conditions
vonneumann=[(1,0),(-1,0),(0,1),(0,-1)]
#----------------------------------------------------------------------------
#Define User input variables
print("\nThis is a simple program to demonstrate the formation of lines "+
      "of epipotential for an Electrolytic Tank of dimensions 12cmx24cm.")
n=int(input('\nSelect the number of iterations you wish to carry out: '))
Vright=float(input('\nPlease give a suitable electrode voltage for the RHS: '))
Vleft=float(input('\nPlease give a suitable electrode voltage for the LHS: '))
#-----------------------------------------------------------------------------
try:
#-----------------------------------------------------------------------------
    temp=0
    #Check input values
    if n<0:
        n=0
        print('Invalid integer, n is set to 0.')
    if Vright<0.0:
        temp=Vright*(-1.0)
        Vright=temp
    if Vleft<0.0:
        temp=Vleft*(-1.0)
        Vleft=temp
#-----------------------------------------------------------------------------
    #define functions
    def ave_val_cell(i,j,a):
        """ Averaging of cells, to 5 decimal places"""
        total=0
        for dy, dx in vonneumann:
            total+=a[i+dx,j+dy]
        s=float(total/4)
        return np.round(s, 5)

    def iterateGrid(a,n):
        """Iterate n times over 2D array"""
        print('Iterating grid: ',n,'times.')
        for i in range(n): 
            for i in range(1,11):
                for j in range(1,23):
                    a[i,j]=ave_val_cell(i,j,a)
        print('Iteration Complete.')
        return a

    def createGrid(y,x,V1,V2):
        """Create a grid with user-defined
        electrode configuration"""
        print('Creating grid...')
        agrid = np.zeros(shape=(y,x))
        for i in range(y,x):
            #RHS X-AXIS
            agrid[0][i]=V1
            agrid[y-1][i]=V1
        for j in range(y):
            #LHS AND RHS Y-AXIS
            agrid[j][x-1]=V1
            agrid[j][0]=V2
        for n in range(0,y+1):
            #lHS X-AXIS
            agrid[0][n]=V2
            agrid[y-1][n]=V2
        print('\nGrid is ready.')   
        return agrid
#-----------------------------------------------------------------------------
    #Create, iterate and display grid.
    a=createGrid(12,24,Vright,Vleft) 
    #print(a)-Check grid values
    b=iterateGrid(a,n)
    #print(b)-Check grid values
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Electrolytic Tank 2-D Simulation")
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.grid(True)
    ax.contour(a, levels=levels)
    plt.draw()
    plt.show()
except ValueError:
    #temporary exception until I implement future improvements...
    print('A error occured please restart.')
