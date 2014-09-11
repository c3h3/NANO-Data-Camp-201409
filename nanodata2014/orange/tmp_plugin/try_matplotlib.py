from matplotlib import pylab
import numpy as np
pylab.ion()

x = np.linspace(0,1,101)
p = pylab.plot(x,x**2)