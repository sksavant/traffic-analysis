#!/usr/bin/python
from pylab import *

x = [0.01*i for i in range(201)]
y = [(1+0.15*(x1**4)) for x1 in x]

plot(x,y,linewidth=3.0)
xlabel('flow rate/capacity')
ylabel('link delay')
grid(True)
savefig('eqn_plot.png')
show()
