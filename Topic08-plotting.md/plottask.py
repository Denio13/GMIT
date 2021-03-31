#the program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

#Author: Denis Sarf

import numpy as np
import matplotlib.pyplot as plt


def f(x): # function f(x)=x
    return x

def g(x):  #function g(x)=x2
    return x ** 2

def h(x):  #function h(x)=x3
    return x ** 3

x = np.array(range(0, 5))   #range [0, 4] range 0 to 3, 4 not included

plt.figure()
#The plot() function is used to draw points in a diagram and the function takes parameters for specifying points in the diagram.
plt.plot(x, f(x),  label = "f(x)=x")
plt.plot(x, g(x), 'o:r', label = "g(x)=x2")
plt.plot(x, h(x), '--', label = "h(x)=x3")
plt.legend() # A legend() is a function describing the elements of the graph.

font1 = {'family':'serif','color':'blue','size':20} #style chart title
plt.title("A plot of the functions", fontdict = font1) #title of graph

font2 = {'family':'serif','color':'green','size':10} #style chart xlabel and ylabel
plt.xlabel("Input(x)", fontdict = font2)
plt.ylabel("Output(x)", fontdict = font2)

plt.show() #display all open figures.
plt.savefig('chart.png')
    
