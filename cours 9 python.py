# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:13:00 2023

@author: Dell
"""
import matplotlib.pyplot as plt
import numpy as np

"""
%matplotlib inline
x=np.linspace(-2,2,101)
y=x**2
print(x)
"""

"""
plt.plot (x,y) #vector x,y
plt.title("Graph of x**2" )
plt.show #affiche le graphe

x=np.linspace(0,3*np.pi,101)
"""

"""
plt.plot (x,np.sin(x**2)) #vector x,y
plt.title("a simple chirp" )#on donne un titre au graphe
plt.show
"""
"""
%matplotlib inline
x=np.linspace(-2,2,101)
y = x**2
plt.plot(x,y,'g', label = "x**2")
plt.xlabel("x") #on donne un nom a l'axe des absicces
plt.ylabel("f(x)")#on donne un nom a l'axe des ordonnées
y2 = x**4
plt.plot (x,y2,'ro',label='x**4')#le troisieme (r) element correspond au changement de couleur et le "o" c'est pour mettre des points sur la courbe
plt.legend
plt.show
plt.savefig("fig1.png")
"""

def exo1():
    p = int(input("what number of points ?"))
    x = np.linspace(-1,1,p)
    y = np.cos(2*np.pi*x)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel("f(x)")
    plt.title("f(x) = cos(2pi*x)")
    plt.savefig("cos2pix.png")
    plt.show()
    
def exo2():
    p = int(input("what number of points ?"))
    x = np.linspace(-1,1,p)
    y = np.cos(2*np.pi*x)
    y2=np.sin(2*np.pi*x)
    plt.plot(x,y2)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel("f(x)")
    plt.title("f(x) = cos(2pi*x) anf g(x)=sin(2pi*x")

    plt.show()
    
def exo3():
    p = int(input("what number of points ?"))
    x = np.linspace(0,4,p)
    y = np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
    plt.plot(x,y)
    plt.show()

def exo4():
    p = int(input("what number of points ?"))
    t = float(input("what is the temperature during the experience"))
    x = np.linspace(2,10,p)
    y = 0.08206*t/x
    plt.plot(x,y)
    plt.xlabel('Vm')
    plt.ylabel('p')
    plt.title('Isotherm (ideal gas)')
    plt.show()
    plt.savefig("isotherm.jpg")
    
def exo5():
    p = int(input("Prompt the number of points"))
    start = int(input("where is the start ?"))
    end = int(input("Where is the end"))
    x0 = int(input("where is the center ?"))
    s = float(input("choose the width "))
    x = np.linspace(start,end,p)
    y=(1/(np.sqrt(2*np.pi)))*np.exp(-((x-x0)**2)/(2*(s)**2))
    plt.plot(x,y)
    plt.show()
    
def exo6():
        p = int(input("What is the number of points ?"))
        x = np.linspace(0, 3, p)
        y1 = np.sin(3*np.pi*x)*np.exp(-x)
        y2 = np.exp(-x)
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.title("Function")
    
def exo7():
    Xmin = int(input("What is the intial value of Xmin"))
    Xmax = int(input("What is the final value of Xmax"))  
    num = int(input("What is the number of point"))
    c = int(input("How many curves ?"))
    
    x = np.linspace(Xmin,Xmax,num )
    plt.title("gaussian functions")
    
    for i in range (0,c):
        x0 = int(input("What is the value of x0"))
        S = float(input("What is the value of S"))
        y = (1/(np.sqrt(2*np.pi)))*(np.exp((-1/2)*(((x-x0)**2)/(S**2))))
        plt.plot(x,y,label="gaussian {}".format(i))
    plt.legend()
    plt.show()

exo7()
    
    

