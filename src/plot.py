#!/usr/bin/python

import matplotlib.pyplot as plt

f = open("npoints.txt","r")
no_of_points = map(int, f.read().split())
#print no_of_points
f.close()
index = [i+1 for i in range(len(no_of_points))]
plt.plot(index, no_of_points)
plt.title("Cumulative number of good GPS points as days pass")
plt.show()
