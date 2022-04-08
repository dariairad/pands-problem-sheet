# Problem Sheet - Weekly Task 08

# Task Description:
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plot

xpoints = np.array(range (0, 5))
ypointsf = xpoints              
ypointsg = xpoints * xpoints    
ypointsh = xpoints ** 3         

plot.plot(xpoints, ypointsf, label='f(x)=x', color='magenta')
plot.plot(xpoints, ypointsg, label='g(x)=x\N{SUPERSCRIPT TWO}', color='purple')
plot.plot(xpoints, ypointsh, label='h(x)=x\N{SUPERSCRIPT THREE}', color='blue')


plot.title('Exponential Functions')
plot.xlabel('Values')
plot.ylabel('Exponents of values')
plot.grid()
plot.legend()

plot.show()