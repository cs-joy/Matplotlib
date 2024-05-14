# -*- coding: utf-8 -*-
"""01_matplotlib_tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EuNzvazQnsvyk-CQkwtl1nDIGdFNiZMp

# Documentation

## 1. PyPlot - https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py
"""

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5]) # plt() - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.ylabel('same numbers')
plt.show()

"""You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to plot, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0; therefore, the x data are [0, 1, 2, 3]."""

#  an arbitrary number of arguments
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

"""#### Formatting the style of your plot
For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue
"""

|plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis((0, 6,0,20))
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'r+')
plt.axis((0, 6,0,20))
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'r-') # by default
plt.axis((0, 6,0,20)) # axis() - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'r*')
plt.axis((0, 6,0,20)) # The axis function in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes
plt.show()

"""### NumPy"""

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**2.5, 'y+', t, t**3, 'g^')
plt.show()

"""#### Plotting with keyword strings"""

data = {
          'a': np.arange(50),
          'c': np.random.randint(0, 50, 50),
          'd': np.random.randn(50)
        }

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d'] * 100)

data
print(f"length of data= {len(data)}")

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

