#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:28:11 2019

@author: jeffin
"""

from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Triangulation_2 import Delaunay_triangulation_2
 
from random import random
dt = Delaunay_triangulation_2()

# inserting random points
for i in range(20):
    dt.insert(Point_2(random(),random()))

"""
#pts = dt.points()  // Depricated : Probably used by old school students
for ip in pts:
    print(ip.x(), ip.y()) 
"""
    
fcs = dt.finite_faces()
vert = dt.finite_vertices()
numpts = dt.number_of_vertices()
print ("number of points:", numpts)
numfcs = dt.number_of_faces()
print ("number of points:", numfcs)

# counting edge since there is no direct function 

num = dt.all_edges()
numedg = 0
for e in num:
    # Uncomment the following line to print the x1,y1 (starting) and x2,y2 (ending) cordinates
    #print(dt.segment(e))  
    numedg = numedg + 1
print("number of edges ", numedg)


# comment out the follwoing lines if you don't want to print out the faces
for i in fcs:
    for j in range(0,3):
        print(i.vertex(j).point(),sep=' ')
    print()

# Printing the certices of Triangulations
for k in vert:
    print(k.point())

# Checking for valid Triangulation 
# The follwing code can find everything from overlap to point of failure
flag = 0
count_of_failure = 0
for i in fcs:
    for j in vert:
        if (dt.side_of_oriented_circle(i,j.point()) > 0):
            print("NOT A Valid Triangulation")
            flag = 1
            # Comment out the break statement and you will get answer for othe question
            break
            count_of_failure = count_of_failure + 1
            print("failure at vertex ", j.point())
            

if (flag == 0):
    print("The triangulation was Valid")
    
    
# alternatively you could also use is_valid(...) function
# the following only return bool value and doesn't say anythin about number of failure 
print(dt.is_valid())

