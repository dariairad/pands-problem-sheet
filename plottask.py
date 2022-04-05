# Problem Sheet - Weekly Task 08

# Task Description:
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plot

xpoints = np.array(range (0, 5))
ypointsf = xpoints              # f(x)=x
ypointsg = xpoints * xpoints    # g(x)=x2
ypointsh = xpoints ** 3         # h(x)=x3

plot.plot(xpoints, ypointsf, label='f(x)=x', color='red')
plot.plot(xpoints, ypointsg, label='g(x)=x\N{SUPERSCRIPT TWO}', color='green')
plot.plot(xpoints, ypointsh, label='h(x)=x\N{SUPERSCRIPT THREE}', color='blue')

plot.title('Exponents of x')
plot.legend()

plot.show()