#the program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

#Author: Denis Sarf

import numpy as np
import matplotlib.pyplot as plt

#running function f(x)=x
def f(x):
    return x

#running function g(x)=x2
def g(x):
    return x ** 2

#running function h(x)=x3
def h(x):
    return x ** 3

#range [0, 4] range 0 to 3, 4 not included
x = np.array(range(0, 5))

# 'plt.figure()' is to create a figure object.
plt.figure()
#The plot() function is used to draw points in a diagram and the function takes parameters for specifying points in the diagram.
plt.plot(x, f(x),  label = "f(x)=x")
plt.plot(x, g(x), 'o:r', label = "g(x)=x2")
plt.plot(x, h(x), '--', label = "h(x)=x3")
# A legend() is a function describing the elements of the graph.
plt.legend() 

#giving a style to a chart title 
font1 = {'family':'serif','color':'blue','size':20} 
#giving a title to a graph
plt.title("A plot of the functions", fontdict = font1)

#giving a style to chart's xlabel and ylabel
font2 = {'family':'serif','color':'green','size':10} 
plt.xlabel("Input(x)", fontdict = font2)
plt.ylabel("Output(x)", fontdict = font2)

#displaying and saving as a .png format all open figures
plt.show()
plt.savefig('chart.png')
    
