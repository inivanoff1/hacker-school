#!/bin/python

import math
import matplotlib.pyplot as plt
import numpy as np
import sys

angle = 0

points = input("How many points your circle has? ")
if points < 4 or points > 360:
     sys.exit("Input a number between 4 and 360!")

r = input("Input the radius: ")
if r < 1:
     sys.exit("Input a number larger than 1!")

for i in range(0, points):
     x = r * math.cos(angle * 3.14 / 180)
     y = r * math.sin(angle * 3.14 / 180)
     print "For %d degrees 'x' and 'y' coordinates are: " % angle 
     print "'x' is: ", round(x, 4)
     print "'y' is: ", round(y, 4)
     plt.scatter(x, y)
     i = i + 1
     angle = i * 360 / points

plt.show()
