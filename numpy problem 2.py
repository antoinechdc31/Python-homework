# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:02:19 2023

@author: Dell
"""

import numpy as np
import random as random

def exo1():
    x =np.arange(0,21)
    x[9:16]=- x[9:16]
    
def exo2():
    x = np.arange(15,56)
    print(x[1:-1])
    
def exo3():
    x = np.array[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    for i in range(0,len(x[1])):
        for j in range(0,x[0]):
            print("")

def exo4():
    x = np.linspace(10,50,10)
    print(x)
    


def exo5():
    vector = np.empty(5, dtype=int)
    for i in range(5):
        while True:
            try:
                value = int(input(f"Enter an integer between 0 and 10 for element {i + 1}: "))
                if 0 <= value <= 10:
                    vector[i] = value
                    break
                else:
                    print("Value must be between 0 and 10. Try again.")
            except ValueError:
                        print("Invalid input. Please enter an integer between 0 and 10.")
    print("User-defined vector:", vector)


def exo6():
    a = np.array[2,3,4]
    b = np.array[5,6,7]
    c = np.matmul(a,b)
    print(c)
    
def exo7():
    matrice = np.zeros((3, 4))
    for i in range (0,3):
        for j in range (0,4):
            matrice[i,j]=random.randint(10, 21)
    print(matrice)

def exo8():
    matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


    num_rows, num_columns = matrix.shape

    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    
def exo9():
    matrix = np.zeros((4, 4), dtype=int)

    matrix[1::2, ::2] = 1
    matrix[::2, 1::2] = 1
    print(matrix)

def exo10():
    Array1= np.array([ 0 ,10 ,20 ,40, 60,40])
    Array2= np.array([10, 30, 40])
    l3=[]
    for i in range (0,len(Array1)):
        for j in range (len(Array2)):
            if Array1[i]==Array2[j]:
                l3.append(Array1[i])
    l4= np.unique(l3)           
    print(l4)

def exo11():
   l1=np.array([10, 10, 20, 20 ,30, 30])
   l2=np.unique(l1)
   print(l2)
   
def exo12():
    l1=np.array([2,3,4])
    l2=np.array([5,6,7])
    l3=np.cross(l1,l2)
    print(l3)
    
def exo13():
    mat = np.zeros((10,2))
    for i in range (0,10) :
       for j in range (0,2) :
           mat[i,j] = np.random.randint(-10,10)
          
    x = mat[:, 0]
    y = mat[:, 1]
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    deg = np.degrees(theta)
    polmat = np.column_stack((r, deg))
    print(mat)
    print(polmat)
    
def exo14():
   a = np.array( [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,
50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,
75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
   b = float(input("Choose a number between 0 and 100"))
   c = round(b,0)
   for i in range(0,len(a)):
       if a[i]==c:
           print("le rang du nombre le plus proche est {}".format(i))
       
   print (c)
exo14()
    

    









    
    
