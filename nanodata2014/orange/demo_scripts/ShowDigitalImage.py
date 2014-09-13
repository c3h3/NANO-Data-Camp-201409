import numpy as np
from matplotlib import pylab
import matplotlib.cm as cm
data_arr = in_data.to_numpy()[0]
pylab.ion()
pylab.imshow(data_arr[0,:].reshape(28,28),cmap=cm.gray)
pylab.show()