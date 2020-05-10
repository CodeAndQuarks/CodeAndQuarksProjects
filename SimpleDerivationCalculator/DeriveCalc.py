# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:15:08 2020

@author: CodeAndQuarks
Desc: A modified derivative calculator I made in my final year.*
      *Still in development for improvement
      Written in Python 3.7.1
"""
#Imports
import numpy as np
from matplotlib import pyplot as plt
#-----------------------------------------------------------------------------
#functions for plotting
def derivative_2nd(f,x,h):
    """function to calaculate 2nd derivative"""
    h = float(h)
    func=f(x)
    return (f(x+h)-(2*func)+(f(x-h)))/(h*h)

def three_point_derivative(f,x,h):
    """#3-point function to calaculate 1st derivative"""
    h = float(h)
    return (1/(2*h))*(f(x-2*h) - 4*f(x-h) + 3*f(x))

def five_point_derivative(f,x,h):
    """#5-point function to calaculate 1st derivative"""
    h = float(h)
    return (1/(12*h))*(f(x-2*h)-f(x+2*h)-
            8*f(x-h)+8*f(x+h))
def f(x):
    """Tan(X)/X"""
    return (np.tan(x)/x)

def g(x):
    """Cos(X)/X"""
    return (np.cos(x)/x)
def k(x):
    """Sin(X)/X"""
    return (np.sin(x)/x)
def checkTitle(func, r):
    """Change title according to function in use"""
    a=f(r)
    b=g(r)
    c=k(r)
    comp=func(r)
    #.all() checks all values in each array match
    if (comp==a).all():
        Title='Tan(X)/X'
    elif (comp==b).all():
        Title='Cos(X)/X'
    elif (comp==c).all():
        Title='Sin(X)/X'
    return Title
def plotresults(func, x1, x2):
    """Graph Function"""
    #create range
    r = np.linspace(x1, x2,1000)
    #update title
    Title=''+checkTitle(func,r)
    plt.figure()
    plt.plot(r,func(r),'b')
    plt.plot(r,three_point_derivative(func,r,h),'r--')
    plt.plot(r,derivative_2nd(func,r,h),'g')
    plt.plot(r,five_point_derivative(func,r,h),'m--')
    plt.xlim(x1,x2)
    plt.ylim(-0.45,1)
    
    #label axis and title 
    plt.xlabel('x',fontsize=14,color='r')
    plt.ylabel('y',fontsize=14,color='r')
    plt.title(r''+Title+' Point Derivatives',color='r')
    #set y-axis limit
    plt.legend(["f(x)", " 3-point derivative","d2f/dx", '5-point derivative'], 
            loc='upper right')
    #format grid
    ax = plt.gca()
    ax.grid(True)
    #draw to memory
    plt.draw()
    #show graph
    plt.show()

#------------------------------------------------------------------------------
#take h=0.01
h=0.01
#Take in user input for a range of  values
x1=int(input('Please set X1, for range x1<=X<=x2, example, -20:'))
x2=int(input('Please set X2, for range x1<=X<=x2, example,  20:'))
try: 
    if x2<=x1:
       #error check
       x2=x1+10
       print('X1>=X2, X2 has been altered to provide suitable visuals')
    #Plotting
    plotresults(f, x1,x2)
    plotresults(g, x1,x2)
    plotresults(k, x1,x2)
except ValueError:
    x1=-20
    x2=20
    print('ValueError generated, (X1,X2) has defaulted to (-20,20)')
    #Plotting
    plotresults(f, x1,x2)
    plotresults(g, x1,x2)
    plotresults(k, x1,x2)

